'''
Description: 
Author: Huang Wen
Date: 2022-04-12 15:37:13
LastEditTime: 2022-04-24 16:13:00
LastEditors: Huang Wen
'''
from tkinter import *


# 注册界面类
class RegisterPanel:

    def __init__(self, quit_func, reg_func, close_callback):
        print("初始化登陆界面类")
        self.reg_frame = None
        self.btn_reg = None
        self.btn_quit = None
        self.user = None
        self.key = None
        self.confirm = None
        self.quit_func = quit_func
        self.reg_func = reg_func
        self.close_callback = close_callback

    def show(self):
        self.reg_frame = Tk()
        self.reg_frame.configure(background="#333333")
        # 设置窗口关闭按钮回调，用于退出时关闭socket连接
        self.reg_frame.protocol("WM_DELETE_WINDOW", self.close_callback)
        screen_width = self.reg_frame.winfo_screenwidth()
        screen_height = self.reg_frame.winfo_screenheight()
        width = 400
        height = 360
        gm_str = "%dx%d+%d+%d" % (width, height, (screen_width - width) / 2,
                                  (screen_height - 1.2 * height) / 2)
        self.reg_frame.geometry(gm_str)
        self.reg_frame.title("注册")
        self.reg_frame.resizable(width=False, height=False)

        title_lable = Label(self.reg_frame, text="python聊天室 - 注册", font=("黑体", 16),
                            fg="white", bg="#555555")
        title_lable.pack(ipady=10, fill=X)

        # 注册表单frame
        form_frame = Frame(self.reg_frame, bg="#333333")
        user_img = PhotoImage(file="image\\user.png", master=self.reg_frame)
        key_img = PhotoImage(file="image\\key.png", master=self.reg_frame)
        confirm_img = PhotoImage(file="image\\key.png", master=self.reg_frame)
        user_img_label = Label(form_frame, image=user_img, width=30, height=30, bg="#333333")
        key_img_label = Label(form_frame, image=key_img, width=30, height=30, bg="#333333")
        confirm_img_label = Label(form_frame, image=confirm_img, width=30, height=30, bg="#333333")
        user_img_label.grid(row=0, column=0, padx=5)
        key_img_label.grid(row=1, column=0, padx=5)
        confirm_img_label.grid(row=2, column=0, padx=5)
        Label(form_frame, text="用户名：", font=("宋体", 12), bg="#333333", fg="white") \
            .grid(row=0, column=1, pady=20)
        Label(form_frame, text="密  码：", font=("宋体", 12), bg="#333333", fg="white") \
            .grid(row=1, column=1, pady=20)
        Label(form_frame, text="确认密码：", font=("宋体", 12), bg="#333333", fg="white") \
            .grid(row=2, column=1, pady=20)
        self.user = StringVar()
        self.key = StringVar()
        self.confirm = StringVar()
        Entry(form_frame, textvariable=self.user, bg="#e3e3e3", width=30) \
            .grid(row=0, column=2, ipady=1)
        Entry(form_frame, textvariable=self.key, show="*", bg="#e3e3e3", width=30) \
            .grid(row=1, column=2, ipady=1)
        Entry(form_frame, textvariable=self.confirm, show="*", bg="#e3e3e3", width=30) \
            .grid(row=2, column=2, ipady=1)
        form_frame.pack(fill=X, padx=20, pady=10)
        # 按钮frame
        btn_frame = Frame(self.reg_frame, bg="#333333")
        self.btn_quit = Button(btn_frame, text="取消", bg="lightgreen", fg="black", width=15,
                               font=('黑体', 11), command=self.quit_func).pack(side=LEFT, ipady=3)
        self.btn_reg = Button(btn_frame, text="注册", bg="lightblue", fg="black", width=15,
                              font=('黑体', 11), command=self.reg_func).pack(side=RIGHT, ipady=3)
        btn_frame.pack(fill=X, padx=20, pady=20)
        self.reg_frame.mainloop()

    def close(self):
        if self.reg_frame == None:
            print("未显示界面")
        else:
            self.reg_frame.destroy()

    # 获取输入的用户名、密码、确认密码
    def get_input(self):
        return self.user.get(), self.key.get(), self.confirm.get()
