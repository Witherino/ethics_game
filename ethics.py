from tkinter import * # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import messagebox

year = 0

middle_x = 150
middle_y = 275
left_button_x = 85
right_button_x = 235
split_button_y = 400
button_pad_x = 10
button_pad_y = 2

top = Tk()
top.text = "Game Window"
top.geometry("400x550")


def clear():
	for widget in top.winfo_children():
		widget.destroy()
	
def tutorial():
	clear()
	top.title = "New Window"
	intro = StringVar()
	intro.set("""From this point on you'll be starting a new adventure. The choices you make along the way will have an impact on the person you are in the end. This is the screen you'll be directed to when you come the one of 10 endings availible for you to find. Have fun... """)
	newTitle = Message(top, textvariable = intro, justify= CENTER, width= 250, pady = 50, font = ("Helvetica", 14, "bold"))
	newTitle.pack()
	cont = Button(text="Continue", command= level_one, width = 10)
	cont.place(x = middle_x, y = middle_y)
	
def health_raise():
	clear()
	intro = StringVar()
	intro.set("""The comittee has set aside the money because of upcoming performance reviews. Despite not having any medical experience at all, they've asked you to start consulting on actual medical practice as well. A new patient has revealed to you that they have a severe allergy to ATP, an active ingredient. A doctor tells you the only common active ingredient in their treatement cycle is TCG. That's all the information given to you. Do you suggest the patient go through with this treatment?""")
	newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 13, "bold"))
	newTitle.pack()
	opt1 = Button(text="Yes", command= raise_treat_yes, width= 8)
	opt2 = Button(text="No", command= treat_no, width= 8)
	opt1.place(x = left_button_x,y =  split_button_y)
	opt2.place(x = right_button_x,y = split_button_y)
	
def raise_treat_yes():
	clear()
	intro = StringVar()
	intro.set("""The procedure went well for your patient, and they checked out 2 months after their treatment started. Your performance reviews were sparkling, and the hospital has offered you an executive position making $154,000 a year. Big jump, I know. Because of your LinkedIn presence, you've also garnered the attention of an upcoming financial consulting firm called Hail Mary Fiduciary. They're offering you $120,000 to start at their company. Do you stay at the hospital, or stretch out into the financial district?""")
	newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 13, "bold"))
	newTitle.pack()
	opt1 = Button(text="H.M.F", command= finance, width= 8)
	opt2 = Button(text="Hospital", command= raise_hospital, width= 8)
	opt1.place(x = left_button_x,y =  split_button_y)
	opt2.place(x = right_button_x,y = split_button_y)
	
def finance():
	clear()
	intro = StringVar()
	intro.set("""It's your first week at the new firm, and two clients walk through the door. It's up to you to decide if you'd rather consult with Phil, a young man with old money, or Cassandra, a woman looking to recoup losses from a divorce settlement.""")
	newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 13, "bold"))
	newTitle.pack()
	opt1 = Button(text="Phil", command= finance_phil, width= 8)
	opt2 = Button(text="Cassy", command= finance_cassy, width= 8)
	opt1.place(x = left_button_x,y =  split_button_y)
	opt2.place(x = right_button_x,y = split_button_y)

def finance_phil():
    clear()
    intro = StringVar()
    intro.set("""Phil tells you that he wants to make as much money as possible, and that he doesn't care about the legality of it. """)
    newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 13, "bold"))
    newTitle.pack()
    opt1 = Button(text="Phil", command= finance_phil, width= 8)  
    opt2 = Button(text="Cassy", command= finance_cassy, width= 8)
    opt1.place(x = left_button_x,y =  split_button_y)
    opt2.place(x = right_button_x,y = split_button_y)    
	
