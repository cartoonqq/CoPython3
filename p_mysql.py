#codeing=utf-8
import pymysql
import time

p_date=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print("[NOW]:%s" % p_date)


def f_connDB(p_user,p_pwd,p_db,p_ip='192.168.10.120'):
  #try:
    print("--1111--%s,%s,%s,%s" % (p_ip,p_user,p_pwd,p_db))
    #获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
    conn=pymysql.connect(host=p_ip,user=p_user,passwd=p_pwd,db=p_db,charset='utf8')
    #conn=pymysql.connect(host='192.168.10.120',user='oa_product',passwd='oa_product123',db='oa_product',charset='utf8')
    cur=conn.cursor() #获取一个游标
    cur.execute("select * from sys_user")
    data=cur.fetchall()
    for d in data :
    #注意int类型需要使用str函数转义
       print("ID: "+str(d[0])+'  名字： '+d[1]+"  性别： "+d[2])

    cur.close()#关闭游标
    conn.close()#释放数据库资源
  #except  Exception :print("发生异常")

f_connDB('oa_product','oa_product123','oa_product')