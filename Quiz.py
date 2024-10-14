from tkinter import *
 
# define question dictionary
question = {"1.India’s ‘National Sports Day’ coincides with the birthday of which sportsperson ?": ['Milkha Singh','Syed Abdul Rahim','Kapil Dev','Dhyan Chand'],
"2.In which year did Independent India win its first Olympic gold medal ?":['2008','1948','1972','1960'], 
"3.Who was the first Indian woman to win an Olympic medal ?": ['Karnam Malleswari','Saina Nehwal','Mary Kom','Sakshi Malik'], 
"4.What is the name of the International Organisation that regulates basketball in the world ?":['FIBA','NBA','IBA','RBA'], 
"5.Knockout and Knockdown are the terms related to which sport ?":['Hockey','Boxing','Cricket','Badminton']
}
# define answer list
ans = ['Dhyan Chand', '1948', 'Karnam Malleswari','FIBA','Boxing']
 
current_question = 0
 
 
def start_quiz():
    start_button.forget()
    next_button.pack()
    next_question()
 
 
def next_question():
    global current_question
    if current_question < len(question):
        check_ans()
        user_ans.set('None')
        c_question = list(question.keys())[current_question]
        
        clear_frame()
        
        Label(f1, text=f"Question : {c_question}", padx=15,
              font="calibre 12 normal").pack(anchor=NW)
        
        for option in question[c_question]:
            Radiobutton(f1, text=option, variable=user_ans,
                        value=option, padx=28).pack(anchor=NW)
        current_question += 1
    else:
        next_button.forget()
        check_ans()
        clear_frame()
        output = f"Your Score is {user_score.get()} out of {len(question)}"
        Label(f1, text=output, font="calibre 25 bold").pack()
        Label(f1, text="Thank You for Participating",
              font="calibre 18 bold").pack()
 
 
def check_ans():
    temp_ans = user_ans.get()
    if temp_ans != 'None' and temp_ans == ans[current_question-1]:
        user_score.set(user_score.get()+1)
 
 
def clear_frame():
    for widget in f1.winfo_children():
        widget.destroy()
 
 
if __name__ == "__main__":
    root = Tk()
    
    root.title("GK QUIZ APP")
    root.geometry("850x520")
    root.minsize(800, 400)
 
    user_ans = StringVar()
    user_ans.set('None')
    user_score = IntVar()
    user_score.set(0)
 
    Label(root, text=" SPORTS Quiz", 
          font="calibre 30 bold",
          relief=SUNKEN, background="Yellow", 
          padx=10, pady=9).pack()
    Label(root, text="", font="calibre 10 bold").pack()
    start_button = Button(root, 
                          text="Start Quiz",
                          command=start_quiz, 
                          font="calibre 16 bold")
    start_button.pack()
 
    f1 = Frame(root)
    f1.pack(side=TOP, fill=X)
 
    next_button = Button(root, text="Next Question",
                         command=next_question, 
                         font="calibre 16 bold")
 
    root.mainloop()