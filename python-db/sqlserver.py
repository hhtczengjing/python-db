#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

import pymssql

class MSSQL():
	"""MSSQL初始化方法"""
	def __init__(self, host, user, password, database):
		self.host = host
		self.user = user
		self.password = password
		self.database = database

	"""
		获取数据库连接对象
	"""
	def __getConnect(self):
		if not self.database:
			raise(NameError, "未指定需要连接的数据库名称")
		self.connection = pymssql.connect(host=self.host, user=self.user, password=self.password, database=self.database, charset="utf8")
		cur = self.connection.cursor()
		if not cur:
			raise(NameError, "连接数据库失败")
		else:
			return cur

	"""
        执行非查询语句
        调用示例：
            ms = MSSQL(host="localhost", user="sa", password="123456", database="Demo")
            ms.executeUpdate("DELETE FROM T_USER")
    """
	def executeUpdate(self, sql):
		cur2 = self.__getConnect()
		cur2.execute(sql)
		self.connection.commit()
		self.connection.close()
	
	"""
    	执行查询语句
    	返回的是一个包含tuple的list，list的元素是记录行，tuple的元素是每行记录的字段
    	调用示例：
			ms = MSSQL(host="localhost", user="sa", password="123456", database="Demo")
			list = ms.executeQuery("SELECT uid, uname FROM T_USER")
			for (uid, uname) in list:
				print uid, uname
    """
	def executeQuery(self, sql):
		cur1 = self.__getConnect()
		cur1.execute(sql)
		resList = cur1.fetchall()
		self.connection.close()
		return resList

