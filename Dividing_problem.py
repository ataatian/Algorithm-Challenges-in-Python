#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 16:38:03 2021

@author: nooshinnejati
"""
import math



def FindNum(AA, N, D):

    #    //N includes the last element of aN
    #    //Left (group 1) sum is D more than Right (group 2) sum.
    #  //Assuming that AA is sorted ascending

    if (N==1):
        return 0
    
    if (N == 2):
        if ((D == 0) and (AA[0]==AA[1])):
            return 2
        if ((D!=0) and (AA[0] == AA[1] + D)):
    	    return 1
        return 0

    
    i=N-2
    count=0
    Result=0
    print("H",N,i)
    while (i>=0) and (AA[i]==AA[N - 1]):
        count += 1
        i -= 1 
        
        
#    print("N: ", N)      
    
    Result = FindNum (AA, N - 1, D)    + SumSum (AA, N - 1, AA[N - 1] + D)  + \
    FindNum (AA, N - 1, AA[N - 1] + D) + Left2(AA, N, D, AA[N - 1], count)
    
    return Result

def SumSum (AA, M, Y):
#    //a1+a2+...+aM=S
    if (Y < AA[0]):
        return 0
    
    if (M == 1):
        if (AA[0] == Y):
            return 1
        else:
            return 0

    if (M > 1):
        if (Y == AA[M - 1]):
            return SumSum (AA, M - 1, Y) + 1
        else:
            return SumSum (AA, M - 1, Y) + SumSum (AA, M - 1, Y - AA[M - 1])


def Left2(B, N, D, aN, C):
#    //N includes the last element of aN as well.
    
    if (C==0):
        return 0

    Res=0
    for u in range(1,C+1):
        if ((u==1) and (D==0)):
            Res=C
        else:
            if (N>1+u):
                Res= Res+ NchooseK(C,u) * SumSum(B, N-1-u, aN*(u-1)+D)
            
    return Res

def NchooseK(t,k):
    if (t>=k):
        return math.factorial(t)/(math.factorial(k)*math.factorial(t-k))
    else:
        return 0


#main ()

Out = 0
A=[1,1,1,1,1]
#A=[1,2,2,3,4,5,6,7,7,8,9,10,11]

mylen = len(A)
#  bubbleSort (A, len);
print("Length: ",mylen  )
print("Sorted Array: ")

for i in range(0,mylen):
    print (i,":",A[i]) 

print(A)

Out = FindNum(A, mylen, 0);
  
print("The answer is: ", int(Out))

#######################################################






