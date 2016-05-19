#codeing=utf-8
def f_map_upper(name):   #转大写
    return name.upper()
def f_map_title(name):   #单词首字母转大写
    return name.title()
def f_map_addstr(name):   #字符串连接
    addstr=print(name)
    return addstr

L1=['caowei','coco','co']
L2=list(map(f_map_upper,L1))
print(L2)
L3=list(map(f_map_title,L1))
print(L3)
f_map_addstr("caowei")
L4=reduce(f_map_addstr,L1) ###???
print(L4)