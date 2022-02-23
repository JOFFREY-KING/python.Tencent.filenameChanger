
'''
1、获取键盘的管理员权限
2、关联键盘的相应函数
3、记录键盘按下的值（关闭程序就会流失数据）
4、保存记录的内容(记事本保存)
'''
from pynput.keyboard import  Listener #监控者模块

#2、关联键盘的相应函数
def press(key):
    print("按下")


def releases(key):
    print("松开")

#1、获取键盘的管理员权限
with Listener(on_press=press,on_releases=releases) as listener:
    listener.join() #创建监听线程




