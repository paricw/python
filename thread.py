#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# C:\Users\win 10\AppData\Local\Programs\Python\Python37

# import threading
# import time
# 线程
# 如何使用？
    # 方式1：调用创建线程 API，适用于简单的任务
    # 方式2：线程类，是继承了 threading 方法的类
# n=0
# while n < 6 :
    # print('time()',time.ctime(time.time()))
    # n=n+1


# function: 每隔 intervel s 打印下 当前时间
# def print_time(threadName, intervel, counter):
    # while counter:        # counter 控制循环的次数
        # time.sleep(intervel) # 颜色 delay(1) (1)s
        # print ("%s: %d %s" % (threadName, counter, time.ctime(time.time()))) # time.ctime(time.time())打印当前的时间
        # counter -= 1


# 类 = 属性 + 方法
# 线程类属性： threadID，name，counter + 基类的属性
# 线程类方法:  run + 基类的方法
# class myThread (threading.Thread):   #继承父类threading.Thread
    # def __init__(self, threadID, name, intervel):
        # threading.Thread.__init__(self)  #继承一定要先初始化基类，掉基类的__init__方法
        # self.threadID = threadID
        # self.name = name
        # self.intervel = intervel

    # def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
        # print ("Starting " + self.name)
        # print_time(self.name, self.intervel, 5)
        # print ("Exiting " + self.name)
 

# def task1():
    # count = 20  
    # while(count > 0):
        # print (count,"play music")
        # count = count - 1
        # time.sleep(1)

# def task2():
    # count = 20
    # while(count > 0):
        # print (count,'play movies')
        # count = count - 1
        # time.sleep(2)

if __name__=='__main__':
    # 创建新线程
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)

    # 开启线程
    thread1.start()  #实际是调用的myThread 的 run 方法
    thread2.start()
   
    # print ("Exiting Main Thread")

    # t1 = threading.Thread(target=task1, name='music')  #创建
    # t1.start()                                         #启动
    # t2 = threading.Thread(target=task2, name='movies')
    # t2.start()
