# coding=UTF-8
'''
Created on 2016年8月21日

@author: ShawnPhang
'''
import MySQLdb

class intoMysql(object):
    def __init__(self):
        self.conn = MySQLdb.connect(host = '127.0.0.1',user = 'root',passwd = 'root',port = 3306,db = 'test',charset="utf8")

    def collect_data(self , data):
        if data is None :
            return
        
        try :
            cursor = self.conn.cursor()
            #print u"标题：%s" %data["title"]
            #print u"内容：%s" %data["summary"]
            sql = "insert into spider(title , summary) values('%s','%s')"%(data["title"].encode("utf8"),data["summary"].encode("utf8"))
            cursor.execute(sql)
            self.conn.commit()
            
        except Exception as e :
            print e
            

