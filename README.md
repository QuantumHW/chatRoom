# Python聊天室

> 该项目为计算机网络的课程作业——网络聊天室，涵盖了基本的socket网络编程、Tkinter图像化界面、MySQL数据库等技术，可实现表情包的发送、单用户私聊、机器人对话等功能

☑️用户密码采用MD5加密（可根据需要，灵活调整为其他加密方式）

☑️支持发送表情包

☑️支持消息记录同步（从数据库中读取历史消息）

☑️支持单用户私聊（通过@实现，eg：@test 这是一条私聊消息）

☑️支持与智能机器人聊天（同样通过@实现，eg：@robot 你好）



## 1.项目结构

chatRoom             
├─ emoji &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//存放表情包的文件夹  
│  ├─ concerned.png  
│  ├─ facepalm.png   
│  ├─ smart.png      
│  └─ smirk.png      
├─ image &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//可视化界面中用到的图片  
│  ├─ key.png        
│  └─ user.png       
├─ res               
│  ├─ screenshot &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//屏幕截图  
│  │  ├─ 登录界面.png    
│  │  └─ 聊天界面.png    
│  └─ chat.sql &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//配套SQL脚本  
├─ Client.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//客户端类  
├─ databaseTool.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//数据库操作类  
├─ LoginPanel.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//可视化登录界面类  
├─ Main.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//用户主类  
├─ MainPanel.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//可视化主界面类  
├─ MD5.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//MD5加密工具  
├─ README.md  
├─ RegisterPanel.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//可视化注册类  
└─ Server.py &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;//服务端脚本   



## 2.环境依赖

Python 3.9.7  
MySQL 8.0.28  
PyMySQL==1.0.2  
requests==2.26.0  



## 3.构建流程

- #### 搭建数据库

```
运行前，请先自行创建一个名为chat的MySQL数据库，然后运行配套的SQL脚本（./res/chat.sql），以创建数据表、恢复样例数据
```

- #### 配置数据库


```
修改databaseTool.py文件中有关数据库的配置（用户名和密码修改为自己的）
```

- #### 配置机器人robot的apikey（跳过则无法使用机器人相关的聊天服务）

```
为了增加聊天室的可玩性，本项目调用了图灵机器人的api，由于调用次数有限制，请先将Client.py中send_message()函数里apiKey修改为自己的机器人（若需要获取自己的apiKey，请前往[图灵机器人](http://www.turingapi.com/)的官网进行注册，也可参考相关教程接入其他机器人）
```

- #### 启动服务器

```
在服务器上运行Server.py，服务器开始监听端口，并准备处理消息（也可在本地测试）
```

- #### 运行客户端

```
在用户端运行Main.py（在本地测试时，可运行多个Main.py，达到模拟多用户的效果）
```



## 4.运行截图

![](https://github.com/QuantumHW/chatRoom/blob/master/res/screenshot/%E7%99%BB%E5%BD%95%E7%95%8C%E9%9D%A2.png)

![](https://github.com/QuantumHW/chatRoom/blob/master/res/screenshot/%E8%81%8A%E5%A4%A9%E7%95%8C%E9%9D%A2.png)

