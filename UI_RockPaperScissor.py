import tkinter as tk
from tkinter import Toplevel, messagebox
import random
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry('600x400')
root.title("Rock Paper Scissors Game")

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

def yes():
    root2 = Toplevel()
    root2.title("Rock Paper Scissors Game") 
    root2.geometry("800x600")
    root2.configure(bg='#add8e6')
    
    top_frame = tk.Frame(root2, bg='#add8e6', padx=20, pady=20)
    top_frame.pack(fill=tk.BOTH, expand=True)
    
    middle_frame = tk.Frame(root2, bg='#add8e6', padx=20, pady=20)
    middle_frame.pack(fill=tk.BOTH, expand=True)

    bottom_frame = tk.Frame(root2, bg='#add8e6', pady=20)
    bottom_frame.pack(fill=tk.BOTH, expand=True)

    points_frame = tk.Frame(root2, bg='#add8e6', pady=20)
    points_frame.pack(fill=tk.BOTH, expand=True)
    
    round_label = tk.Label(top_frame, text="Round 1", font=('Comic Sans MS', 24, 'bold'), bg='#add8e6', fg='darkblue')
    round_label.pack()


    compoints = 0
    userpoints = 0
    rounds = 1

    user_choice_label = tk.Label(middle_frame, text="You: ", font=('Comic Sans MS', 18), bg='#add8e6', fg='black')
    user_choice_label.pack(pady=10)

    computer_choice_label = tk.Label(middle_frame, text="Computer: ", font=('Comic Sans MS', 18), bg='#add8e6', fg='black')
    computer_choice_label.pack(pady=10)

    round_result = tk.Label(middle_frame, text="", font=('Comic Sans MS', 18), bg='#add8e6', fg='red')
    round_result.pack(pady=10)

    user_points_label = tk.Label(points_frame, text="Your points: 0", font=('Comic Sans MS', 18, 'bold'), bg='#add8e6', fg='black')
    user_points_label.pack(side='left', padx=20)

    computer_points_label = tk.Label(points_frame, text="Computer points: 0", font=('Comic Sans MS', 18, 'bold'), bg='#add8e6', fg='black')
    computer_points_label.pack(side='right', padx=20)

    def update_score(uchoice, Cchoice):
        nonlocal compoints, userpoints, rounds

        if (uchoice == "rock" and Cchoice == "paper") or (uchoice == "paper" and Cchoice == "scissors") or (uchoice == "scissors" and Cchoice == "rock"):
            compoints += 1
            result = "Computer wins!"
        elif (uchoice == "paper" and Cchoice == "rock") or (uchoice == "scissors" and Cchoice == "paper") or (uchoice == "rock" and Cchoice == "scissors"):
            userpoints += 1
            result = "You win!"
        else:
            result = "It's a draw!"

        round_result.config(text=result)
        user_points_label.config(text=f"Your points: {userpoints}")
        computer_points_label.config(text=f"Computer points: {compoints}")

        rounds += 1

        if rounds <= 3:
            round_label.config(text=f"Round {rounds}")
        else:
            if userpoints > compoints:
                final_result = "🎉 You won the game! 🎉"
            elif userpoints < compoints:
                final_result = "😞 You lost the game. 😞"
            else:
                final_result = "🤝 It's a draw. 🤝"
                
            final_result_label = tk.Label(middle_frame, text=final_result, font=('Comic Sans MS', 24, 'bold'), bg='#add8e6', fg='darkblue')
            final_result_label.pack(pady=10)

            b1.pack_forget()
            b2.pack_forget()
            b3.pack_forget()

            play_again_button = tk.Button(bottom_frame, text="Play Again", font=('Comic Sans MS', 18), command=play_again, bg='#4CAF50', fg='black', relief='flat', width=10)
            play_again_button.pack(side="left", padx=20, expand=True)

            exit_button = tk.Button(bottom_frame, text="Exit", font=('Comic Sans MS', 18), command=root.destroy, bg='#f44336', fg='black', relief='flat', width=10)
            exit_button.pack(side="left", padx=20, expand=True)

    def make_choice(uchoice):
        user_choice_label.config(text=f"You: {uchoice}")
        
        lst = ["rock", "paper", "scissors"]
        Cchoice = random.choice(lst)
        
        computer_choice_label.config(text=f"Computer: {Cchoice}")

        update_score(uchoice, Cchoice)

    def load_image(name):
        img = Image.open(name)
        img = img.resize((100, 100))
        return ImageTk.PhotoImage(img)

    rock_img = load_image("C:/Users/yasha/OneDrive/Desktop/Python_learning/RockPaperScissor/rock.png")
    paper_img = load_image("C:/Users/yasha/OneDrive/Desktop/Python_learning/RockPaperScissor/paper.png")
    scissors_img = load_image("C:/Users/yasha/OneDrive/Desktop/Python_learning/RockPaperScissor/scissor.png")

    b1 = tk.Button(bottom_frame, image=rock_img, command=lambda: make_choice("rock"), bg='#add8e6', relief='flat')
    b1.image = rock_img
    b1.pack(side="left", padx=20, pady=20, expand=True)

    b2 = tk.Button(bottom_frame, image=paper_img, command=lambda: make_choice("paper"), bg='#add8e6', relief='flat')
    b2.image = paper_img
    b2.pack(side="left", padx=20, pady=20, expand=True)

    b3 = tk.Button(bottom_frame, image=scissors_img, command=lambda: make_choice("scissors"), bg='#add8e6', relief='flat')
    b3.image = scissors_img
    b3.pack(side="left", padx=20, pady=20, expand=True)

def no():
    iExit = messagebox.askyesno("Rock Paper Scissors Game", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()

def play_again():
    for widget in root.winfo_children():
        widget.destroy()
    yes()

label1 = tk.Label(root, text="Play Rock Paper Scissors?", font=('Comic Sans MS', 24, 'bold'), pady=20, bg='#add8e6', fg='darkblue')
label1.pack(pady=20)

button_frame = tk.Frame(root, bg='#add8e6')
button_frame.pack(pady=20)

button1 = tk.Button(button_frame, text="Yes", width=14, height=2, command=yes, bg='#4CAF50', fg='black', font=('Comic Sans MS', 18), relief='flat')
button1.pack(side="left", padx=20)

button2 = tk.Button(button_frame, text="No", width=14, height=2, command=no, bg='#f44336', fg='black', font=('Comic Sans MS', 18), relief='flat')
button2.pack(side="left", padx=20)

center_window(root)

root.configure(bg='#add8e6')
root.mainloop()
