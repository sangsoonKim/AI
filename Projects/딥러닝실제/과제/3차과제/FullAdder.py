# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 19:34:27 2021

@author: KSS
"""

import numpy as np

class AND:
    def __init__(self,x,y):
        self.x = x
        self.y=  y

    def andin(self):
        tmp = np.sum(self.x*self.y)
        if tmp <= 0:
            return 0
        else:
            return 1
    
class OR:

    def __init__(self,x,y):
        self.X = x
        self.Y = y
  
    def orin(self):
        tmp = np.sum(self.X + self.Y)
        if tmp <= 0:
            return 0
        else:
            return 1
              
class NAND:
 
    def __init__(self,x,y):
        self.X = x
        self.Y = y
   
    def xorin(self):
        tmp = np.sum(self.X*self.Y)
        if tmp <= 0:
            return 1
        else:
            return 0
        
        
a, b = input('숫자 두 개를 입력하세요: ').split('+')    # 입력받은 값을 공백을 기준으로 분리
c = int(a)   # 변수를 정수로 변환한 뒤 다시 저장

e= format(c,'b')
f = str(e)

lista = [0,0,int(f[0]),int(f[1])]

print('첫번째 값의 이진화 값은 {0}입나다,'.format(e))
#if(len(d))
#listX = []
d = int(b)    # 변수를 정수로 변환한 뒤 다시 저장
g = format(d,'b')
h = str(g)
listb = [0,0,int(h[0]),int(h[1])]
print('두번째 값의 이진화 값은 {0}입나다,'.format(h))

#for length in len()

##########################################
#0Layer
#XOR
s1 = NAND(lista[3],listb[3])
s2 = s1.xorin()

s3 = OR(lista[3],listb[3])
s4 = s3.orin()

temp = AND(s2,s4)
Result1A = temp.andin()

#AND
s5 = AND(lista[3],listb[3])
Result1B = s5.andin()

##########################################
#1layer
#XOR -> SUM
carry = int(0)

s6 = NAND(Result1A,carry)
s7 = s6.xorin()

s8 = OR(Result1A,carry)
s9 = s8.orin()

temp = AND(s7,s9)
Result2A = temp.andin() #SUM

SUM1 = Result2A
print('SUM1 {0}입나다,'.format(SUM1))
#AND
s10 = AND(Result1A,carry)
Result2B = s10.andin()

##########################################
#2Layer
#OR CARRY
s11 = OR(Result2B,Result1B)
ResultCarry = s11.orin()
print('Carry1 {0}입나다,'.format(ResultCarry))


##########################################
##########################################
##########################################################
#0Layer
s1 = NAND(lista[2],listb[2])
s2 = s1.xorin()

s3 = OR(lista[2],listb[2])
s4 = s3.orin()

temp = AND(s2,s4)
Result1A = temp.andin()

#AND
s5 = AND(lista[2],listb[2])
Result1B = s5.andin()

##########################################
#1layer
#XOR -> SUM
carry = ResultCarry

s6 = NAND(Result1A,carry)
s7 = s6.xorin()

s8 = OR(Result1A,carry)
s9 = s8.orin()

temp = AND(Result1A,carry)
Result2A = temp.andin() #SUM
SUM2 = Result2A
print('SUM2 {0}입나다,'.format(SUM2))


#AND
s10 = AND(Result1A,carry)
Result2B = s10.andin()
##########################################
#2Layer
#OR CARRY
s11 = OR(Result2B,Result1B)
ResultCarry2 = s11.orin()
print('Carry2 {0}입나다,'.format(ResultCarry2))

srtResult = '0b' +str(ResultCarry2)  +str(SUM2)+ str(SUM1) 
print('{0}입나다,'.format(srtResult))
intResult=int(srtResult,2)
print('두수의 합은 {0}입나다,'.format(intResult))


        
    
    