def raise_hospital():
	clear()
	intro = StringVar()
	intro.set("""One of the employees under you has recently revealed that a hospital board member has been sexually harrasing them. You know that whoever brings the harassment to light will likely be fired from the hospital. This board member donates many millions of dollars annually to the hospital allowing it to further serve the community in ways it wouldn't be able to otherwise. Do you encourage the employee to bring this harassment to light, bring up the harassment on your own and hope your solid reputation helps back the claim, or do you let it slide for the greater good?""")
	newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 13, "bold"))
	newTitle.pack()
	opt1 = Button(text="Encourage", command= hospital_enc, width= 8)
	opt2 = Button(text="Stand", command= hospital_stand, width= 8)
	opt3 = Button(text="Slide", command= hospital_slide, width= 8)
	opt3.place(x = 70,y =  split_button_y)
	opt1.place(x = 160,y =  split_button_y)
	opt2.place(x = 250,y = split_button_y)

	
def hospital_enc():
	clear()
	intro = StringVar()
	intro.set("""The employee brings the harassment to light, and is immediately let go from their duties at the hospital. An "investigation" was opened into their claims, and surprisingly enough, no evidence of wrongdoing was found. Your life at the hospital is now mostly filled with boring bureaucracy, but you never forget the worker who put their career on the line to make a change.""")
	newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 13, "bold"))
	newTitle.pack()
	opt1 = Button(text="Start Over", command= tutorial, width= 8)
	opt1.place(x = middle_x,y =  middle_y)
	
def hospital_slide():
	clear()
	intro = StringVar()
	intro.set("""You tell the employee to let the situation slide, and to be patient. 3 weeks pass, and it seems the board member makes a mistake by overstepping their bounds with a different employee. He's caught out in the open, and with nowhere to hide, he retires from the hospital in shame and takes his money with him. Everyone's salary takes a slight dip in order to continue providing all the services availible, but over time everything works out. """)
	newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 13, "bold"))
	newTitle.pack()
	opt1 = Button(text="Start Over", command= tutorial, width= 8)
	opt1.place(x = middle_x,y =  middle_y)
	
	
def hospital_stand():
	clear()
	intro = StringVar()
	intro.set("""You confront the COO about the board member and their inappropriate behavior. The COO tells you how important the board member's financial contributions are, and that if you plan on continuing this stand, you'll be asked to resign. You follow through with the investigation, and force the board member to resign. As a result, you yourself are fired, but atleast you know you have the stones to stand up to tyranny.""")
	newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 13, "bold"))
	newTitle.pack()
	opt1 = Button(text="Start Over", command= tutorial, width= 8)
	opt1.place(x = middle_x,y =  middle_y)
	
def level_two_retail():
	clear()
  
	
def level_one():
	clear()
	intro = StringVar()
	intro.set("""This is it. You've just graduated with an MBA from Northwestern University, and now it's time to head out into the world. You've gotten a handful of job offers, but the only ones piquing your interest are from Catheters United Healthcare, and The Mad Haber's Dashery. What's your choice going to be?""")
	prob = Message(top, textvariable = intro, justify= CENTER, width= 250, pady = 100, font = ("Helvetica", 13, "bold"))
	prob.pack()
	opt1 = Button(text="C.A.H", command= level_two_health, width = 8)#padx = button_pad_x, pady = button_pad_y)
	opt2 = Button(text="T.M.H.D", command= level_two_retail, width = 8)#padx = button_pad_x, pady =  button_pad_y)
	opt1.place(x = left_button_x,y =  split_button_y)
	opt2.place(x = right_button_x,y = split_button_y)
	
	
def level_two_health():
	clear()
	intro = StringVar()
	intro.set("""You've been hired by Catheters United Healthcare as a part of their new Project Management team. You're getting paid around $65,000 annually, which isn't bad for a fresh grad. You happen to be the deciding vote on whether to direct money for new wing attached to the hospital, or to funnel that money into a fund for possible raises.""")
	newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 13, "bold"))
	newTitle.pack()
	opt1 = Button(text="Lab", command= health_lab, width= 8)
	opt2 = Button(text="Raise", command= health_raise, width= 8)
	opt1.place(x = left_button_x,y =  split_button_y)
	opt2.place(x = right_button_x,y = split_button_y)
	
