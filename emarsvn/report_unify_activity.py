'''

@author: hankedang
'''

import subprocess, datetime, sys;


def command(cmd):
    num = 0
    status = subprocess.Popen(cmd, shell=True).wait();
    if(status != 0):
        while True:
            num +=  1
            status = subprocess.Popen(cmd, shell=True).wait();
            if(num >=  2):
                return status;
            if(status != 0):
                continue
    else:
        return 0
        

def data_import(date):
#    hive_sql = """ /data/hadoop/spark-1.6.0-bin-hadoop2.6/bin/spark-sql --name wangchenchen -e "
    hive_sql=""" /data/hadoop/hive-1.1.0-cdh5.5.0/bin/hive  -e"
        add jar /data/scriptMarket/udf/UDF.jar;
        create temporary function d_arr as 'com.emar.udf.DArray';
        insert overwrite table report.report_unify_activity partition(day_id='"""+ date +"""', hour_id)
        select a.channel_id, a.proj_id, a.campaign_id, bid_num, imp, invalid_imp, click, invalid_click, rtb_price, rtb_price_succ, bid_cost, arrive_num, jump_out_num, reg_num, 
        if(order_num is null, 0, order_num) as order_num, if(order_price is null, 0, order_price) as order_price, total_stay_time, is_rd,
        uv, pv, shop_cart_num, shop_cart_price, a.hour_id from
        (
        select channel_id, proj_id, campaign_id, sum(bid_num) as bid_num, sum(imp) as imp, sum(invalid_imp) as invalid_imp, sum(click) as click,  sum(invalid_click) as invalid_click,
        sum(rtb_price) as rtb_price, sum(rtb_price_succ) as rtb_price_succ, sum(bid_cost) as bid_cost, hour_id 
        from dm.unify_report
        where day_id='"""+ date +"""'
        group by channel_id, proj_id, campaign_id, hour_id
        ) a
        left outer join
        (
        select channel_id, project_id, campaign_id, count(session_id) as arrive_num, 
        sum(if(page_view=1, 1, 0)) as jump_out_num, sum(reg_num) as reg_num,
        sum(if(is_rd = 1 and order_no is not null, d_arr(order_no,2), 0)) as order_num,
        sum(if(is_rd = 1 and order_no is not null, d_arr(order_total, 1), 0)) as order_price, 
        sum(total_stay_time) total_stay_time, 1 as is_rd, sum(shop_cart) shop_cart_num, 
        count(distinct user_id) as uv, sum(page_view) as pv, sum(shop_cart_price) as shop_cart_price, hour_id
        from dm.adwiser_session 
        where day_id='"""+ date +"""'
        and s_ad_channel_code='dsp' and s_ad_source_code='emar'
        and is_rd <> 2
        group by channel_id, project_id, campaign_id, hour_id
        ) b
        on a.channel_id = b.channel_id and a.proj_id = b.project_id and a.campaign_id = b.campaign_id and a.hour_id = b.hour_id
    " """
    print hive_sql
    return command(hive_sql)

def rd_fill(date):
    hive_sql = """ /data/hadoop/hive-1.1.0-cdh5.5.0/bin/hive -e "
        add jar /data/scriptMarket/udf/UDF.jar;
        create temporary function d_arr as 'com.emar.udf.DArray';
        insert into table report.report_unify_activity partition(day_id='"""+ date +"""', hour_id)
        select channel_id, project_id, campaign_id, '' as bid_num, '' as imp, '' as invalid_imp, '' as click, '' as invalid_click, '' as rtb_price, 
        '' as rtb_price_succ, '' as bid_cost,  '' as arrive_num, '' as jump_out_num, '' as reg_num, sum(if(order_no is not null, d_arr(order_no,2), 0)) as order_num,
        sum(if(order_no is not null, d_arr(order_total, 1), 0)) as order_price, '' as total_stay_time, 2 as is_rd, '' as shop_cart_num, 
        '' as uv, '' as pv, '' as shop_cart_price, hour_id
        from dm.adwiser_session
        where day_id='"""+ date +"""'
        and is_rd = 2
        group by channel_id, project_id, campaign_id, hour_id
    " """
    print hive_sql
    return command(hive_sql)
	
# %Y%m%d %Y-%m-%d %Y%m 
def getDateFormat(formatStr, day):
    return (datetime.datetime.now() - datetime.timedelta(days=day)).strftime(formatStr)

def mailto(date,pwd, jobname, maillist):
    cmd = """ python "nohup """ + pwd + """/report.report_activity.py '""" + date +"""' &" | mail -s "Job --""" + jobname + """-- fail" """ + maillist
    command(cmd);
    
if __name__ == '__main__':
    pwd = """/data/scriptMarket/report/"""
    jobname = """214 report.report_activity job  hive """ + pwd + """/report.report_activity """
    to = """"""
    
    date = getDateFormat('%Y%m%d', 1)
    month = getDateFormat('%Y%m', 1)
    
    if(len(sys.argv) == 2):
        date = sys.argv[1]
        month = date[0:6]
    
    r1 = data_import(date)
    if r1 != 0:
        print 'report.report_activity hive job tried 3 times all failed'
        mailto(date, pwd, jobname, to)
        sys.exit(1)

    r1 = rd_fill(date)
    if r1 != 0:
        print 'report.report_activity , rd_fill job tried 3 times all failed'
        mailto(date, pwd, jobname, to)
        sys.exit(1)
