'''
Description: 
Author: Huang Wen
Date: 2022-04-12 15:37:13
LastEditTime: 2022-04-24 16:12:31
LastEditors: Huang Wen
'''
# -*- coding:utf-8 -*-
import math
import json
import socket
import requests

#客户端的定义
class ChatClient:
    def __init__(self):
        print("初始化tcp客户端")
        self.sk = socket.socket()
        # 客户端连接服务器
        self.sk.connect(('127.0.0.1', 12323))

    # 验证登录
    def check_user(self, user, key):
        self.sk.sendall(bytes("1", "utf-8"))
        # 依次发送用户名密码给服务器，send_string_with_length（）函数下面有定义，先发长度，后发内容
        #服务器server中有定义判断用户名密码是否正确的函数，将服务器结果发给客户端
        self.send_string_with_length(user)
        self.send_string_with_length(key)
        # 获取服务器的返回值，"1"代表通过，“0”代表不通过
        check_result = self.recv_string_by_length(1)
        #check_result=‘1’返回的是bool类型的值，如果=1-》True,否则是False
        return check_result == "1"

    # 注册，同样是客户端和服务器同时执行
    # 客户端将待注册的用户名和密码发送给服务器，服务器检测是否符合注册条件，将结果返回给客户端
    def register_user(self, user, key):
        # 请求类型
        self.sk.sendall(bytes("2", "utf-8"))
        # 依次发送用户名密码，同登录
        self.send_string_with_length(user)
        self.send_string_with_length(key)
        # 获取服务器的返回值，"0"代表通过，“1”代表已有用户名, "2"代表其他错误
        return self.recv_string_by_length(1)

    # 发送消息
    def send_message(self, message):
        if message[:6]=='@robot': # 检测是否调用机器人
            msg=message[6:]
            apiUrl = 'http://openapi.turingapi.com/openapi/api/v2'
            data = {
                "perception": {
                    "inputText": {
                        "text": msg
                    }
                },
                "userInfo": {
                    "apiKey": '####', # 修改为自己的apiKey
                    "userId": '0',
                }

            }
            data_json = json.dumps(data)
            robot_message='emmm...'  # robot默认回复内容
            try:
                response = requests.post(apiUrl, data=data_json)
                robot_res = json.loads(response.content)
                robot_message = robot_res["results"][0]['values']['text']
            except:
                robot_message='Robot Error'
            message=(message+'@@'+robot_message).replace('\n','')
            
        self.sk.sendall(bytes("3", "utf-8"))   
        self.send_string_with_length(message)
        
        

    ########################### 封装一些发送接受数据的方法 ##############################
    # 发送带长度的字符串
    def send_string_with_length(self, content):
        # 先发送内容的长度
        self.sk.sendall(bytes(content, encoding='utf-8').__len__().to_bytes(4, byteorder='big'))
        # 再发送内容
        self.sk.sendall(bytes(content, encoding='utf-8'))

    # 获取服务器传来的定长字符串
    def recv_string_by_length(self, len):
        #socket.recv()函数用于接收服务器发送回来的数据，定长字符串可直接接收
        return str(self.sk.recv(len), "utf-8")

    # 获取服务端传来的变长字符串，这种情况下服务器会先传一个长度值
    def recv_all_string(self):
        # 首先获取消息长度，根据消息长度再接收
        length = int.from_bytes(self.sk.recv(4), byteorder='big')
        b_size = 3 * 1024  # 注意utf8编码中汉字占3字节，英文占1字节
        #math.ceil()返回大于或等于给定整数的整数，他决定循环次数
        times = math.ceil(length / b_size)
        content = ''
        for i in range(times):
            #如果是最后一次接收，那么它的长度不一定等于b_size,可能小于，所以要单独讨论
            if i == times - 1:
                seg_b = self.sk.recv(length % b_size)
            else:
                seg_b = self.sk.recv(b_size)
            content += str(seg_b, encoding='utf-8')
        return content
    #发送数字
    def send_number(self, number):
        self.sk.sendall(int(number).to_bytes(4, byteorder='big'))
        #接收数字
    def recv_number(self):
        return int.from_bytes(self.sk.recv(4), byteorder='big')