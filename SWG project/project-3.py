#import package
from tkinter import *
from PIL import Image,ImageTk
import random

#defining a function
def info(a):
    global score
    global score1

    list = ['Snake','Water','Gun']
    Ranval = random.choice(list)
    print(Ranval)

    if a == 'Snake':
        snake_user = Label(win,image=snake,border=0)
        snake_user.place(x=822,y=100)
        if Ranval == 'Snake':
            snake_img = Label(win,image=snake,border=0)
            snake_img.place(x=50,y=100)
            label1 = Label(win,text='Draw      ',fg='black',bg='#29f6ff',font=('minian pro',15,'bold'))
            label1.place(x=500,y=230)
        elif Ranval == 'Water':
            water_img = Label(win,image=water,border=0)
            water_img.place(x=50,y=100)
            label2 = Label(win,text='You win! ',fg='black',bg='#29f6ff',font=('minian pro',15,'bold'))
            label2.place(x=500,y=230)
        else:
            gun_img = Label(win,image=gun,border=0)
            gun_img.place(x=50,y=100)
            label3 = Label(win,text='You loss!',fg='black',bg='#29f6ff',font=('minian pro',15,'bold'))
            label3.place(x=500,y=230)

        if Ranval == 'Gun':
            score += 1
            score_com = Label(win,text=''+str(score),fg='black',bg='#29f6ff')
            score_com.config(font=('consolas',25))
            score_com.place(x=127,y=380) 
        elif Ranval == 'Water':
            score1 += 1 
            score_user = Label(win,text=''+str(score1),fg='black',bg='#29f6ff')
            score_user.config(font=('consolas',25))
            score_user.place(x=942,y=380)


    elif a == 'water':
        snake_user = Label(win,image=water,border=0)
        snake_user.place(x=822,y=100)
        if Ranval == 'Snake':
            snake_img = Label(win,image=snake,border=0)
            snake_img.place(x=50,y=100)
            label3 = Label(win,text='You loss!',fg='black',bg='#29f6ff',font=('minian pro',15,'bold'))
            label3.place(x=500,y=230)
        elif Ranval == 'Water':
            water_img = Label(win,image=water,border=0)
            water_img.place(x=50,y=100)
            label1 = Label(win,text='Draw      ',fg='black',bg='#29f6ff',font=('minian pro',15,'bold'))
            label1.place(x=500,y=230)
        else:
            gun_img = Label(win,image=gun,border=0)
            gun_img.place(x=50,y=100)
            label2 = Label(win,text='You win! ',fg='black',bg='#29f6ff',font=('minian pro',15,'bold'))
            label2.place(x=500,y=230)

        if Ranval == 'Snake':
            score += 1
            score_com = Label(win,text=''+str(score),fg='black',bg='#29f6ff')
            score_com.config(font=('consolas',25))
            score_com.place(x=127,y=380) 
        elif Ranval == 'Gun':
            score1 += 1 
            score_user = Label(win,text=''+str(score1),fg='black',bg='#29f6ff')
            score_user.config(font=('consolas',25))
            score_user.place(x=942,y=380)

    else:
        snake_user = Label(win,image=gun,border=0)
        snake_user.place(x=822,y=100)
        if Ranval == 'Snake':
            snake_img = Label(win,image=snake,border=0)
            snake_img.place(x=50,y=100)
            label2 = Label(win,text='You win! ',fg='black',bg='#29f6ff',font=('minian pro',15,'bold'))
            label2.place(x=500,y=230)
        elif Ranval == 'Water':
            water_img = Label(win,image=water,border=0)
            water_img.place(x=50,y=100)
            label3 = Label(win,text='You loss!',fg='black',bg='#29f6ff',font=('minian pro',15,'bold'))
            label3.place(x=500,y=230)
        else:
            gun_img = Label(win,image=gun,border=0)
            gun_img.place(x=50,y=100)
            label1 = Label(win,text='Draw      ',fg='black',bg='#29f6ff',font=('minian pro',15,'bold'))
            label1.place(x=500,y=230)
        
        if Ranval == 'Water':
            score += 1
            score_com = Label(win,text=''+str(score),fg='black',bg='#29f6ff')
            score_com.config(font=('consolas',25))
            score_com.place(x=127,y=380) 
        elif Ranval == 'Snake':
            score1 += 1 
            score_user = Label(win,text=''+str(score1),fg='black',bg='#29f6ff')
            score_user.config(font=('consolas',25))
            score_user.place(x=942,y=380)

    return

