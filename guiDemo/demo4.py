import tkinter


def go():
    print(entry1.get())  # 获取文本框的内容


win = tkinter.Tk()
button = tkinter.Button(win, text="有种点我", command=go)  # 收到消息执行这个函数
button.pack()  # 加载到窗体，
entry1 = tkinter.Entry(win, width=50, bg="red", fg="black")
# entry1=tkinter.Entry(win,show="*",width=50,bg="red",fg="black")
entry1.pack()
win.mainloop()


