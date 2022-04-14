#!/usr/bin/env python
# coding: utf-8

# # 第十七组计算器

# In[ ]:


import tkinter 
from math import sqrt

root = tkinter.Tk()
root.minsize(280,500)#初始化最小大小
root.title('第十七组的计算器')


# # 1、界面布局

# In[ ]:


result = tkinter.StringVar()
result.set(0)
result2 = tkinter.StringVar()
result2.set(0)
#显示板
label1 =  tkinter.Label(root,font=('微软雅黑',20),bg='#EEE9E9',bd='9',fg='#828282',anchor='se',textvaria=result2)
label1.place(width = 280,height = 115)
label2 =  tkinter.Label(root,font=('微软雅黑',30),bg='#EEE9E9',bd='9',fg='black',anchor='se',textvaria=result)
label2.place(y = 115,width = 280,height = 60)


# In[ ]:


btn7 =  tkinter.Button(root,text='7',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressNum('7'))  #tkinter要求由按钮（或者其它的插件）触发的控制器函数不能含有参数若要给函数传递参数，需要在函数前添加lambda
btn7.place(x = 0,y = 285,width = 70,height = 55)
btn8 =  tkinter.Button(root,text='8',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressNum('8'))
btn8.place(x = 70,y = 285,width = 70,height = 55)
btn9 =  tkinter.Button(root,text='9',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressNum('9'))  
btn9.place(x = 140,y = 285,width = 70,height = 55)
btn4 =  tkinter.Button(root,text='4',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressNum('4'))  #tkinter要求由按钮（或者其它的插件）触发的控制器函数不能含有参数若要给函数传递参数，需要在函数前添加lambda
btn4.place(x = 0,y = 340,width = 70,height = 55)
btn5 =  tkinter.Button(root,text='5',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressNum('5'))
btn5.place(x = 70,y = 340,width = 70,height = 55)
btn6 =  tkinter.Button(root,text='6',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressNum('6'))  
btn6.place(x = 140,y = 340,width = 70,height = 55)
btn1 =  tkinter.Button(root,text='1',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressNum('1'))
btn1.place(x = 0,y = 395,width = 70,height = 55)
btn2 =  tkinter.Button(root,text='2',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressNum('2'))
btn2.place(x = 70,y = 395,width = 70,height = 55)
btn3 =  tkinter.Button(root,text='3',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressNum('3'))  
btn3.place(x = 140,y = 395,width = 70,height = 55)
btnzc =  tkinter.Button(root,text='%',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressSign('%'))
btnzc.place(x = 0,y = 450,width = 70,height = 55)
btn0 =  tkinter.Button(root,text='0',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressNum('0'))
btn0.place(x = 70,y = 450,width = 70,height = 55)
btnpo =  tkinter.Button(root,text='.',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressNum('.'))  
btnpo.place(x = 140,y = 450,width = 70,height = 55)

btnAC =  tkinter.Button(root,text='AC',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressSign('AC'))
btnAC.place(x = 0,y = 175,width = 70,height = 55)
btnback =  tkinter.Button(root,text='←',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressSign('b'))
btnback.place(x = 70,y = 175,width = 70,height = 55)
btn3 =  tkinter.Button(root,text='÷',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressSign('/'))  
btn3.place(x = 140,y = 175,width = 70,height = 55)
btnleft =  tkinter.Button(root,text='(',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressleft())
btnleft.place(x = 0,y = 230,width = 70,height = 55)
btnright =  tkinter.Button(root,text=')',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressright())
btnright.place(x = 70,y = 230,width = 70,height = 55)
btnlifang =  tkinter.Button(root,text='^2',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressfang())  
btnlifang.place(x = 140,y = 230,width = 70,height = 55)

btngen =  tkinter.Button(root,text='√',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : presssqrt())  
btngen.place(x = 210,y = 175,width = 70,height = 55)
btncheng =  tkinter.Button(root,text='×',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressSign('*'))  
btncheng.place(x = 210,y = 230,width = 70,height = 55)
btnplus =  tkinter.Button(root,text='+',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressSign('+'))  
btnplus.place(x = 210,y = 285,width = 70,height = 55)
btnjian =  tkinter.Button(root,text='-',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressSign('-'))  
btnjian.place(x = 210,y = 340,width = 70,height = 55)
btnequal =  tkinter.Button(root,text='=',bg='yellow',font=('微软雅黑',20),fg='#4F4F4F',bd=0.5,command = lambda : pressequal())  
btnequal.place(x = 210,y = 395,width = 70,height = 110)


# In[ ]:


lists=[]
ispressSign = False
isequal = False
operateLists = [[0, 0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 0,0], [0, 0, 0, 0, 1, 0, 0], [1, 1, 1, 1, 1, 2, 3],
                [0, 0, 0, 0, 3, 0, 0],[1, 1, 1, 1, 1, 3, 2]] # 大于为0，小于为1，等于为2，顺序为+-*/（）


