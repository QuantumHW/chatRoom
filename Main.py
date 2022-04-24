'''
Description: 
Author: Huang Wen
Date: 2022-04-12 15:37:13
LastEditTime: 2022-04-24 16:12:25
LastEditors: Huang Wen
'''
# -*- coding:utf-8 -*-
from LoginPanel import LoginPanel
from MainPanel import MainPanel
from RegisterPanel import RegisterPanel
from Client import ChatClient
import MD5
from tkinter import messagebox
from threading import Thread
import time


def send_message():
    print("send message:")
    #获取输入框输入的内容
    content = main_frame.get_send_text()
    if content == "" or content == "\n":
        print("空消息，拒绝发送")
        return
    print(content)
    # 清空输入框
    main_frame.clear_send_text()
    client.send_message(content)


def close_sk():
    print("尝试断开socket连接")
    client.sk.close()


def close_main_window():
    close_sk()
    main_frame.main_frame.destroy()


def close_login_window():
    close_sk()
    login_frame.login_frame.destroy()


# 关闭注册界面并打开登陆界面
def close_reg_window():
    reg_frame.close()
    #登录界面
    global login_frame
    login_frame = LoginPanel(login, register, close_login_window)
    login_frame.show()


# 关闭登陆界面前往主界面
def goto_main_frame(user):
    login_frame.close()
    global main_frame
    # 从MainPanel.py模块中调用
    main_frame = MainPanel(user, send_message, close_main_window, client)
    # 新开一个线程专门负责接收并处理数据
    Thread(target=recv_data).start()
    main_frame.show()

# 登陆时需要进行的验证
def login():
    user, key = login_frame.get_input()
    # 密码传md5,加密
    key = MD5.gen_md5(key)
    if user == "" or key == "":
        messagebox.showwarning(title="提示", message="用户名或者密码为空")
        return
    print("user: " + user + ", key: " + key)
    #验证密码是否正确
    if client.check_user(user, key):
        # 验证成功
        goto_main_frame(user)
    else:
        # 验证失败
        messagebox.showerror(title="错误", message="用户名或者密码错误")


# 登陆界面->注册界面
def register():
    login_frame.close()
    global reg_frame
    reg_frame = RegisterPanel(close_reg_window, register_submit, close_reg_window)
    reg_frame.show()


# 提交注册表单
def register_submit():
    user, key, confirm = reg_frame.get_input()
    if user == "" or key == "" or confirm == "":
        messagebox.showwarning("错误", "请完成注册表单")
        return
    if not key == confirm:
        messagebox.showwarning("错误", "两次密码输入不一致")
        return
    # 发送注册请求
    result = client.register_user(user, MD5.gen_md5(key))
    if result == "0":
        # 注册成功，跳往登陆界面
        messagebox.showinfo("成功", "注册成功")
        close_reg_window()
    elif result == "1":
        # 用户名重复
        messagebox.showerror("错误", "该用户名已被注册")
    elif result == "2":
        # 未知错误
        messagebox.showerror("错误", "发生未知错误")


# 处理消息接收的线程方法
def recv_data():
    # 暂停几秒，等主界面渲染完毕
    time.sleep(1)
    while True:
        try:
            # 首先获取数据类型
            _type = client.recv_all_string()
            print("recv type: " + _type)
            if _type == "#!onlinelist#!":
                print("获取在线列表数据")
                online_list = list()
                for _ in range(client.recv_number()):
                    #添加各个用户名
                    online_list.append(client.recv_all_string())
                    #显示在发送消息界面中
                main_frame.refresh_friends(online_list)
                #输出登录的用户名
                print(online_list)
            elif _type == "#!message#!":
                print("获取新消息")
                user = client.recv_all_string()
                print("user: " + user)
                content = client.recv_all_string()
                print("message: " + content)
                main_frame.recv_message(user, content)
        except Exception as e:
            print("接受服务器消息出错，消息接受子线程结束。" + str(e))
            break


def start():
    global client
    client = ChatClient()
    global login_frame
    login_frame = LoginPanel(login, register, close_login_window)
    login_frame.show()


if __name__ == "__main__":
    start()