# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 11:12:44 2016

@author: 文龙
"""

import pylab as pl
import math
class billiard_on_a_square_table():
    """This is a continuation of the trajectory of a billiard
    on a stadium-shaped table
    """
    def __init__(self,time_step=0.01,x0=0.2,y0=0,vx0=1,vy0=0.6,steps=20000,α=0.01):
        self.x=[x0]
        self.y=[y0]
        self.vx=[vx0]
        self.vy=[vy0]
        self.dt=time_step
        self.t=[0]
        self.steps=steps
        self.α=α
        self.poincare_x=[]
        self.poincare_vx=[]
    def backtrack(self,condition,x,y,vx,vy,t):#倒退回溯确定撞击点
        m=0
        while eval(condition):
            x=x+vx*self.dt/100
            y=y+vy*self.dt/100
            m+=1    
        return x,y,self.dt/100*m+t
        
    def change_upper(self,x,y,vx,vy): #上半圆碰撞改变速度方向的函数
        n1=math.sqrt(vx**2+vy**2)
        n2=math.sqrt(x**2+(y-self.α)**2)
        cos1=(vx*x+vy*(y-self.α))/(n1*n2)
        vx=vx-2*cos1*n1*x/n2
        vy=vy-2*cos1*n1*(y-self.α)/n2
        return vx,vy

    def change_down(self,x,y,vx,vy):#下半圆碰撞改变速度方向的函数
        n1=math.sqrt(vx**2+vy**2)
        n2=math.sqrt(x**2+(y+self.α)**2)
        cos1=(vx*x+vy*(y+self.α))/(n1*n2)
        vx=vx-2*cos1*n1*x/n2
        vy=vy-2*cos1*n1*(y+self.α)/n2
        return vx,vy
        
    def calculate(self):
        for i in range(self.steps):
            temp_x=self.x[i]+self.vx[i]*self.dt
            temp_y=self.y[i]+self.vy[i]*self.dt
            temp_vx=self.vx[i]
            temp_vy=self.vy[i]
            self.x.append(temp_x)
            self.y.append(temp_y)
            self.vx.append(temp_vx)
            self.vy.append(temp_vy)
            self.t.append(self.t[i]+self.dt)
            if (math.sqrt(self.x[i+1]**2+(self.y[i+1]-self.α)**2)>1) and self.y[i]>self.α:
                self.x[i+1],self.y[i+1],self.t[i+1]=self.backtrack("math.sqrt(x**2+(y-self.α)**2)<=1",self.x[i],self.y[i],self.vx[i],self.vy[i],self.t[i])
                self.vx[i+1],self.vy[i+1]=self.change_upper(self.x[i+1],self.y[i+1],self.vx[i],self.vy[i])
            if (math.sqrt(self.x[i+1]**2+(self.y[i+1]+self.α)**2)>1) and self.y[i]<-self.α:
                self.x[i+1],self.y[i+1],self.t[i+1]=self.backtrack("math.sqrt(x**2+(y+self.α)**2)<=1",self.x[i],self.y[i],self.vx[i],self.vy[i],self.t[i])
                self.vx[i+1],self.vy[i+1]=self.change_down(self.x[i+1],self.y[i+1],self.vx[i],self.vy[i])
            if (self.x[i+1]<-1):
                self.x[i+1],self.y[i+1],self.t[i+1]=self.backtrack("x>=-1",self.x[i],self.y[i],self.vx[i],self.vy[i],self.t[i])
                self.vx[i+1]=-self.vx[i]
            if (self.x[i+1]>1):
                self.x[i+1],self.y[i+1],self.t[i+1]=self.backtrack("x<=1",self.x[i],self.y[i],self.vx[i],self.vy[i],self.t[i])
                self.vx[i+1]=-self.vx[i]
            if (self.y[i+1]<0.01):
                self.poincare_x.append(self.x[i+1])
                self.poincare_vx.append(self.vx[i+1])
                
  
        return self.x,self.y
        
    def show_result(self):
        pl.plot(self.x,self.y,".")
        pl.xlabel('x')
        pl.ylabel('y')
        pl.xlim(-1,1)
        pl.ylim(-1,1)
        pl.title('trajectory of a billiard on a stadium-shaped table')
        pl.show()
                
a=billiard_on_a_square_table()
a.calculate()
a.show_result()       
