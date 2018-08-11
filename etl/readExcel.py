

import os

def read_excel(file):
    ft = file.split(".")[-1]

    # if ft=='xlsx':
    #     # from openpyxl import load_workbook
    #     # wookbook = load_workbook(filename=file, read_only=True)
    #     # print(file,wookbook.sheetnames)
    #     # print(file)
    #     print()
    # el
    if ft=='xls':
        import xlrd
        wookbook = xlrd.open_workbook(file)
        print(file, wookbook.sheet_names())

        import pandas as pd
        excel = pd.read_excel(file,header=None)
        print((excel[:1]))
        print(excel[:1])
    # else:
    #     print(ft,'this file is not an excel.' ,file)



p1='E:\精品班学员信息采集'
os.chdir(p1)
file_list=os.listdir(p1)
type_count={}
for file in file_list:
    ft = file.split(".")[-1]
    if ft in type_count:
        type_count[ft] = type_count[ft] + 1
    else:
        type_count[ft] = 1

    read_excel(file)


print(type_count)


# file1='C:/Users/Light/Downloads/2018年5月发货.xlsx'
# import pandas as pd
# excel = pd.read_excel(file1)
# print(excel.head(2))

# import xlrd
# workbook = xlrd.open_workbook(r'F:\demo.xlsx')

# from openpyxl import load_workbook
# file="/Users/admin/Documents/工作文件夹/项目/财务销售分摊/201805/2018年5月发货.xlsx"
# wb = load_workbook(filename=file, read_only=True)
# print( wb.sheetnames )

