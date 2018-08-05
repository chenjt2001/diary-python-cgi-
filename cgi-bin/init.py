#!/usr/bin/python3
import pymysql
from config import *

# 打开数据库连接
db = pymysql.connect(host=mysql.host,user=mysql.user, password=mysql.password, port=mysql.port, db=mysql.database)
 
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

#cursor.execute("""CREATE TABLE sd (
#datetime DATETIME default getdate(),
#timestamp TIMESTAMP,
#title VARCHAR(max) NOT NULL,
#content VARCHAR(max) NOT NULL,
#ip VARCHAR(15) NOT NULL,)""" )

cursor.execute("""
CREATE TABLE %s (
datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
title TEXT NOT NULL,
content TEXT NOT NULL,
ip VARCHAR(15) NOT NULL)
""" % (mysql.table))
 
# 关闭数据库连接
db.close()
