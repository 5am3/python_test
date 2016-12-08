import random
import copy

def display(mtrx):#初始化棋盘
	for i in range(4):
		s=""
		print('*********************')
		for j in range(4):
			s=s+"*%4s"%(mtrx[i][j] if mtrx[i][j] else ' ')
		print(s+"*")
	print('*********************')

def init(): #初始化内容
    mtr = [[0 for i in range(4)] for j in range(4)]  
    ran_pos = random.sample(range(16), 2)
    mtr[ran_pos[0]//4][ran_pos[0]%4] = mtr[ran_pos[1]//4][ran_pos[1]%4] = 2
    return mtr

def random_number(mtr):
	ran_pos=random.sample(range(16), 1)
	if not mtr[ran_pos[0]//4][ran_pos[0]%4]:
		mtr[ran_pos[0]//4][ran_pos[0]%4]=2
		return mtr
	else:
		random_number(mtr)
	return mtr

def onlive(map_n):
	for i in range(4):
		for j in range(4):
			if not map_n[i][j]:
				return 1
			elif i>0 and map_n[i][j]==map_n[i-1][j]:
				return 1 
			elif i<3 and map_n[i][j]==map_n[i+1][j]:
				return 1 
			elif j<3 and map_n[i][j]==map_n[i][j+1]:
				return 1 
			elif j>0 and map_n[i][j]==map_n[i][j-1]:
				return 1 
	return 0

def top(map_n):
	global visit,score
	for i in range(4):
		for j in range(4):
			if i>0:
				if map_n[i][j] and map_n[i][j]==map_n[i-1][j] and i*10+j not in visit and (i-1)*10+j not in visit:#判断是否有两个上下相邻且相等的数字
					map_n[i-1][j]=map_n[i-1][j]*2
					score+=map_n[i-1][j]
					map_n[i][j]=0
					visit.append((i-1)*10+j)
					visit.append(i*10+j)
					map_n=top(map_n)
				elif not map_n[i-1][j] and map_n[i][j]:#判断该数字上方是否为空
					map_n[i-1][j]=map_n[i][j]
					map_n[i][j]=0
					map_n=top(map_n)
	return map_n

def xia(map_n):
	global visit,score
	for i in range(4):
		for j in range(4):
			if i<3:
				if map_n[i][j] and map_n[i][j]==map_n[i+1][j] and i*10+j not in visit and (i+1)*10+j not in visit:#判断是否有两个上下相邻且相等的数字
					map_n[i+1][j]=map_n[i+1][j]*2
					score+=map_n[i+1][j]
					map_n[i][j]=0
					visit.append((i+1)*10+j)
					visit.append(i*10+j)
					map_n=xia(map_n)
				elif not map_n[i+1][j] and map_n[i][j]:#判断该数字上方是否为空
					map_n[i+1][j]=map_n[i][j]
					map_n[i][j]=0
					map_n=xia(map_n)
	return map_n

def left(map_n):
	global visit,score
	for i in range(4):
		for j in range(4):
			if j>0:
				if map_n[i][j] and map_n[i][j]==map_n[i][j-1] and i*10+j not in visit and i*10+j-1 not in visit:#判断是否有两个上下相邻且相等的数字
					map_n[i][j-1]=map_n[i][j-1]*2
					score+=map_n[i][j-1]
					map_n[i][j]=0
					visit.append(i*10+j-1)
					visit.append(i*10+j)
					map_n=left(map_n)
				elif not map_n[i][j-1] and map_n[i][j]:#判断该数字上方是否为空
					map_n[i][j-1]=map_n[i][j]
					map_n[i][j]=0
					map_n=left(map_n)
	return map_n

def right(map_n):
	global visit,score
	for i in range(4):
		for j in range(4):
			if j<3:
				if map_n[i][j] and map_n[i][j]==map_n[i][j+1] and i*10+j not in visit and i*10+j+1 not in visit:#判断是否有两个上下相邻且相等的数字
					map_n[i][j+1]=map_n[i][j+1]*2
					score+=map_n[i][j+1]
					map_n[i][j]=0
					visit.append(i*10+j+1)
					visit.append(i*10+j)
					map_n=right(map_n)
				elif not map_n[i][j+1] and map_n[i][j]:#判断该数字上方是否为空
					map_n[i][j+1]=map_n[i][j]
					map_n[i][j]=0
					map_n=right(map_n)
	return map_n

def random_num(map_num_o,map_num_n):
	global on_live,map_num#声明全局变量
	if map_num_o==map_num_n:	#判断是否可移动
		print("你再往这边走，它也不会动的。")
	else:
		map_num=random_number(map_num_n)#生成随机数
		on_live=onlive(map_num)#判断是否存活
		display(map_num_n)#绘制地图
		print("←：a  ↓: s ↑: w →: d  \n输入字符后请点击回车。","\n你的分数为%d"%score)#输出提示文字与分数。（\n是换行的意思。%d是格式控制语句。）
#以下为游戏主函数

	#游戏开始，放到一个死循环中，一直循环下去
while 1:
	score = 0#初始化游戏得分
	map_num = init()#初始化第一个数
	display(map_num)#绘制图案
	print("←：a  ↓: s ↑: w →: d  \n输入字符后请点击回车。")#输出提示文字
	on_live=1#设置游戏未输（28行onlive函数会控制这个）
	#以下为依据游戏开始
	while on_live:#检测游戏进行
		visit=[]#创建一个列表，存储已经合并过得数（有点说不清，想知道的找我来问。）
		map_num_o=copy.deepcopy(map_num)#复制一个地图
		
		fangxiang=input()#输入方向	
		if fangxiang=="w":#判断输入为什么方向
			map_num_n=top(map_num)#执行向上函数
			random_num(map_num_o,map_num_n)#执行产生随机数函数
		elif fangxiang=="s":
			map_num_n=xia(map_num)#执行向下函数
			random_num(map_num_o,map_num_n)#执行产生随机数函数
		elif fangxiang=="a":
			map_num_n=left(map_num)#执行向左函数
			random_num(map_num_o,map_num_n)#执行产生随机数函数
		elif fangxiang=="d":
			map_num_n=right(map_num)#执行向右函数
			random_num(map_num_o,map_num_n)#执行产生随机数函数
		else:
			print("亲，你输错东西了吧。")#检测不出来是什么方向，输出错误提示
	#一局游戏结束，输出提示信息
	print("游戏结束。你的分数为%d"%score)
	input("按任意键重新开始")
