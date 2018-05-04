#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

import MySQLdb

class MySQL():
	"""MySQL初始化方法"""
	def __init__(self, host, port=3306, user, password, database):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.database = database

    """
		获取数据库连接对象
	"""
	def __getConnect(self):
		if not self.database:
			raise(NameError, "未指定需要连接的数据库名称")
		self.connection = MySQLdb.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, db=self.database, use_unicode=True, charset='utf8')
		cur = self.connection.cursor()
		if not cur:
			raise(NameError, "连接数据库失败")
		else:
			return cur

	"""
        执行非查询语句
        调用示例：
            ms = MySQL(host="localhost", port=3306, user="sa", password="123456", database="Demo")
            ms.executeUpdate("DELETE FROM T_USER")
    """
	def executeUpdate(self, sql):
		cur2 = self.__getConnect()
		cur2.execute(sql)
		self.connection.commit()
		cur2.close()
		self.connection.close()
	
	"""
    	执行查询语句
    	返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    	调用示例：
			ms = MySQL(host="localhost", port=3306, user="sa", password="123456", database="Demo")
			list = ms.executeQuery("SELECT uid, uname FROM T_USER")
			for (uid, uname) in list:
				print uid, uname
    """
	def executeQuery(self, sql):
		cur1 = self.__getConnect()
		aa = cur1.execute(sql)
		resList = cur1.fetchmany(aa)
		cur1.close()
		self.connection.close()
		return resList