'''
This is the Python Mini-Project(Cartoon Quiz) that Vinayaka Hegde, Sidharth U Nair and Vaibhav Singh have done together
To begin with the project, we need to first import 2 libraries into our program.
one is tkinter(for GUI) and the other is random(to jumble the question order)
'''
from tkinter import *
from time import time
import random as r



# questions is a list which holds all the questions used in the program
questions = [
    # Chota Bheem
    "What is this character's name? ",
    "Where does he live? ",
    "Which animal is his best friend? ",
    "Which is his favorite sweet?",
    # Doraemon
    "From which timeline did this character come from? ",
    "Who is the creator of this character? ",
    "What is this character scared of?",
    "What is  this character's specialty",
    # Tom and Jerry
    "Who created this series? ",
    "What is the cat's full name? ",
    "Who is the first owner of the cat? ",
    "What is Spike in this cartoon series?",
    # Shinchan
    "Which cartoon is this? ",
    "Which language was this originally made in?",
    "How many friends does he have?",
    "How many pets does this character have?",
    # Spongebob
    "Who is the character in this image?",
    "In which year did this animation come out?",
    "Who is the best friend of this character?",
    "Who is the creator of this animated series?",

]
# answer_choice is a list which holds all the answers for the respective question
answers_choice = [
    # Chota Bheem
    ["Raju", "Jaggu", "Chota Bheem", "Dhoni"],
    ["Bheemnagar", "Pehalwanpur", "Rampur", "Dholakpur"],
    ["Cat", "Monkey", "Buffalo", "Donkey"],
    ["Gulab Jamun", "Laddoo", "Rasgulla", "Jalebi"],
    # Doraemon
    ["Past", "Future", "Present", "A timeline which doesn't exist"],
    ["Fujiki Fujiho", "Yoshito Usui", "Masashi Kishimoto", "None of the above"],
    ["Assignments", "Rats", "Flies", "Cakes"],
    ["Creating fire from his bare hands ", "blow off mountains with a single blow", "Take out anything which is usable but has a drawback", "Nothing..."],
    # Tom and Jerry
    ["Walt Disney", "Hanna and Barbera", "Warner Bros", "Universal"],
    ["Tom cat", "Thomas cat", "Tommy cat", "Tom Riddle"],
    ["Mammy Two-Shoes", "Mammy Apron", "Aunt Rose", "Guille"],
    ["A Cat", "A Mouse", "A Dog", "A Bird"],
    # Shinchan
    ["Shinchan", "Horrid Henry", "Dexter", "Naruto"],
    ["English", "Hindi", "Japanese", "Korean"],
    ["1", "6", "3", "4"],
    ["2", "1", "4", "3"],
    # SpongeBob
    ["Shinchan", "Ben 10", "Spongebob", "Patrick Star"],
    ["2001", "1999", "2005", "1996"],
    ["Sandy Cheeks", "Mr. Krabs", "Patrick Star", "Squidward Tentacles"],
    ["Stephen Hillenberg", "Duncan Rouleau", "Stephen Hawkins", "Hillary Clinton"],

]

# answers is a list containing all the correct answers which is basically an index of the particular list in the answer_choice list
answers = [3,4,2,2, # Chota Bheem
           2,1,2,3, # Doraemon
           2,2,1,3, # Tom and Jerry
           1,3,4,2, # Shinchan
           3,2,3,1 # Spongebob
           ]
# user_answer is the list of entries that the user answers
user_answer = []
#indexes is the list of indexes of the questions list
indexes = []
# gen is the function which inputs elements into the indexes list
def gen():
    global indexes
    i = 0
    while i <= 19:
        x = r.randint(0, 19) # Generating random indexes for questions
        if x in indexes:
            continue # To make sure that no indexes are repeated
        else:
            indexes.append(x) # adding elements to the list
            i+=1 # loop updation

'''
showresult is the function which at the end of the quijm uz shows the score and 
imports an appropriate image based on the user's score
'''
def showresult(score):
    lblQuestion.destroy() # to remove the question label
    lblimage.destroy() # to remove the meme
    r1.destroy() # to remove the radiobutton 1
    r2.destroy() # to remove the radiobutton 2
    r3.destroy() # to remove the radiobutton 3
    r4.destroy() # to remove the radiobutton 4
    labelimage = Label(
        root,
        background = "white",
        border = 0,
    )
    labelimage.pack(pady=(50,30))
    labelresulttext = Label(
        root,
        font = ("Consolas",20),
        background = "white",
    )
    labelresulttext.pack()
    end_time = time()
    global start_time
    elapsed_time = str((end_time - start_time))[:4]

    s = str(score)
    if score >= 80:
        img = PhotoImage(file="great.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You scored "+s+"\n You Are Excellent !!"+"\nTime Taken :"+elapsed_time+" secs")
    elif (score >= 40 and score < 80):
        img = PhotoImage(file="ok.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You scored "+s+"\n You Can Be Better !!"+"\n Time Taken :"+elapsed_time+" secs")
    else:
        img = PhotoImage(file="bad.png")
        labelimage.configure(image=img)
        labelimage.image = img
        labelresulttext.configure(text="You scored "+s+"\n You Should Work Hard !!"+"\n Time Taken :"+elapsed_time+" secs")
