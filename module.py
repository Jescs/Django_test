'''
author:jescs
date:2017/9/18
describle:实现计算机功能
'''


class Calculator():

    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a+self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        return self.a/self.b