#Windows initialization
win = Tk()
win.title(' Snake Water Gun')
win.iconbitmap('icon.ico')#for convent image to ico file use (zamzar.com)
win.config(bg='#29F6FF')
win.resizable(0,0)
win.geometry('1080x600')

#picture initialization
snake_open = Image.open('snake.jpg')
re_img = snake_open.resize((200,200),Image.ANTIALIAS)
snake = ImageTk.PhotoImage(re_img)

gun_open = Image.open('gun.jpg')
re_gun = gun_open.resize((200,200),Image.ANTIALIAS)
gun = ImageTk.PhotoImage(re_gun)

water_open = Image.open('water.jpg')
re_water = water_open.resize((200,200),Image.ANTIALIAS)
water = ImageTk.PhotoImage(re_water)

#widgets
Frame(win,bg='#2196ff',width=1080,height=74,border=0).pack()

btn = Button(win,text='SNAKE',bg='#CC1AFF',fg='white',command=lambda:info('Snake'))
btn.configure(font=('consolas',15,'bold'),
            width=10,
            height=2,
            activebackground='grey')
btn.place(x=365,y=480)

btn1 = Button(win,text='WATER',bg='#7229FF',fg='white',command=lambda:info('water'))
btn1.configure(font=('consolas',15,'bold'),
            width=10,
            height=2,
            activebackground='grey')
btn1.place(x=485,y=480)

btn2 = Button(win,text='GUN',bg='#1F35FF',fg='white',command=lambda:info('gun'))
btn2.configure(font=('consolas',15,'bold'),
            width=10,
            height=2,
            activebackground='grey')
btn2.place(x=605,y=480)

name = Label(win,text='Created by :   DhanaSelvan')
name.configure(font=('minion pro',13),
                bg='#29F6FF',
                fg='black')
name.place(x=858,y=575)

com_lab = Label(win,text='Computer')
com_lab.configure(font=('minion pro',22),
                bg='#2196ff',
                fg='white')
com_lab.place(x=50,y=20)

user_lab = Label(win,text='User')
user_lab.configure(font=('minion pro',22),
                bg='#2196ff',
                fg='white')
user_lab.place(x=953,y=20)

user_score = Label(win,text='Score')
user_score.configure(font=('minion pro',27),
                bg='#29F6FF',
                fg='brown')
user_score.place(x=900,y=330)

com_score = Label(win,text='Score')
com_score.configure(font=('minion pro',27),
                bg='#29F6FF',
                fg='brown')
com_score.place(x=90,y=330)

snake_img = Label(win,image=snake,border=0)
snake_img.place(x=50,y=100)
snake_user = Label(win,image=snake,border=0)
snake_user.place(x=822,y=100)

water_img = Label(win,image=water,border=0)
water_img.place(x=50,y=100)
water_user = Label(win,image=water,border=0)
water_user.place(x=822,y=100)

gun_img = Label(win,image=gun,border=0)
gun_img.place(x=50,y=100)
gun_user = Label(win,image=gun,border=0)
gun_user.place(x=822,y=100)

score = 0
score1 = 0
score_com = Label(win,text=''+str(score),fg='black',bg='#29f6ff')
score_com.config(font=('consolas',18))
score_com.place(x=127,y=380)
score_user = Label(win,text=''+str(score1),fg='black',bg='#29f6ff')
score_user.config(font=('consolas',18))
score_user.place(x=942,y=380)

win.mainloop()