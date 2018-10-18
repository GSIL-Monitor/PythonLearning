# -*- coding: utf-8 -*-
import datetime

import openpyxl
from odps import ODPS, options
from odps.tunnel import TableTunnel

# from conf import ACCESS_KEY_ID, ACCESS_KEY_SECRET
ACCESS_KEY_ID='<ACCESS_KEY_ID>'
ACCESS_KEY_SECRET='<ACCESS_KEY_SECRET>'
PROJECT='<PROJECT>'

options.tunnel.string_as_binary	= True

def uploadexcel(input_file,output_table_n='defult'):
    odps =  ODPS(ACCESS_KEY_ID,
             ACCESS_KEY_SECRET,
             PROJECT,
             endpoint='http://service.odps.aliyun.com/api')

    project = odps.get_project()  # 取到默认项目
    print(project)
    ds = datetime.datetime.now().strftime('%Y%m%d')
    print(ds)

    wb = openpyxl.load_workbook(filename=input_file,read_only=True)
    ws = wb.active
    print(datetime.datetime.now())

    output_table = odps.get_table(output_table_n)
    if output_table.exist_partition('ds=' + ds):
        output_table.delete_partition('ds=' + ds)
    output_table.create_partition('ds=' + ds, if_not_exists=True)

    tunnel = TableTunnel(odps)
    upload_session = tunnel.create_upload_session(output_table.name, partition_spec='ds=' + ds)
    print('output into', output_table_n, 'partition ds=', ds, ':\n', output_table.schema)
    index=0
    with upload_session.open_record_writer(0) as writer:
        for row in ws.rows:
            records = output_table.new_record()
            i=0
            for cell in row:
                if cell is None:
                    records[i] = None
                else:
                    records[i] = str(cell.value).encode('utf-8', "replace")
                i=i+1
            writer.write(records)
            index=index+1
            if index % 1000 == 0:
                print(index)
    upload_session.commit(0)

    print('===========')
    print(datetime.datetime.now())
