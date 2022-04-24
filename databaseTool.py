'''
Description: 
Author: Huang Wen
Date: 2022-04-17 22:34:44
LastEditTime: 2022-04-24 16:12:20
LastEditors: Huang Wen
'''
import pymysql

class MySQLTool():
    # 打开数据库连接
    def __init__(self):
        self.conn = pymysql.connect(
            host = "127.0.0.1",
            port = 3306,
            user = "root",
            passwd = "####", # 修改为自己的数据库密码
            db = "chat", # 连接chat数据库
            charset = "utf8")


    def register_account(self, uid, password):
        '''注册账号
        :param uid: 待注册账号
        :param password: 待注册密码
        :return 0: '用户名存在'
        :return 1: '其他错误'
        :return 2: '添加用户成功'
        '''
        cursor = self.conn.cursor() # 获取游标
        try:
            SQL="INSERT INTO users(uid, password) VALUES ('%s', '%s')" % (uid, password)
            cursor.execute(SQL) # 执行SQL语句
            cursor.close()  # 关闭游标
            self.conn.commit() # 提交事务
            return "0"
        except pymysql.Error as e:
            if e.args[0]==1062:
                print('账户已存在,不允许重复注册')
                return "1"
            else:
                return "2"


    def login_verify(self, uid_input, password_input):
        '''登录验证
        :param uid_input: 用户输入的账号
        :param password_input: 用户输入的密码
        :return True: 登录成功
        :return False: 登录失败(账号密码输入有误或数据库出错)
        '''
        cursor = self.conn.cursor()
        try:
            SQL="SELECT * FROM users WHERE uid = '%s' AND password = '%s'" % (uid_input, password_input)
            cursor.execute(SQL)
            res = cursor.fetchone()  # 查询单条记录（由于用户ID唯一，所以没必要遍历整张表）
            cursor.close()
            self.conn.commit()
            if res==None:
                print('你输入的账号或密码有误')
                return False
            return True
        except pymysql.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
            return False
            
            
    def msg2database(self, mid_input, time_input, content_input):
        '''将消息存入数据库
        :param mid_input: 消息所属用户
        :param time_input: 消息发出时间
        :param content_input: 消息具体内容
        :return True: 成功存入数据库
        :return False: 数据库出错
        '''
        # 注：若需要对数据库自增主键id的起始值进行修改，可执行SQL语句 ALTER TABLE messages AUTO_INCREMENT= 1
        cursor = self.conn.cursor()
        try:
            SQL="INSERT INTO messages(mid, time, content) VALUES ('%s', '%s', '%s')" % (mid_input, time_input, content_input)
            cursor.execute(SQL)
            cursor.close()
            self.conn.commit()
            return True
        except pymysql.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
            return False
            
            

    def sync_messages(self):
        '''同步数据库中的消息
        :return return_value: 从数据库中返回的值
        :return False: 数据库中无任何消息记录或数据库出错
        '''
        return_value= []
        message={
            'mid':'',
            'time':'',
            'content':'',
        }
        cursor = self.conn.cursor()
        try:
            SQL="SELECT * FROM messages" 
            cursor.execute(SQL)
            res = cursor.fetchall()  # 返回所有消息记录
            cursor.close()
            self.conn.commit()
            if res==():
                print('数据库中暂无记录')
                return False
            else:
                for i in res:
                    message=message.copy()
                    message['mid']=i[1]
                    message['time']=i[2]
                    message['content']=i[3]
                    return_value.append(message)
            return return_value
        except pymysql.Error as e:
            print("Mysql Error %d: %s" % (e.args[0], e.args[1]))
            return False
    
    # 关闭连接
    def conn_close(self):
        self.conn.close()