def health_lab():
	clear()
	intro = StringVar()
	intro.set("""The approval process for the wing is now well underway, and should be completed in the upcoming months. Despite not having any medical experience at all, they've asked you to start consulting on actual medical practice as well. A new patient has revealed to you that they have a severe allergy to ATP, an active ingredient. A doctor tells you the only common active ingredient in their treatement cycle is TCG. That's all the information given to you. Do you suggest the patient go through with this treatment?""")
	newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 13, "bold"))
	newTitle.pack()
	opt1 = Button(text="Yes", command= treat_yes, width= 8)
	opt2 = Button(text="No", command= treat_no, width= 8)
	opt1.place(x = left_button_x,y =  split_button_y)
	opt2.place(x = right_button_x,y = split_button_y)
	
def treat_yes():
	clear()
	intro = StringVar()
	intro.set("""The procedure went well for your patient, and they checked out 2 months after their treatment started. The new wing was approved, and money has been directed towards its construction. The hospital now must decide on whether the wing should be focused on newborn care, or to further research into finding a cure for Alzheimer's. The choice is yours.""")
	newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 14, "bold"))
	newTitle.pack()
	opt1 = Button(text="Babies", command= yes_babies, width= 8)
	opt2 = Button(text="Old People", command=yes_alz , width= 8)
	opt1.place(x = left_button_x,y =  split_button_y)
	opt2.place(x = right_button_x,y = split_button_y)

def treat_no():
	clear()
	intro = StringVar()
	intro.set("""You tell the patient to look for an alternate treatement plan for their safety. Unfortunately, they take that suggestion the wrong way, and decide to treat their illness with the magic cures that are essential oils. A few months after leaving your care, they succomb to their stupidity, and you resign from your position at the hospital out of internal conflict.""")
	newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 14, "bold"))
	newTitle.pack()
	opt1 = Button(text="Start Over", command= tutorial, width= 8)
	opt1.place(x = middle_x,y =  450)
	
def yes_babies():
	clear()
	intro = StringVar()
	intro.set("""You've chosen the utilitarian choice, as the babies have a much higher capacity to further improve the world than those old bastards. Because of your work, Catheters United has become the nationwide frontrunner in maternity care; allowing 99.7% of problematic births to have a happy ending. Unfortunately, your birth mother, whom you had recently connected with, has come down with an uncharacteristically agressive case of Alzheimer's, despite being only 37. You try your best to connect, but you only see the husk of a person, alongside a vision of what could have been.""")
	newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 13, "bold"))
	newTitle.pack()
	opt1 = Button(text="Start Over", command= tutorial, width= 8)
	opt1.place(x = middle_x,y =  450)
	
def yes_alz():
	clear()
	intro = StringVar()
	intro.set("""Ah, the sentimental choice. Although most Alzheimer's patients are near the end of their life, you chose to prioritize their care. 5-6 years after the completion of the wing, a significant breakthrough is made in the development of a cure. The researchers that made the discovery are awarded the 2026 Nobel Prize for Physiology, which brings even more money to the hospital. Unfortunately, their "cure" is estimated to cost $972,000 per patient, and thus is vastly out of reach for the common man. The work continues to find a more affordable cure, but the future is bleak. """)
	newTitle = Message(top, textvariable = intro, justify = CENTER, width = 275, pady = 100, font = ("Helvetica", 13, "bold"))
	newTitle.pack()
	opt1 = Button(text="Start Over", command= tutorial, width= 8)
	opt1.place(x = middle_x,y =  450)
	
	
b = Button(top, text = "Start Game", command = tutorial, width = 10)
b.place(x = middle_x, y = middle_y)


var = StringVar()
w = Label(top, textvariable = var, pady = 50, font = ("Helvetica", 16, "bold"))
var.set("The Business of Living")
w.pack()
top.mainloop()
