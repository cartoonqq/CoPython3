#-*-coding:utf-8-*-

###if
def f_get_bmi(height,weight):
        bmi=weight/(height*height)

        if bmi < 18.5:
            print("%.2f,体重过轻"%bmi)
        elif bmi>=18.5 and bmi <25:
            print('%.2f,体重正常'%bmi)
        elif bmi >=25 and bmi< 32:
            print('%.2f,肥胖'%bmi)
        else:
            print('%.2f,严重肥胖'%bmi)
def main():
    try:
        #height=float(input('input height(m):'))
        height=float(input('input height(m):'))
        weight=float(input('input weight(kg):'))
        f_get_bmi(height,weight)
    except Exception as e:  #此处的异常捕获会把上面的执行以及函数中的执行的错误都捕获打印
        print('error:',e)
        raise ValueError('cuowu shuzi:%s'%e)
    finally:
        print('gogogogogoog:')
import logging
#main()
print('aaaaaa')

###for
def p_for():
    try:
        v_sum=0
        i=1
        for m in list(range(101)):   #range函数，生成整数序列
            v_sum=v_sum+m
            print('%-3d:%d'%(i,v_sum))
            i=i+1
    except Exception as e:
        print(e)
#p_for()

L = ['Bart', 'Lisa', 'Adam']
for v_name in L:
    print('hello,%s'%v_name)


#while
def p_while():
    try:
        v_sum=0
        i=1
        while i < 101:
            v_sum=v_sum+i
            print('%-3d:%d'%(i,v_sum))
            i=i+1
    except Exception as e:
        print(e)
#p_while()


