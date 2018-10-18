# coding: utf-8

import tkinter as tk
from tkinter import filedialog
from guiDemo.loadexcel2odps import uploadexcel
from guiDemo.loadintoexcel import load2excel

GUI = tk.Tk()  # 创建父容器GUI
GUI.title("Serial Tool")  # 父容器标题
GUI.geometry("780x380")  # 设置父容器窗口初始大小,窗口会随着组件大小的变化而变化

input_file = output_file = sql_mode = ''
begin_date = end_date = ''


def xz():
    global input_file
    input_file = filedialog.askopenfilename()
    if input_file != '':
        lb1.config(text="输入的文件是：" + input_file)
    else:
        lb1.config(text="您没有选择任何文件")
    return input_file


frame1 = tk.Frame(GUI)
frame1.grid(row=0, column=0, sticky='w')
lb1 = tk.Label(frame1, text='请选择输入文件:')
# lb1.grid_location(1, 10)
lb1.pack(side='left')
btn1 = tk.Button(frame1, text="弹出选择文件对话框", command=xz)
btn1.pack(side='left')
print(input_file)


def bc():
    global output_file
    output_file = filedialog.asksaveasfilename()
    if output_file != '':
        lb2.config(text="输出的文件是：" + output_file)
    else:
        lb2.config(text="您没有选择任何文件")
    return output_file


frame2 = tk.Frame(GUI)
frame2.grid(row=2, column=0, sticky='w')

lb2 = tk.Label(frame2, text='请选择输出文件:')
lb2.pack(side='left')
btn2 = tk.Button(frame2, text="弹出选择文件对话框", command=bc)
btn2.pack(side='left')
print(output_file)


# def go(*args):  # 处理事件，*args表示可变参数
#     global sql_mode
#     sql_mode = comboxlist.get()
#     print(sql_mode)  # 打印选中的值
#     return sql_mode
#

# frame3 = tk.Frame(GUI)
# frame3.grid(row=3, column=0, sticky='w')
#
# lb3 = tk.Label(frame3, text='请选模式和时间:')
# lb3.pack(side='left')
# comboxlist = ttk.Combobox(frame3)  # 初始化
# comboxlist["values"] = ("1. 班长完课率", "2. 班级完课率", "3. 你最帅", "4. 你真菜")
# comboxlist.current(0)  # 选择第一个
# comboxlist.bind('<<ComboboxSelected>>', go)  # 绑定事件,(下拉列表框被选中时，绑定go()函数)
# # sql_mode = comboxlist.get()
# comboxlist.pack()

frame4 = tk.Frame(GUI)
frame4.grid(row=4, column=0, sticky='w')
lb4_1 = tk.Label(frame4, text='开始日期:')
lb4_1.pack(side='left')
var1 = tk.StringVar()  # 这即是输入框中的内容
var1.set('20180910')  # 通过var.get()/var.set() 来 获取/设置var的值
entry4_1 = tk.Entry(frame4, width=10, textvariable=var1)
entry4_1.pack(side='left')

lb4_2 = tk.Label(frame4, text='结束日期:')
lb4_2.pack(side='left')
var2 = tk.StringVar()  # 这即是输入框中的内容
var2.set('20181009')  # 通过var.get()/var.set() 来 获取/设置var的值
entry4_2 = tk.Entry(frame4, width=10, textvariable=var2)
entry4_2.pack(side='left')


def run_stat():
    lb5.config(text="正在执行...")

    print('sql select data.========')
    print(input_file)
    print(output_file)
    begin_date = entry4_1.get()
    end_date = entry4_2.get()
    print(begin_date, end_date)

    uploadexcel(input_file)
    load2excel(output_file,begin_date,end_date)
    lb5.config(text="运行结束,文件输出在:")
    var5 = tk.StringVar()  # 这即是输入框中的内容
    var5.set(output_file)  # 通过var.get()/var.set() 来 获取/设置var的值
    entry5_1 = tk.Entry(frame5, width=30, textvariable=var5)
    entry5_1.pack(side='left')

frame5 = tk.Frame(GUI)
frame5.grid(row=5, column=0, sticky='w')


btn5 = tk.Button(frame5, text="执行查询", command=run_stat)
btn5.pack(side='left')
lb5 = tk.Label(frame5, text='xx')
lb5.pack(side='left')
GUI.mainloop()


