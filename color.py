#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/27 10:06
# @Author  : 彦小明IT
# @File    : color.py
# @Software: PyCharm
# @description： 运用colorama库改变终端输出的颜色

from colorama import Fore, Style, Back, init
init(autoreset=True)  # 初始化，设置颜色自动恢复

class Colored(object):
	#  前景色:红色  背景色:默认
	def red(self, s):
		return Fore.RED + s + Fore.RESET

	#  前景色:绿色  背景色:默认
	def green(self, s):
		return Fore.GREEN + s + Fore.RESET

	#  前景色:黄色  背景色:默认
	def yellow(self, s):
		return Fore.YELLOW + s + Fore.RESET

	#  前景色:蓝色  背景色:默认
	def blue(self, s):
		return Fore.BLUE + s + Fore.RESET

	#  前景色:洋红色  背景色:默认
	def magenta(self, s):
		return Fore.MAGENTA + s + Fore.RESET

	#  前景色:青色  背景色:默认
	def cyan(self, s):
		return Fore.CYAN + s + Fore.RESET

	#  前景色:白色  背景色:默认
	def white(self, s):
		return Fore.WHITE + s + Fore.RESET

	#  前景色:黑色  背景色:默认
	def black(self, s):
		return Fore.BLACK

	#  前景色:白色  背景色:绿色
	def white_green(self, s):
		return Fore.WHITE + Back.GREEN + s

	def dim(self, s):
		return Style.DIM + s

	def dave(self, s):
		return Style.BRIGHT + Fore.GREEN + s