#codeing=utf-8
#python获取本机名称与IP地址

#windows下获取函数
def gethostname_win():
    import socket
    #获取本机电脑名
    myname = socket.getfqdn(socket.gethostname(  ))
    #获取本机ip
    myaddr = socket.gethostbyname(myname)
    print (myname)
    print (myaddr)
#调用
gethostname_win()
'''
#Linux下获取Ip函数
def gethostip_linux():
  import socket
  import fcntl
  import struct

  def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])
'''

def f_ping():
    import os
    print(os.system("ping www.baidu.com"))

f_ping()