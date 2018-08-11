# -*- coding:utf-8 -*-  
# file: FileMerage.py

def is_txt(fn):
	'''匹配目标文件的filter函数
	'''
	if r'.utf' in fn:
		return fn

def format_context(a):
	''' 1:
		原始: \{智代}「那么，今天就来庆祝自立吧」
		目标: 智代:「那么，今天就来庆祝自立吧」
		2:
		原始: 6月26日
		目标: 第6月26日
		3:
		删除 <0001>
	'''
	import re
	reg1 = re.compile(r'<\d{4}>')
	reg2 = re.compile(r'(\d{1,2}月\d{1,2}日)')
	reg3 =  re.compile(r'\\\{(.+)\}') 
	return reg3.sub(r'\1'+':',reg2.sub('第'+r'\1',reg1.sub('',a)))

# os模块中包含很多操作文件和目录的函数  

import os  
FindPath='C:/Users/sgjr/Desktop/a18a'
FileNames = list(filter(is_txt,os.listdir(FindPath)))
print(FileNames)

# FileNames = list(map(lambda x: FindPath+'/'+x ,FileNames))
outfile=open(FindPath+'/outfile.txt','w',encoding='utf-8') 
for f in list(map(lambda x: FindPath+'/'+x ,FileNames)):
	for a in open(f,'r',encoding='utf-8'):
		outfile.write(format_context(a)) 
outfile.close()

# list(map(lambda x: os.path.join(FindPath,fn) ))
# fullfilename=os.path.join(FindPath,fn)


# def GetFileList(FindPath,FlagStr=[]): 
# ''''' 
# #获取目录中指定的文件名 
# #>>>FlagStr=['F','EMS','txt'] #要求文件名称中包含这些字符 
# #>>>FileList=GetFileList(FindPath,FlagStr) #
# '''
# 	import os 
# 	FileList=[] 
# 	FileNames=os.listdir(FindPath) 
# 	if (len(FileNames)>0): 
# 	for fn in FileNames: 
# 		if (len(FlagStr)>0): 
# 		#返回指定类型的文件名 
# 			if (IsSubString(FlagStr,fn)): 
# 			fullfilename=os.path.join(FindPath,fn) 
# 			FileList.append(fullfilename) 
# 			else: 
# 			#默认直接返回所有文件名 
# 			fullfilename=os.path.join(FindPath,fn) 
# 			FileList.append(fullfilename) 
# 			#对文件名排序 
# 	if (len(FileList)>0):
# 		FileList.sort()
# 	 return FileList

# #获取目标文件夹的路径  
# meragefiledir = os.getcwd()+'\\MerageFiles'  
# #获取当前文件夹中的文件名称列表  
# filenames=os.listdir(meragefiledir)  
# #打开当前目录下的result.txt文件，如果没有则创建  
# #文件也可以是其他类型的格式，如result.js  
# file=open('result.txt','w')  
# #向文件中写入字符  
# #file.write('python\n')  

# #先遍历文件名  
# for filename in filenames:  
#     filepath=meragefiledir+'\\'+filename  
#     # 遍历单个文件，读取行数  
#     for line in open(filepath):  
#         file.writelines(line)  
#     file.write('\n')  

# #关闭文件
# file.close()  

