#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# C:\Users\win 10\AppData\Local\Programs\Python\Python37

#基类 = 属性 方法
class ball(object):
    def __init__(self, radius):
        self.radius = radius
    def get_size(self):
        return self.radius * self.radius
    def get_shape(self):
        return "i am a base ball"

#篮球  继承
#radius = 20 
#size
#Brand  = niling,    naike
class basket_ball(ball):
    def __init__(self, radius, Brand):
        ball.__init__(self, radius)     #引用父类的属性
        self.Brand = Brand

    def get_brand(self):
        return (self.Brand)
    
    def get_prince(self):
        return 1000
        
    def get_shape(self):
        return"i am a basketball"

#网球
#color

class tennis_ball(ball):
    def __init__(self,radius,color):
        ball.__init__(self, radius)
        self.color = color
        
    def get_color(self):
        return (self.color)
    
        
if __name__=='__main__':  #程序执行入口\

    # mytennisball = tennis_ball(8,'yellow')  #myball
    # print(mytennisball.get_size())
    # print(mytennisball.get_shape())
    # print(mytennisball.get_color())
    mybasketball = basket_ball(8,'naike')
    print(type(mybasketball))
    # print(mybasketball.get_shape())
    # print(mybasketball.get_brand())
    # print(mybasketball.get_size())
    fn = tennis_ball(8,'bule')
    print(type(fn))
