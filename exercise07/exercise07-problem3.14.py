# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 19:53:22 2016

@author: 文龙
"""

import pylab as pl
import math
class  Poincare_sections:
    """
    Program 3.14
    Repeat problem3.13,but give the two pendulums slightly different
    damping factors .
    """
    def __init__(self,friction_coefficient=0.5,gravity=9.8,rope_length=9.8,angular_frequency_of_driving_force=2/3,ampulitude=1.2,time_of_step=0.04,initial_angel=0.2):
        self.q1=friction_coefficient
        self.q2=friction_coefficient+0.001
        self.l=rope_length
        self.g=gravity
        self.Ω=angular_frequency_of_driving_force
        self.FD=ampulitude
        self.dt=time_of_step
        self.t=[0]
        self.ω1=[0]                
        self.ω2=[0]
        self.Θ1=[0.2] 
        self.Θ2=[0.2]
        self.dΘ=[0]
        self.log=[]


    def calculate(self):
        i=0
        while self.t[i]<=150:
            if self.Θ1[i]>math.pi:          #使角度在-π到+π之间有意义
                self.Θ1[i]=self.Θ1[i]-2*math.pi
            if self.Θ1[i]<-math.pi:
                self.Θ1[i]=self.Θ1[i]+2*math.pi
            else:
                self.Θ1[i]=self.Θ1[i]
    
            temp_ω1=self.ω1[i]+(-self.g/self.l*math.sin(self.Θ1[i])-self.q1*self.ω1[i]+self.FD*math.sin(self.Ω*self.t[i]))*self.dt
            self.ω1.append(temp_ω1)
            temp_Θ1=self.Θ1[i]+self.ω1[i+1]*self.dt
            self.Θ1.append(temp_Θ1)
            
            #上述计算了初始角度为0.2的单摆运动数据
            #下面的代码计算了初始q改变0.001的单摆运动数据
            if self.Θ2[i]>math.pi:
                self.Θ2[i]=self.Θ2[i]-2*math.pi
            if self.Θ2[i]<-math.pi:
                self.Θ2[i]=self.Θ2[i]+2*math.pi
            else:
                self.Θ2[i]=self.Θ2[i]
    
            temp_ω2=self.ω2[i]+(-self.g/self.l*math.sin(self.Θ2[i])-self.q2*self.ω2[i]+self.FD*math.sin(self.Ω*self.t[i]))*self.dt
            self.ω2.append(temp_ω2)
            temp_Θ2=self.Θ2[i]+self.ω2[i+1]*self.dt
            self.Θ2.append(temp_Θ2)
            self.t.append(self.t[i]+self.dt)
            self.dΘ.append(abs(self.Θ1[i+1]-self.Θ2[i+1]))#角度差列表

            i+=1
            
            

            
    def show_result(self):      #画图直观显示数据
        pl.plot(self.t,self.dΘ,"r")
        pl.xlabel("时间t")
        pl.ylabel("角度差")
        pl.xlim(0,50)
        pl.ylim(0,0.05)
        pl.show()


a=Poincare_sections()
a.calculate()
a.show_result()
