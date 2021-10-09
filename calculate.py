from tkinter import *
import tkinter

#方法
def append_num(i):
    lists.append(str(i))
    result_num.set(''.join(lists))

def operator(i):
    if len(lists) > 0:
        if lists[-1] in ['+','-','*','/']:
            lists[-1] = i 
        else:
            lists.append(i)
        result_num.set(''.join(lists))

def clear():
    lists.clear()
    result_num.set(0)

def equall():
    a = ''.join(lists)
    end_num = eval(a)
    lists.clear()
    lists.append(str(end_num))
    result_num.set(''.join(lists))

#创建一个界面窗口
win = Tk()
#取一个名字
win.title("Calculator")
#设定窗口的大小
win.geometry("255x455")
#制作按钮
bu7 = Button(win,text = 7,width = 2,font = ("Arial",31),command = lambda : append_num(7))
bu8 = Button(win,text = 8,width = 2,font = ("Arial",31),command = lambda : append_num(8))
bu9 = Button(win,text = 9,width = 2,font = ("Arial",31),command = lambda : append_num(9))
bu4 = Button(win,text = 4,width = 2,font = ("Arial",31),command = lambda : append_num(4))
bu5 = Button(win,text = 5,width = 2,font = ("Arial",31),command = lambda : append_num(5))
bu6 = Button(win,text = 6,width = 2,font = ("Arial",31),command = lambda : append_num(6))
bu1 = Button(win,text = 1,width = 2,font = ("Arial",31),command = lambda : append_num(1))
bu2 = Button(win,text = 2,width = 2,font = ("Arial",31),command = lambda : append_num(2))
bu3 = Button(win,text = 3,width = 2,font = ("Arial",31),command = lambda : append_num(3))
bu0 = Button(win,text = 0,width = 2,font = ("Arial",31),command = lambda : append_num(0))
bu_eq = Button(win,text = '=',width = 2,font = ("Arial",31),command = lambda : equall())
bu_cl = Button(win,text = 'c',width = 2,font = ("Arial",31),command = lambda : clear())
bu_ad = Button(win,text = '+',width = 2,font = ("Arial",31),command = lambda : operator('+'))
bu_mi = Button(win,text = '-',width = 2,font = ("Arial",31),command = lambda : operator('-'))
bu_mul = Button(win,text = '*',width = 2,font = ("Arial",31),command = lambda : operator('*'))
bu_div = Button(win,text = '/',width = 2,font = ("Arial",31),command = lambda : operator('/'))
#放入到框架中
bu7.place(x = 10, y = 100)
bu8.place(x = 70, y = 100)
bu9.place(x = 130, y = 100)
bu4.place(x = 10, y = 185)
bu5.place(x = 70, y = 185)
bu6.place(x = 130, y = 185)
bu1.place(x = 10, y = 270)
bu2.place(x = 70, y = 270)
bu3.place(x = 130, y = 270)
bu0.place(x = 10 , y = 355)
bu_eq.place(x = 70,y = 355)
bu_cl.place(x = 130,y = 355)
bu_ad.place(x = 190, y = 100)
bu_mi.place(x = 190, y = 185)
bu_mul.place(x = 190, y = 270)
bu_div.place(x = 190, y = 355)

lists = []
result_num = tkinter.StringVar()
result_num.set(0)
en = tkinter.Label(win,textvariable = result_num,width = 10 ,font = ("Arial",31),justify = "left",anchor = "se")
en.place(x = 10 ,y =30)

mainloop()