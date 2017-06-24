# -*- coding:utf-8 -*-				# 使用中文注释，最好放在第一行
# !/usr/bin/python				# 指定解释器

import platform					# 引入platform模块

system = platform.system()			# 操作系统
systemBitness = platform.architecture()[0]	# 系统架构（更偏向于python安装的版本）

systemVersion = platform.version()		# 系统版本
systemInfo = platform.uname()			# 系统信息
cpuplat = platform.machine()			# CPU平台
machinename = platform.node()			# 节点名，即机器名
pythonVersion = platform.python_version()	# python版本
linuxdist = platform.dist()			# linux发行版本

# 打印系统相关信息
print systemVersion
print systemInfo
print cpuplat
print machinename
print pythonVersion

# Windows
if system == "Windows" and systemBitness == "32bit":
  print "Windows 32bit"
if system == "Windows" and systemBitness == "64bit":
  print "Windows 64bit"
  
# Linux 
if system == "Linux" and systemBitness == "32bit":
  print "Linux 32bit"
  print linuxdist
if system == "Linux" and systemBitness == "64bit":
  print "Linux 64bit"
  print linuxdist
  
# Mac
if system == "Darwin" and systemBitness == "32bit":
  print "Darwin 32bit"
if system == "Darwin" and systemBitness == "64bit":
  print "Darwin 64bit"  
