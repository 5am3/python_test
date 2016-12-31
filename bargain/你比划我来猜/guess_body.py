import pygame
from pygame.locals import *
from sys import exit
import os
import xlrd

#------0.以下获取表格内容--------
def get_name(x):
	data = xlrd.open_workbook('list.xlsx')#打开文件
	table=data.sheets()[0]#获取表页
	nrows = table.nrows#获取行数
	name=table.row_values(x)[0]#获取内容
	error="抱歉，没了。"#当下一行无内容时提示文本
	if x>=nrows-1:
		return error
	else:
		return name
	#判断是否有文本，返回相应内容
#------0.到此结束-------------

#------1.以下是初始化游戏所需代码-------
pygame.init()
#初始化pygame
screen = pygame.display.set_mode((1920,1080), FULLSCREEN, 32)
#初始化屏幕，全屏，分辨率自己按需要改。

#以下两行为非全屏代码
# width,height=1920,1000
# screen=pygame.display.set_mode((width,height))

background=pygame.image.load("bj.png")
#载入背景图片
font1=pygame.font.Font("FZBWKSJW.TTF",200)
#载入字体
#-----1.到此结束---------------

#----2.以下为游戏主逻辑-----
i=0
#设置默认读取列表第几行内容
while 1:
	pygame.display.flip()
	#刷新屏幕
	for x in range(screen.get_width()//background.get_width()+1):
		for y in range(screen.get_height()//background.get_height()+1):
			screen.blit(background,(x*100,y*100))
	#画出背景图
	name=font1.render(get_name(i),True,(0,0,0))
	#获得文字内容
	screen.blit(name,(screen.get_width()/2-name.get_width()/2,screen.get_height()/2-name.get_height()/2))
	#绘制文字内容
	#-----2.1按键匹配-------
	for event in pygame.event.get():
		
		if event.type==pygame.QUIT:
			pygame.quit()
			exit(0)
		#主退出
		if event.type == pygame.KEYDOWN:
			if event.key==K_SPACE:
				i=i+1
			#按空格，读取下一行内容。
			if event.key==K_ESCAPE:
				pygame.quit()
				exit(0)
			#按esc键，退出游戏
	#-----2.1结束---------
#-----2.到此结束------------