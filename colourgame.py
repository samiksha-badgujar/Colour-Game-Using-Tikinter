from tkinter import *
import random
from tkinter import messagebox

#declaring colors

colors = ["Red", "Blue", "Green", "Pink", "Black", "Yellow", "Orange", "White", "Purple", "Brown", "Cyan"]

score = 0
timeleft = 10

# For launching the game

def startGame(event):
    if timeleft == 10:

#Calling countdown function
        
        countdown()
        
#Calling nextcolor function 

    nextcolor()


#Function for countdown

def countdown():
    global timeleft

#Checking timeleft
    
    if timeleft == 0:        
        messagebox.showinfo("Time Left", "Time is over and Your score is " + str(score))

#Checking if time is over

    if timeleft > 0:        
        timeleft -= 1
        timeLabel.config(text="Time Left : " + str(timeleft))
        timeLabel.after(1000, countdown)


#For changing color of text

def nextcolor():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()
        if e.get().lower() == colors[1].lower():
            score += 1

        e.delete(0, END)
        random.shuffle(colors)

        label.config(fg=str(colors[1]), text=str(colors[0]))
        
        scoreLabel.config(text="Your concetration is low. Score: " + str(score))

        if score<4:
            
            scoreLabel.config(text="Your concetration is low. Score: " + str(score))

        if score>4:
            
            scoreLabel.config(text="Your concentration is excellent. Score: " + str(score))

        if score==4:
            
            scoreLabel.config(text="Your concentration is good. Score: " + str(score))

#For quting the game

def Quit():
    global root 
    msg=messagebox.askquestion("Confirm","Are you want to Quit? You still have chances!")
    if msg=='yes':        
        root.destroy()


root = Tk()
root.title("Color Game")
root.geometry("500x400")
root.resizable(0, 0)

instruction = Label(root, text="Type the color of the words,and not the word text!", font=("Helvetica", 12))
instruction.pack()

scoreLabel = Label(root, text="Press Enter to start", font=("Helvetica", 12))
scoreLabel.pack()

timeLabel = Label(root, text="Time Left : ", font=("Helvetica", 12))
timeLabel.pack()

label = Label(root, font=("Helvetica", 60))
label.pack()

e = Entry(root,width="50")
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

btn1=Button(root, text= "QUIT",command=Quit)
btn1.pack(pady= 50)

root.mainloop()
