#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# C:\Users\win 10\AppData\Local\Programs\Python\Python37

# 为什么推荐使用线程类，而不使用通过 API 的那种方式！
# 线程类和普通类有什么区别，线程类能够独立运行，而普通类不能独立运行，多了一个run方法。
# 线程类如何运行，通过run 方法运行。
import threading
import time

#属性：小美本身，身高，体重 + 基类的属性   ---所有的属性通过self引用
#方法：吃饭，睡觉 +基类的方法              ---所有的方法通过实例化的类名引用
#重新实现基类的run方法，并在start时开始运行

class Dog(threading.Thread):
    def __init__(self,height,weight,name):
        threading.Thread.__init__(self)
        self.height = height
        self.weight = weight
        self.name = name
        
    def get_height(self):
        print(self.name,self.height)
    
    def get_weight(self):
        print(self.name,self.weight)

    def run(self):
        while (1):
            print(self.name,"在吃饭")
            time.sleep(5)
            print(self.name,"在睡觉")
            time.sleep(10)


if __name__=='__main__':
    Miss_Mei = Dog(20,6.2,'xiaomei')
    Mr_Kuai = Dog(15,8,'快乐')
    Mr_Kuai.start()
    Miss_Mei.start()
    