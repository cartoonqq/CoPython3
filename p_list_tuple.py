# -*- coding:utf-8 -*-
#LIST，用[]
classmaster=['zhao','qian','sun','li']
print(classmaster)
#长度
print(len(classmaster))
print(max(classmaster))
print(min(classmaster))
print(classmaster[2])
#取最后一个:
print(classmaster[len(classmaster)-1])
print(classmaster[-1])

#2.  append() 方法向列表的尾部添加一个新的元素。只接受一个参数。
#3.  extend()方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中，元素也就是可以一个，也可以多个
classmaster.append('wang')
print('1:',classmaster)
classmaster.extend(['zhang'])
print('2:',classmaster)
classmaster.extend('zhang') #没有作为一个列表，就默认为多个参数
print('3:',classmaster)
classmaster.extend(['zhang1','zhang2'])  #参数多个，列表只有1个
print('4:',classmaster)

#insert()插入
classmaster.insert(2,'@@')
print('5:',classmaster)

#pop()删除
classmaster.pop(2)
print('6:',classmaster)

p_tt=['00','11',classmaster]  #二维数组
print('7:',p_tt)
print('8:',p_tt[2][2])
classmaster[0]='zhang@@'
print('9:',classmaster)

#tuple，用（）
classtuple=('zhao','qian','sun')
print(classtuple[1:3])
#classtuple.insert(2,'li')  #不支持改动
classtuple=(1,)
print(classtuple[0])