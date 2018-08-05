# diary-python-cgi-
A diary used python cgi.

一个日记本项目。因为不会用PHP而又想建网站所以用python写了一下。
emmm...目前只使用windows10测试通过。

win10运行方法如下：
  1、安装python3。
  2、pip install pymysql。
  3、安装mysql.然后启动他...具体这里不写了。
  4、配置cgi-bin/config.py。把里面的mysql登录信息改成自己的，并修改错误文件存放目录。
  5、运行cgi-bin/init.py。
  6、运行HTTPServer.py。（里面有端口、日志文件之类的可以改一下）
  7、在浏览器输入http://localhost:8080/ 。
  8、开始写日记吧。
  9、提交后，日记会被记录在mysql数据库里。
