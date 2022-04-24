'''
Description: 
Author: Huang Wen
Date: 2022-04-12 15:37:13
LastEditTime: 2022-04-24 16:12:51
LastEditors: Huang Wen
'''
# -*- coding:utf-8 -*-
import time
import tkinter
from tkinter import *
from tkinter import messagebox
from databaseTool import MySQLTool


db=MySQLTool()
# 主界面类
class MainPanel:
    # 四个按钮, 使用全局变量, 方便创建和销毁
    b1, b2, b3, b4 = None, None, None, None
    # 将图片打开存入变量中
    p1,p2,p3,p4 = None, None, None, None
    # 用字典将标记与表情图片一一对应, 用于后面接收标记判断表情贴图
    dic = None
    ee = 0  # 判断表情面板开关的标志
    
    def __init__(self, username, send_func, close_callback, client):
        print("初始化主界面")
        self.username = username
        self.friend_list = None
        self.message_text = None
        self.send_text = None
        self.send_func = send_func
        self.close_callback = close_callback
        self.main_frame = None
        self.client = client


    def show(self):
        global main_frame,ee,b1,b2,b3,b4,ii,listbox1
        main_frame = Tk()
        main_frame.title("python聊天室")
        main_frame.configure(background="#333333")
        # 设置窗口关闭按钮回调，用于退出时关闭socket连接
        main_frame.protocol("WM_DELETE_WINDOW", self.close_callback)
        width = 1000
        height = 700
        screen_width = main_frame.winfo_screenwidth()
        screen_height = main_frame.winfo_screenheight()
        gm_str = "%dx%d+%d+%d" % (width, height, (screen_width - width) / 2,
                                  (screen_height - 1.2 * height) / 2)
        main_frame.geometry(gm_str)
        # 设置最小尺寸
        main_frame.minsize(width, height)
        Label(main_frame, text="python聊天室欢迎您：" + self.username, font=("黑体", 13), bg="#333333",
              fg="white").grid(row=0, column=0, ipady=10, padx=10, columnspan=2, sticky=W)
        friend_list_var = StringVar()
        self.friend_list = Listbox(main_frame, selectmode=NO, listvariable=friend_list_var,
                                   bg="#444444", fg="white", font=("宋体", 14), highlightcolor="white")
        self.friend_list.grid(row=1, column=0, rowspan=3, sticky=N + S, padx=10, pady=(0, 5))
        main_frame.rowconfigure(1, weight=1)
        main_frame.columnconfigure(1, weight=1)
        sc_bar = Scrollbar(main_frame)
        sc_bar.grid(row=1, column=0, sticky=N + S + E, rowspan=3, pady=(0, 5))
        sc_bar['command'] = self.friend_list.yview
        self.friend_list['yscrollcommand'] = sc_bar.set
        msg_sc_bar = Scrollbar(main_frame)
        msg_sc_bar.grid(row=1, column=1, sticky=E + N + S, padx=(0, 10))
        self.message_text = Text(main_frame, bg="white", height=1,
                                 highlightcolor="white", highlightthickness=1)
        # 显示消息的文本框不可编辑，当需要修改内容时再修改版为可以编辑模式 NORMAL
        self.message_text.config(state=DISABLED)
        self.message_text.tag_configure('greencolor', foreground='green')
        self.message_text.tag_configure('bluecolor', foreground='blue')
        self.message_text.grid(row=1, column=1, sticky=W + E + N + S, padx=(10, 30))
        msg_sc_bar["command"] = self.message_text.yview
        self.message_text["yscrollcommand"] = msg_sc_bar.set
        send_sc_bar = Scrollbar(main_frame)
        send_sc_bar.grid(row=2, column=1, sticky=E + N + S, padx=(0, 10), pady=10)
        self.send_text = Text(main_frame, bg="white", height=11, highlightcolor="white",
                              highlightbackground="#444444", highlightthickness=3)
        self.send_text.see(END)
        self.send_text.grid(row=2, column=1, sticky=W + E + N + S, padx=(10, 30), pady=10)
        send_sc_bar["command"] = self.send_text.yview
        self.send_text["yscrollcommand"] = send_sc_bar.set
        Button(main_frame, text="发送", bg="blue", font=("宋体", 14), fg="white", command=self.send_func) \
            .grid(row=3, column=1, pady=5, padx=10, sticky=W, ipady=3, ipadx=10)
        Button(main_frame, text="清空", bg="red", font=("宋体", 14), fg="white", command=self.clear_send_text) \
            .grid(row=3, column=1, pady=5, sticky=W, padx=(110, 0), ipady=3, ipadx=10)
        
        global b1,b2,b3,b4,p1,p2,p3,p4,dic,ee
        ee = 0
        # 将图片打开存入变量中
        p1 = tkinter.PhotoImage(file='./emoji/facepalm.png')
        p2 = tkinter.PhotoImage(file='./emoji/smirk.png')
        p3 = tkinter.PhotoImage(file='./emoji/concerned.png')
        p4 = tkinter.PhotoImage(file='./emoji/smart.png')
        dic = {'aa**': p1, 'bb**': p2, 'cc**': p3, 'dd**': p4}
        # 发送表情图标记的函数, 在按钮点击事件中调用

        def mark(mes):  # 参数是发的表情图标记, 发送后将按钮销毁
            global ee,b1
            #发送给服务器
            self.client.send_message(mes)
            b1.destroy()
            b2.destroy()
            b3.destroy()
            b4.destroy()
            ee = 0

        # 四个对应的函数
        def bb1():
            mark('aa**')


        def bb2():
            mark('bb**')


        def bb3():
            mark('cc**')


        def bb4():
            mark('dd**')
    
    
        def express():
            global b1, b2, b3, b4, ee
            if ee == 0:
                ee = 1  # 表情面板开关的标志，=1表示已经打开了
                b1 = tkinter.Button(main_frame, command=bb1, image=p1, relief=tkinter.FLAT, bd=0)
                b2 = tkinter.Button(main_frame, command=bb2, image=p2, relief=tkinter.FLAT, bd=0)
                b3 = tkinter.Button(main_frame, command=bb3, image=p3, relief=tkinter.FLAT, bd=0)
                b4 = tkinter.Button(main_frame, command=bb4, image=p4, relief=tkinter.FLAT, bd=0)

                b1.place(x=400, y=583)
                b2.place(x=470, y=583)
                b3.place(x=540, y=583)
                b4.place(x=610, y=583)
            else:
                ee = 0
                b1.destroy()
                b2.destroy()
                b3.destroy()
                b4.destroy()
                
                
        # 创建表情按钮
        Button(main_frame, text="表情", bg="green", font=("宋体", 14), fg="white", command=express) \
            .grid(row=3, column=1, pady=5, padx=(220,0), sticky=W, ipady=3, ipadx=10)
            
        # 查看在线用户按钮
        button1 = tkinter.Button(main_frame, text='同步消息记录', command=self.sync_msg)
        button1.place(x=900, y=480, width=90, height=30)
        self.main_frame = main_frame
        main_frame.mainloop()

    # 刷新在线列表
    def refresh_friends(self, names):
        self.friend_list.delete(0, END)
        for name in names:
            self.friend_list.insert(0, name)

    # 接受到消息，在文本框中显示，自己的消息用绿色，别人的消息用蓝色
    def recv_message(self, user, content):
        try:
            self.message_text.config(state=NORMAL)
            global dic
            if content[:6]=='@robot': #判断是否为机器人发出的消息
                msg_user=content.split('@@')[0]
                msg_robot=content.split('@@')[1]
                # 插入用户发送的消息
                title = user + " " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n"
                if user == self.username:
                    self.message_text.insert(END, title, 'greencolor')
                else:
                    self.message_text.insert(END, title, 'bluecolor')
                self.message_text.insert(END, msg_user + "\n")
                    
                # 插入机器人回复的内容
                title_robot = 'robot' + " " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n"
                self.message_text.insert(END, title_robot, 'bluecolor')
                self.message_text.insert(END, msg_robot + "\n")
            # 判断消息是否应该显示（只显示全部、或@我的以及机器人发出的消息）
            elif (content.split(' ')[0]=='@'+self.username) or content[0]!='@'\
                or user==self.username or content.split(' ')[0]=='@robot':
                title = user + " " + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n"
                if user == self.username:
                    self.message_text.insert(END, title, 'greencolor')
                else:
                    self.message_text.insert(END, title, 'bluecolor')
                # 判断是否为表情
                if content in dic:
                    self.message_text.image_create(tkinter.END, image=dic[content])
                    self.message_text.insert(END, "\n")
                else:
                    self.message_text.insert(END, content + "\n")
                self.message_text.config(state=DISABLED)
            # 滚动到最底部
            self.message_text.see(END)
        except Exception as e:
            print('接收方发送错误：'+str(e))



    # 清空消息输入框
    def clear_send_text(self):
        self.send_text.delete('0.0', END)

    # 获取消息输入框内容
    def get_send_text(self):
        return self.send_text.get('0.0', END)

    # 同步数据库中的消息记录
    def sync_msg(self):
        self.message_text.config(state=NORMAL)
        # 清空面板内所有内容
        self.message_text.delete(1.0, "end")
        # 同步数据库中的所有数据
        db_messages=db.sync_messages()
        if db_messages==False:
            messagebox.showerror("同步失败", "数据中无任何消息记录\n或在同步过程中出现错误")
        else:
            for message in db_messages:
                # 判断消息是否应该显示给当前用户
                if (message['content'].split(' ')[0]=='@'+self.username) or message['content'][0]!='@' \
                    or message['mid']==self.username or message['content'].split(' ')[0]=='@robot':
                    if '@@' in message['content']: # 判断是否调用了机器人
                        msg_user_syn=message['content'].split('@@')[0]
                        msg_robot_syn=message['content'].split('@@')[1]
                        title_user = message['mid'] + " " + message['time'] + "\n"
                        # 插入用户的消息
                        if message['mid'] == self.username:
                            self.message_text.insert(END, title_user, 'greencolor')
                        else:
                            self.message_text.insert(END, title_user, 'bluecolor')
                        self.message_text.insert(END, msg_user_syn + "\n")
                        # 插入机器人回复的内容
                        self.message_text.insert(END, 'robot' + " " + message['time'] + "\n", 'bluecolor')
                        self.message_text.insert(END, msg_robot_syn + "\n")
                    else:
                        title = message['mid'] + " " + message['time'] + "\n"
                        if message['mid'] == self.username:
                            self.message_text.insert(END, title, 'greencolor')
                        else:
                            self.message_text.insert(END, title, 'bluecolor')
                        if message['content'] in dic:   # 判断是否为表情包
                            self.message_text.image_create(tkinter.END, image=dic[message['content']])
                            self.message_text.insert(END, "\n")
                        else:
                            self.message_text.insert(END, message['content'] + "\n")
        # 滚动到最底部
        self.message_text.see(END)
        self.message_text.config(state=DISABLED)
