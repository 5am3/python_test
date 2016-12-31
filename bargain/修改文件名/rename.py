#-*coding:utf-8*-
import os
import xlrd
def rname():
	i=0
	path="./pic"
	filelist=os.listdir(path)#所有文件
	for files in filelist:#遍历所有文件
		Olddir=os.path.join(path,files)#原来文件路径
		if os.path.isdir(Olddir):#如果是文件夹则跳过
			continue
		filename=os.path.splitext(files)[0]#文件名
		filetype=os.path.splitext(files)[1]#后缀
		code=getcode(filename)
		if code:
			i=i+1
			Newdir=os.path.join(path,code+filetype)
			os.rename(Olddir,Newdir)#重命名
		else:
			print(filename,"查询不到")
	print('共修改成功',i,"个文件。")
def getcode(x):
	data = xlrd.open_workbook('list.xlsx')#打开文件
	table=data.sheets()[0]#获取表页
	nrows = table.nrows#获取行数
	for i in range(nrows):#遍历每行
		name=table.row_values(i)[1]
		code=table.row_values(i)[0]
		if name==x:
			return code
rname()