# In[ ]:


def pressNum(num):
    global lists
    global ispressSign
    global isequal
    
    if isequal == True: #若已经算完一遍，则初始化
        pressSign('AC')
        isequal = False
        
    if ispressSign == False:#用于复原输入框
        pass
    else:
        result.set(0)
        ispressSign = False
        
        
    oldnum = result.get()
    if num == '.':
        result.set(oldnum + num)
    else:
        if oldnum == '0':  # 若为0则清除
            result.set(num)
        else:
            newnum = oldnum + num
            result.set(newnum)
    
    
def pressSign(sign):
    global lists
    global ispressSign
    global isequal
    num = result.get()
    
    if isequal == True: 
        result2.set('0')
        isequal = False
    
    if sign == 'b':
        a = num[0:-1]
        if a == '':
            result.set('0')
        else:
            result.set(a)
        return
    
    string_2 = result2.get()
    if ispressSign == False:
        result.set(num)
        if string_2 == '0':
            string_2 = num + sign
        else:
            string_2 = string_2 + num + sign

        lists.append(num)

    else:
        string_2 = string_2 + sign

    result2.set(string_2)
    lists.append(sign)

    if sign == 'AC':  # 清空
        lists.clear()
        result.set(0)
        result2.set(0)
        ispressSign = False
        return

    ispressSign = True

        
def pressequal():#等于计算
    global lists
    global isequal
    global ispressSign
    
    curnum = result.get()
    if ispressSign == False:
        lists.append(curnum)
    lists_2 = lists[:]
    lists_2.append('#')
    computrstr = ''.join(lists)
    try:  # 异常处理
        endNum = computerLists(lists_2)
    except Exception as e:
        result.set('ERROR')
        return

    if endNum % 1 == 0:
        endNum = int(endNum)
    else:
        endNum = round(endNum, 5)
    isequal = True
    ispressSign = False
    result.set(endNum)
    result2.set(computrstr)
    lists.clear()
 

    
def presssqrt():#开方计算
    global lists
    
    temp_num = sqrt(float(result.get()))
    if temp_num % 1 == 0:
        temp_num = int(temp_num)
    else:
        temp_num = round(temp_num, 5)
    result.set(temp_num)
    
    
def pressfang():#平方计算
    global lists

    temp_num = pow(float(result.get()),2)
    if temp_num % 1 == 0:
        temp_num = int(temp_num)
    result.set(temp_num)

    
def pressleft():
    lists.append('(')
    string_2 = result2.get()
    if string_2 == '0':
        string_2 = '('
    else:
        string_2=string_2 + '('
        
    result2.set(string_2)
    

def pressright():
    global ispressSign

    num = result.get()
    lists.append(num)
    lists.append(')')
    string_2 = result2.get()
    if string_2 == '0':
        string_2 = num + ')'
    else:
        string_2 = string_2 + num + ')'

    # result.set(')')
    ispressSign = True
    result2.set(string_2)


def computerLists(lists2):

    global operateLists
    ListsNum = []
    ListsSign = [6]
    x = lists2.pop(0)
    
    while x !='#' or ListsSign !=[6]:
        if is_number(x):
            ListsNum.append(float(x)) #若为数字则直接压入数字列表
            x=lists2.pop(0)
            continue
            
        if x == '+':
            b = 0
        elif x == '-':
            b = 1
        elif x == '*':
            b = 2
        elif x == '/':
            b = 3
        elif x == '(':
            b = 4
        elif x == ')':
            b = 5
        elif x == '#':
            b = 5
        else :
            return (-1)
        
        #if ListsSign == []:          #若字符列表为空则先压入元素
        #   ListsSign.append(b) 
        # else:                        # 运算顺序大于为0，小于为1，等于为2，顺序为+-*/（）
        a = int(ListsSign[-1])
        if operateLists[a][b] == 1:
            ListsSign.append(b)
            x = lists2.pop(0)
        elif operateLists[a][b] == 2:
            ListsSign.pop(-1)
            x = lists2.pop(0)
        elif operateLists[a][b] == 0:
            sign1 = ListsSign.pop(-1)
            num2 = ListsNum.pop(-1)
            num1 = ListsNum.pop(-1)
            answer_1 = signtra(num1,sign1,num2)
            ListsNum.append(answer_1) 
            
                
    return (ListsNum[0])
    
        
def signtra(num1,sign1,num2):
    if sign1 == 0:
        return (num1+num2)
    if sign1 == 1:
        return (num1-num2)
    if sign1 == 2:
        return (num1*num2)
    if sign1 == 3:
        return (num1/num2)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False    
    
root.mainloop()