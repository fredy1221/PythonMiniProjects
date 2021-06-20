import tkinter as tk
import random


HEIGHT = 600
WIDTH = 800

target_num = random.randint(1, 10)
trials_number=0

def check_number(guess):
    print(target_num)
    try:
        if int(guess)<target_num:
            label_log['text']="your guess is less than the actual number"
        elif int(guess)>target_num:
            label_log['text']="your guess is greater than the actual number"
        elif int(guess)==target_num:
            label_log['text']="good guess!"
        else:
            label_log['text']="enter a valid number"
    except:
        label_log['text']="enter a valid number"

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH ,bg='#7883e3')
canvas.pack()


intro_frame = tk.Frame(root, bg='#ab6b57', bd=5)
intro_frame.place(relx=0.5, rely=0.1, relwidth=0.95, relheight=0.2, anchor='n')

label = tk.Label(intro_frame,text="Guess the number", font= ('Helvetica', 20, 'bold'),bg="#e6c3e8")
label.place(relwidth=1, relheight=1)


frame = tk.Frame(root, bg='#ab6b57', bd=5)
frame.place(relx=0.5, rely=0.45, relwidth=0.95, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Confirm", font=40, command=lambda: check_number(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)


second_frame = tk.Frame(root, bg='#80c1ff', bd=5)
second_frame.place(relx=0.5, rely=0.65, relwidth=0.5, relheight=0.1, anchor='n')

label_trials = tk.Label(second_frame,text="# trials remaining")
label_trials.place(relx=0.5,rely=0,relwidth=1, relheight=1, anchor='n')


third_frame = tk.Frame(root, bg='#80c1ff', bd=5)
third_frame.place(relx=0.5, rely=0.87, relwidth=0.95, relheight=0.1, anchor='n')

label_log = tk.Label(third_frame)
label_log.place(relx=0.5, relwidth=1, relheight=1, anchor='n')

root.mainloop()

