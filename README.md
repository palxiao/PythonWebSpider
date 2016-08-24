# Python网络爬虫

语言环境：Python2.7 

需要BeautifulSoup4插件 推荐使用控制台pip安装(官方文档https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/)

运行爬虫入口开始爬取  output.html查看结果

简单py爬虫，修改入口及解析器改变规则

新增存入数据库操作  需要插件(MySql)

补充：（折腾一晚上，网上很多方法都试不通）
	mac下安装MySQL-python
	
	下载MySQLdb源码
	下面是1.2.5的版本
	https://pypi.python.org/packages/source/M/MySQL-python/MySQL-python-1.2.5.zip#md5=654f75b302db6ed8dc5a898c625e030c
	下载后解压，然后在终端cd到文件目录
	修改 site.cfg, 修改下面内容:
	由#mysql_config = /usr/local/bin/mysql_config
	改成mysql_config = /usr/local/mysql/bin/mysql_config
	否则会出现找不到 MySQL_config 的问题:

	然后修改 _mysql.c, 把第 37 到 39 行注释掉, 如下:
	//#ifndef uint//#define uint unsigned int//#endif(这一步我没做，不知何意)

	然后再用 python ./setup.py build 编译
	$ python ./setup.py build
	然后再用 python ./setup.py install 安装
	$ sudo python ./setup.py install
	
	安装完成后导包出现：Reason: image not found
	
	vi .bash_profile
	进入编辑状态，在最后添加
	export DYLD_LIBRARY_PATH="/usr/local/mysql/lib"
	esc退出编辑后执行以下命令
	:w 
	保存退出bash
