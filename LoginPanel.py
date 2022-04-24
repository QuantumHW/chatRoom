'''
Description: 
Author: Huang Wen
Date: 2022-04-12 15:37:13
LastEditTime: 2022-04-24 16:12:46
LastEditors: Huang Wen
'''
from tkinter import *


# 登陆界面类
class LoginPanel:

    def __init__(self, login_func, reg_func, close_callback):
        print("初始化登陆界面类")
        self.login_frame = None
        self.btn_reg = None
        self.btn_login = None
        self.user = None
        self.key = None
        self.login_func = login_func
        self.reg_func = reg_func
        self.close_callback = close_callback

    def show(self):
        self.login_frame = Tk()
        self.login_frame.configure(background="#333333")
        # 设置窗口关闭按钮回调，用于退出时关闭socket连接
        self.login_frame.protocol("WM_DELETE_WINDOW", self.close_callback)
        screen_width = self.login_frame.winfo_screenwidth()
        screen_height = self.login_frame.winfo_screenheight()
        width = 400
        height = 300
        gm_str = "%dx%d+%d+%d" % (width, height, (screen_width - width) / 2,
                                  (screen_height - 1.2 * height) / 2)
        self.login_frame.geometry(gm_str)
        self.login_frame.title("登录")
        self.login_frame.resizable(width=False, height=False)

        title_lable = Label(self.login_frame, text="python聊天室 - 登录", font=("黑体", 16),
                            fg="white", bg="#555555")
        title_lable.pack(ipady=10, fill=X)

        # 登录表单frame
        form_frame = Frame(self.login_frame, bg="#333333")
        user_img = PhotoImage(file="image\\user.png", master=self.login_frame)
        key_img = PhotoImage(file="image\\key.png", master=self.login_frame)
        user_img_label = Label(form_frame, image=user_img, width=30, height=30, bg="#333333")
        key_img_label = Label(form_frame, image=key_img, width=30, height=30, bg="#333333")
        user_img_label.grid(row=0, column=0, padx=5)
        key_img_label.grid(row=1, column=0, padx=5)
        Label(form_frame, text="用户名：", font=("宋体", 12), bg="#333333", fg="white") \
            .grid(row=0, column=1, pady=20)
        Label(form_frame, text="密  码：", font=("宋体", 12), bg="#333333", fg="white") \
            .grid(row=1, column=1, pady=20)
        self.user = StringVar()
        self.key = StringVar()
        Entry(form_frame, textvariable=self.user, bg="#e3e3e3", width=30) \
            .grid(row=0, column=2, ipady=1)
        Entry(form_frame, textvariable=self.key, show="*", bg="#e3e3e3", width=30) \
            .grid(row=1, column=2, ipady=1)
        form_frame.pack(fill=X, padx=20, pady=10)
        # 按钮
        btn_frame = Frame(self.login_frame, bg="#333333")
        self.btn_reg = Button(btn_frame, text="注册", bg="lightgreen", fg="black", width=15,
                              font=('黑体', 11), command=self.reg_func).pack(side=LEFT, ipady=3)
        self.btn_login = Button(btn_frame, text="登录", bg="lightblue", fg="black", width=15,
                                font=('黑体', 11), command=self.login_func).pack(side=RIGHT, ipady=3)
        btn_frame.pack(fill=X, padx=20, pady=20)
        self.login_frame.mainloop()
        # Thread(target=self.login_frame.mainloop).start()

    def close(self):
        if self.login_frame == None:
            print("未显示界面")
        else:
            self.login_frame.destroy()

    # 获取输入的用户名密码
    def get_input(self):
        return self.user.get(), self.key.get()
