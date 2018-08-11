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
        


def create_table(table_name):
    mysql_sql = """ mysql -h 192.168.4.235 -udmpapadmin -p'dc077e28' -D xview -e "
create table if not exists xv_bid_l3_1_"""+table_name+"""(
    rep_date datetime DEFAULT NULL COMMENT 'yyyyMMdd',
    trade_type int(1) DEFAULT NULL  COMMENT 'rtb:1,no_rtb:0',
    channel_id int(4) DEFAULT NULL ,
    project_id int(6) DEFAULT NULL ,
    campaign_id int(7) DEFAULT NULL ,
    flow_type varchar(20) DEFAULT NULL COMMENT 'pc_web,mobile_web,mobile_app,mobile_native',
    creative_id int(7) DEFAULT NULL ,
    is_rd int(1) DEFAULT 0 COMMENT '1:notrd,2:rd,0:others or donot have orders',
    region_code int(10),
    domain varchar(100) DEFAULT NULL,
    adslot_id varchar(100) DEFAULT NULL,
    bid bigint(20) DEFAULT NULL,
    imp bigint(20) DEFAULT NULL,
    clk int(11) DEFAULT NULL,
    rtb_cost decimal(10,4) DEFAULT NULL COMMENT '支出 rtb_succ_price',
    bid_cost decimal(10,4) DEFAULT NULL COMMENT '收入',
    profit decimal(10,4) DEFAULT NULL COMMENT '毛利',
    order_num int(11) DEFAULT NULL,
    order_price decimal(10,4) DEFAULT NULL,
    arrival_num int(11) DEFAULT NULL,
    pv int(11) DEFAULT NULL,
    pv_duration int(11) DEFAULT NULL,
    two_jump_num int(11) DEFAULT NULL,
    reg_num int(11) DEFAULT NULL,
    stop_time int(11) DEFAULT NULL,
    jump_num int(11) DEFAULT NULL,
    uv int(11) DEFAULT NULL,
    shop_cart int(11) DEFAULT NULL,
    shop_cart_price decimal(10,4) DEFAULT NULL,
    invalid_clk int(11) DEFAULT NULL COMMENT '无效点击量',
    rtb_price decimal(10,4) unsigned DEFAULT NULL COMMENT '竞价出价',
    active_num int(10) DEFAULT NULL,
    -- create indexes
    INDEX (rep_date) ,
    index (channel_id) ,
    index (project_id) ,
    index (campaign_id) ,
    index (creative_id) ,
    INDEX (region_code)    );
        " """
    return command(mysql_sql)


def data_import(date):
    hive_sql = """ /data/hadoop/hive-1.1.0-cdh5.5.0/bin/hive -e "
        select from_unixtime(unix_timestamp(day_id,'yyyyMMdd'),'yyyy-MM-dd') as rep_date, 
        case when xv_bid_l3_1.channel_id>2000 then 1 else 0 end as trade_type,
        xv_bid_l3_1.channel_id ,xv_bid_l3_1.project_id ,xv_bid_l3_1.campaign_id , campaign.bidding_client_type ,creative_id ,is_rd ,region_code ,domain ,adslot_id ,
        bid ,imp ,clk ,rtb_cost ,bid_cost ,profit ,order_num ,order_price ,arrival_num ,pv ,pv_duration ,two_jump_num ,reg_num ,stop_time ,
        jump_num ,uv ,shop_cart ,shop_cart_price ,invalid_clk ,rtb_price, active_num
        
        from xview.xv_bid_l3_1
        join xview.channel on xv_bid_l3_1.channel_id=channel.id
        join xview.campaign on xv_bid_l3_1.project_id=campaign.project_id and xv_bid_l3_1.campaign_id=campaign.campaign_id
        where day_id='"""+ date +"""';
    " > /data/xview/bid_statistics/day_xv_bid_l3_1"""
    return command(hive_sql)

def load_mysql(date):
    mysql_sql = """ mysql -h 192.168.4.235 -udmpapadmin -p'dc077e28' -D xview -e "
DELETE from xv_bid_l3_1_""" + date + """ where DATE_FORMAT(rep_date,'%Y%m%d')='"""+ date +"""';
LOAD DATA LOCAL INFILE '/data/xview/bid_statistics/day_xv_bid_l3_1' INTO TABLE xv_bid_l3_1_""" + date + """( 
rep_date, trade_type, channel_id, project_id, campaign_id, flow_type, creative_id, is_rd, region_code, domain, adslot_id, 
bid, imp, clk, rtb_cost, bid_cost, profit, order_num, order_price, arrival_num, pv, pv_duration, two_jump_num, reg_num, stop_time, 
jump_num, uv, shop_cart, shop_cart_price, invalid_clk, rtb_price,active_num) ;
    " """
    return command(mysql_sql)



# %Y%m%d %Y-%m-%d %Y%m 
def getDateFormat(formatStr, day):
    return (datetime.datetime.now() - datetime.timedelta(days=day)).strftime(formatStr)

def mailto(date,pwd, jobname, maillist, msg):
    cmd = """ echo "nohup """ + pwd + sys.argv[0]+ date +""" &\n """ + msg +""" " | mail -s "Job --""" + jobname + """-- fail" """ + maillist
    print cmd
    command(cmd);
    
if __name__ == '__main__':
    pwd = """/data/xview/bid_statistics/"""
    jobname = 'new hadoop clusters\'s job ' + pwd + sys.argv[0]
    to = """wangchenchen@emar.com"""
    
    date = getDateFormat('%Y%m%d', 1)
    month = getDateFormat('%Y%m', 1)
    begin=time.time()


    if(len(sys.argv) == 2):
        date = sys.argv[1]
        month = date[0:6]
    

    r=create_table(date)
    if r!= 0:
        msg = jobname + ' . create_table tried 3 times all failed'
        print msg
        mailto(date, pwd, jobname, to, msg)
        sys.exit(1)

    r=data_import(date)
    if r!= 0:
        msg = jobname + ' . data_import tried 3 times all failed'
        print msg
        mailto(date, pwd, jobname, to, msg)
        sys.exit(1)

    r=load_mysql(date)
    alltime=time.time()-begin
    print "LogTime ",time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time())), ": Finish ",sys.argv[0]," Job Cost time:" ,round(alltime/60,0),'m',round(alltime%60,0),'s'
    
    if r!= 0:
        msg = jobname + ' . load_mysql tried 3 times all failed'
        print msg
        mailto(date, pwd, jobname, to, msg)
        sys.exit(1)


