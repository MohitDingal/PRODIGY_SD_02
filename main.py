import tkinter as tk
import random
root = tk.Tk()

root.geometry("400x400")
ans = random.randint(1,100)
root.title("Random Number Guesser")
print(ans)
def numguess():
    global ans
    guess  = int(num.get())
    if guess>100 or guess<0:
        a.config(text = "Enter the number within the limit")
    elif guess > ans:
        a.config(text = "Enter something smaller")
    elif guess < ans:
        a.config(text = "Enter something bigger")
    else:
        a.config(text = "You have guessed the number!")

head1 = tk.Label(root,text ="Guessing Game!",font = ("Arial",18))
head1.pack(pady = 5)
head2 = tk.Label(root,text = "The number to be guessed is between 1 to 100",font = ("Arial",8))
head2.pack(pady = 2)
text1 = tk.Label(root,text = "Enter your guess: ",font = ("Arial",13))

text1.pack(padx = 5,pady = 7)

num = tk.Entry(root, width = 25, font = ("Arial",15))
num.pack(padx = 5,pady =5)

check = tk.Button(root, text = "Guess", bg = "Blue",command = numguess, font = ("Arial",10))
check.pack(padx = 5,pady = 5)

a = tk.Label(root, text= "",font = ("Arial Bold",13))
a.pack(padx = 5,pady =5)

root.mainloop()