'''
Calc is the function which defines the calculation of the score the user has procured
'''
def calc():
    global indexes,user_answer,answers
    t = 0
    score = 0
    for i in indexes:
        #user_answer.pop(0)
        if user_answer[t]+1 == answers[i]:
            score += 5 #scores will be allotted in the multiples of 5
        t += 1
    showresult(score)

#helper function to load images
def loadImage(d):
    global lblimage
    if (d <= 3):
        imag = PhotoImage(file="Chota Bheem.png")
        lblimage.config(image=imag)
        lblimage.image = imag
        lblimage.pack(before=lblQuestion)

    elif (d <= 7) and (d > 3):
        imag = PhotoImage(file="Doraemon.png")
        lblimage.config(image=imag)
        lblimage.image = imag
        lblimage.pack(before=lblQuestion)

    elif (d <= 11) and (d > 7):

        imag = PhotoImage(file="tom_and_jerry.png")
        lblimage.config(image=imag)
        lblimage.image = imag
        lblimage.pack(before=lblQuestion)
    elif (d <= 15) and (d > 11):
        imag = PhotoImage(file="Shinchan.png")
        lblimage.config(image=imag)
        lblimage.image = imag
        lblimage.pack(before=lblQuestion)

    elif (d <= 19) and (d > 15):
        imag = PhotoImage(file="Spogebob.png")
        lblimage.config(image=imag)
        lblimage.image = imag
        lblimage.pack(before=lblQuestion)
ques = 0
lblimage = None
#selected is a function which proceeds to the question after one question is answered
def selected():
    global radiovar,user_answer
    x = radiovar.get()
    user_answer.append(x)
    global lblQuestion,r1,r2,r3,r4
    global ques
    if ques < 19:
        ques += 1
        loadImage(indexes[ques])
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
    else:
        calc()
    radiovar.set(-1)

start_time = 0
#startquiz is the functions which proceeds to the quiz after the start button is pressed in the opening window
def startquiz():
    global start_time
    start_time = time()
    global lblQuestion,r1,r2,r3,r4
    #creating a label (question)
    lblQuestion = Label(root, text = questions[indexes[0]], font = ("Gabriola", 16), width = 500, justify = "center",
                        wraplength = 400, )
    lblQuestion.pack()
    global lblimage
    #question image
    lblimage = Label(root, bg="white")
    print(indexes) #order in which the questions are displayed
    global radiovar
    radiovar = IntVar(root)
    radiovar.set(-1)
#Assigning Radiobuttons
    r1 = Radiobutton(root,
                     text = answers_choice[indexes[0]][0], # to print the required option on the radiobutton
                     font = ("Times",12), # font for the options
                     value = 0, # giving the radiobutton a value to access it easily
                     command = selected,
                     variable = radiovar,
                     )
    r1.pack()
    r2 = Radiobutton(root,
                     text = answers_choice[indexes[0]][1],
                     font=("Times", 12),
                     value=1,
                     command = selected,
                     variable=radiovar,
                     )
    r2.pack()
    r3 = Radiobutton(root,
                     text = answers_choice[indexes[0]][2],
                     font=("Times", 12),
                     value=2,
                     command = selected,
                     variable=radiovar,
                     )
    r3.pack()
    r4 = Radiobutton(root,
                     text = answers_choice[indexes[0]][3],
                     font=("Times", 12),
                     value=3,
                     command = selected,
                     variable=radiovar,
                     )
    r4.pack()
    loadImage(indexes[0]) # load the image for the first question
'''
startIspressed is the function which destroys the front page when the start button is pressed
It also calls other functions like gen(which generates the sequence in which questions are displayed)
and startquiz(which starts the quiz)
'''
def startIspressed():
    labeltext.destroy()
    lblinstrct.destroy()
    lblrules.destroy()
    buttonstart.destroy()
    gen()
    startquiz()
root = Tk() # creating the window
root.title('Cartoon Quiz') # title of the window(displayed on the title bar)
root.config(bg="white") # background colour for the window
# Title for the front page
labeltext = Label(root,
                  text = 'Cartoon Quiz',
                  font = ("Gabriola", 48, "bold"),
                  bg = "white"
                  )
# the start button(displayed on the opening page)
buttonstart = Button(root,
                     text ="Start",
                     bg = "green",
                     fg = "white",
                     font = ("Gabriola", 24, "bold"),
                     width = 10,
                     command = startIspressed
                     )
lblinstrct = Label(root,
                   text = "Read the rules\n Click Start once you are ready",
                   bg = "white",
                   font = ("Gabriola", 24, "bold"),
                   justify = "center"
                   )
# Rules for the quiz(displayed on the opening page)
lblrules = Label(root,
                 bg = "black",
                 fg = "Yellow",
                 text = "RULES:\nThis quiz contains 5 images\nEach image will have 4 questions based on itself\n"
                        "Once you select a radio button that will be your final choice\nEach question carries 5 marks"
                        "\nHence think carefully before you answer",
                 font=("Times",18 ),
                 width = 500
                 )
# packing all the labels and buttons in the opening page
labeltext.pack(pady = (0,50))
buttonstart.pack()
lblinstrct.pack()
lblrules.pack(side = "bottom")
root.mainloop()