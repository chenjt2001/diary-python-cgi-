#!/usr/bin/python3
# 用于接受写入日记本的内容并写入数据库

import cgi 
import codecs
import sys
import os
import pymysql
import traceback
import cgitb
from config import *

# 用于连接并写入数据库
def write(title, content, ip):
	db = pymysql.connect(host=mysql.host,user=mysql.user, password=mysql.password, port=mysql.port, db=mysql.database)
	cursor = db.cursor()

	sql = "INSERT INTO %s(title, content, ip) VALUES ('%s', '%s', '%s')" % (mysql.table, title, content, ip)# SQL 插入语句
	
	try:
		# 执行sql语句
		cursor.execute(sql)
		db.commit()
		db.close()# 关闭数据库连接

	except Exception as e:
		# 发生错误时回滚
		db.rollback()
		db.close()# 关闭数据库连接
		raise e

cgitb.enable(logdir=logdir)# 捕获错误日志
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

# 创建 FieldStorage的实例
form = cgi.FieldStorage()

# 接收字段数据
title = form.getvalue('title')
content = form.getvalue('content')

print('Content-type:text/html')
print()
print('<html>')
print('<head>')
print('<meta charset="utf-8">')
print('<title>珒陶的日记本 - 提示</title>')
print('</head>')
print('<body>')

if title != None and content != None:
	ip = os.environ['REMOTE_ADDR']# 获取客户机的IP地址
	write(title, content, ip)# 连接并写入数据库
	print('写入成功！')

else:
	print('写入失败！标题或内容不能为空。')

print('</body>')
print('</html>')