'''

@author: wcc
'''

import subprocess, datetime, sys, time;


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

def data_insert(date):
    hive_sql = """ /data/hadoop/spark-1.6.0-bin-hadoop2.6/bin/spark-sql --name wangchenchen -e"
insert overwrite table report.reqandunify_channel_report partition(day_id='"""+date+"""',hour_id)
select channel_id, flow_type,project_id, campaign_id, creative_id,
    sum(req_count) req_count, sum(bid) bid, sum(imp) imp, sum(clk) clk, sum(rtb_price) rtb_price, sum(rtb_cost) rtb_cost, sum(bid_cost) bid_cost,
    sum(order_num) order_num, sum(order_price) order_price, sum(arrive_num) arrive_num, sum(pv) pv, sum(jump_out_num) jump_out_num,
    sum(reg_num) reg_num, sum(stop_time) stop_time, sum(jump_num) jump_num, sum(uv) uv, sum(shop_cart) shop_cart,
    sum(shop_cart_price) shop_cart_price, sum(invalid_click) invalid_click, sum(activate_num) activate_num,hour_id
from(

    select channel_id,if(traffic_type=1,'mobile_web',flow_type) flow_type, null as project_id,null as campaign_id,null as creative_id,
    sum(req_count) req_count,
        0 bid, 0 imp, 0 clk, 0 rtb_price, 0 rtb_cost, 0 bid_cost, 0 order_num, 0 order_price, 0 arrive_num, 0 pv, 0 jump_out_num,
        0 reg_num, 0 stop_time, 0 jump_num, 0 uv, 0 shop_cart, 0 shop_cart_price, 0 invalid_click, 0 activate_num,hour_id
    from dw.dw_adx_req 
    where day_id = '"""+date+"""'
    group by if(traffic_type=1,'mobile_web',flow_type), channel_id,hour_id

union all

    select channel_id, bidding_client_type flow_type, a.proj_id as project_id, a.campaign_id, a.idea_id as creative_id,
        0 req_count, sum(bid_num) bid, sum(imp) imp , sum(click) clk, sum(rtb_price) rtb_price, sum(rtb_succ_price) rtb_cost, sum(bid_cost) bid_cost, 
        sum(order_num) order_num, sum(order_price) order_price, sum(arrive_num) arrive_num, sum(pv) pv, sum(arrive_num-jump_out_num) jump_out_num, 
        sum(reg_num) reg_num, sum(stay_time) stop_time, sum(jump_out_num) jump_num, sum(uv) uv, sum(shop_cart_num)shop_cart, 
        sum(shop_cart_price)shop_cart_price, sum(invalid_click) invalid_click, 0 activate_num,hour_id
    from (select * from report.report_unify_adsite where day_id = '"""+date+"""') a 
    left outer join xview.campaign b
    on a.campaign_id=b.campaign_id
    group by channel_id, bidding_client_type,hour_id,a.campaign_id, a.proj_id, a.idea_id

union all

    select channel_id, if(adreq_type='' or adreq_type is null,'mobile_app','mobile_native') flow_type, null as project_id,null as campaign_id,null as creative_id,
    sum(req_count) req_count,
    0 bid, 0 imp,0 clk,0 rtb_price,0 rtb_cost,
    0 bid_cost,
    0 order_num, 0 order_price, 0 arrive_num, 0 pv, 0 jump_out_num, 
    0 reg_num,0 stop_time, 0 jump_num, 0 uv,
    0 shop_cart, 0 shop_cart_price,0 invalid_click,0 activate_num,hour_id
    from report.report_app_statistics
    where day_id='"""+date+"""'
    group by channel_id,  if(adreq_type='' or adreq_type is null,'mobile_app','mobile_native'),hour_id

union all

    select channel_id, if(adreq_type='' or adreq_type is null,'mobile_app','mobile_native') flow_type, project_id, campaign_id, creative_id,
    0 req_count,sum(bid_count) bid, sum(impr_count) imp,sum(click_count) clk,sum(bid_price) rtb_price,sum(win_price) rtb_cost,
    sum(bid_cost) bid_cost,
    sum(order_num) order_num, sum(order_price) order_price, sum(arrive_num) arrive_num, sum(pv) pv, sum(arrive_num-jump_out_num) jump_out_num, 
    sum(reg_num) reg_num,sum(total_stay_time) stop_time, sum(jump_out_num) jump_num, sum(uv) uv,
    0 shop_cart, 0 shop_cart_price,0 invalid_click,sum(active_count) activate_num,hour_id
    from report.report_app_statistics
    where day_id='"""+date+"""'
    group by channel_id,  if(adreq_type='' or adreq_type is null,'mobile_app','mobile_native'), project_id, campaign_id,creative_id,hour_id
) t 
group by channel_id, flow_type, project_id, campaign_id, creative_id,hour_id;

    " """
    print(hive_sql)
    return command(hive_sql)

# %Y%m%d %Y-%m-%d %Y%m 
def getDateFormat(formatStr, day):
    return (datetime.datetime.now() - datetime.timedelta(days=day)).strftime(formatStr)

def mailto(date,pwd, jobname, maillist, msg):
    cmd = """ echo "nohup """ + pwd + sys.argv[0]+ date +""" &\n """ + msg +""" " | mail -s "Job --""" + jobname + """-- fail" """ + maillist
    print(cmd)
    command(cmd);
    
if __name__ == '__main__':
    pwd = """/data/xview/bid_statistics/"""
    jobname = 'new hadoop clusters\'s job ' + pwd + sys.argv[0]
    to = """wangchenchen@emar.com jiaqiang@emar.com """

    date = getDateFormat('%Y%m%d', 1)
    month = getDateFormat('%Y%m', 1)
    begin=time.time()


    if(len(sys.argv) == 2):
        date = sys.argv[1]
        month = date[0:6]
    

    r=data_insert(date)
    alltime=time.time()-begin
    print("LogTime ", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())), ": Finish ", sys.argv[0],
          " Job Cost time:", round(alltime / 60, 0), 'm', round(alltime % 60, 0), 's')
    if r!= 0:
        msg = jobname + ' . data_insert tried 3 times all failed'
        print(msg)
        mailto(date, pwd, jobname, to, msg)
        sys.exit(1)


