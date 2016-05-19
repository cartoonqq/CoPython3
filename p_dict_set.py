#-*-coding:utf-8-*-

#:list:[]
#:tuple:()
#:dict:{:,}
#:set:([])
#:set:{}
'''
v_dict={'xiaoming':80,'xiaoli':70,'xiaowang':90,'xiaowang':100,'xiaowang':99}
print(v_dict)
print(v_dict['xiaoming'])

#字典key不存在的3种异常判断:
try:
    print(v_dict['xiaoming1'])
except Exception as e:
    print('name:',e,'not exist')
v_name=input('input name:')  #输入姓名获取分数
print('%s分数:'%v_name,v_dict.get(v_name,'此姓名不存在'))

#可以在get()函数中直接带input()函数输入
print(v_dict.get(input('name:'),'此姓名不存在'))

v_name=input('input name:')
if v_name in  v_dict:
    print(v_dict[v_name])
else:
    print(v_name,'此姓名不存在')

#删除字典Key：
d_name=input('input name;')
try:
    v_dict.pop(d_name)
    print(v_dict)
except Exception as e:
    print(d_name,'not exist')

v_set1={1,2,3}
print(v_set1)
v_set2=set([2,3,4])
print(v_set2)
print(v_set1|v_set2)
print(v_set1&v_set2)

v_set3=set([2,[3,4]])
print(v_set3)
'''

