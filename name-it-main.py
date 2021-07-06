import os 
import random 
import csv 
from tkinter import *

#Audio Loop
import pygame 
pygame.mixer.init() 
pygame.mixer.music.load("hailtothechiefRemix.wav")
pygame.mixer.music.play(loops=-1, start=0.0)
global CategoryFileName 
global num CategoryFileName = '.\presidents\president.txt' 
datadirectory =
'.\presidents\\' labelfont = ('Legacy', 20, "bold")

images = [] 
names = [] 
info = []

#Function which changes the current image and resets the textbox 
def FillImage():
  global num 
  global ImageCanvas 
  global Image 
  global filename 
  global info 
  global UserInput 
  global datadirectory 

  UserInput.delete(0,END) 
  num = random.randrange(len(images)) 
  Response.set(info[num])
  ScoreText.set(score) 
  myimagefile = datadirectory + images[num] 
  filename = PhotoImage(file = myimagefile) 
  ImageCanvas.itemconfig(Image,image= filename)

#Separator of each parameter using commas and rows
def ReadData(): 
  global num 
  global images 
  global names 
  global info 
  images = [] 
  names = [] 
  info = [] 

  with open(CategoryFileName) as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',') 
    for row in readCSV: 
      name = row[0] 
      file = row[1] 
      hint = row[2]
      names.append(name) 
      images.append(file) 
      info.append(hint) #Randomly generates a row to be chosen in the text file 
      num = random.randrange(len(images))

# Sample setups for quizzes --TODO: Recognize .txt files from quiz directory
def PresidentCategory():
  global CategoryFileName 
  global datadirectory 
  datadirectory = '.\presidents\\' 
  CategoryFileName = datadirectory + 'president.txt' 
  ReadData() 
  FillImage()

def ComputerCategory():
  global CategoryFileName 
  global datadirectory 
  datadirectory = '.\computerparts\\' 
  CategoryFileName = datadirectory + 'computerparts.txt' 
  ReadData() 
  FillImage()

def ElementCategory():
  global CategoryFileName 
  global datadirectory 
  datadirectory = '.\elements\\' 
  CategoryFileName = datadirectory + 'elements.txt' 
  ReadData() 
  FillImage()

def ColorCategory():
  global CategoryFileName 
  global datadirectory 
  datadirectory = '.\colors\\' 
  CategoryFileName = datadirectory + 'colors.txt' 
  ReadData() 
  FillImage()

#Creates GUIs
def Initialization(): 
  global labelfont 
  global ImageCanvas 
  global Image 
  global filename 
  global ScoreText
  num = random.randrange(len(images))
  MenuFrame = Frame(top) 
  PresidentButton = Button(MenuFrame,text='Presidents',command=PresidentCategory) 
  ComputersButton = Button(MenuFrame,text='Computer Parts',command=ComputerCategory) 
  ElementButton = Button(MenuFrame,text='Elements',command=ElementCategory) 
  ColorsButton = Button(MenuFrame,text='Colors',command=ColorCategory)
  ColorsButton.pack(side = RIGHT,anchor = CENTER) 
  PresidentButton.pack(side = LEFT,anchor = CENTER) 
  ComputersButton.pack(side = RIGHT,anchor = CENTER) 
  ElementButton.pack(anchor = CENTER) 
  MenuFrame.pack(side = TOP,anchor = CENTER)
  Title = StringVar() 
  Title.set("Name It!") 
  TitleLabel = Label(top,textvariable = Title)
  TitleLabel.config(bg="white", fg="black") 
  TitleLabel.config(font=labelfont) 
  TitleLabel.config(height=3, width=20) 
  TitleLabel.pack(side = TOP, expand = YES, fill = X) 
  UserInput.config(bg="white")
  UserInput.pack(side = BOTTOM)
  labelfont = ('Legacy', 10, "bold")
  Response.set(info[num]) 
  ResponseLabel = Label(top,textvariable = Response)
  ResponseLabel.config(bg="white", fg="black") 
  ResponseLabel.config(font=labelfont)
  ResponseLabel.config(height=1, width=20)
  ImageCanvas = Canvas(top, height = 200, width = 200) 
  myimagefile = './presidents/' + images[num]
  filename = PhotoImage(file = myimagefile) 
  Image = ImageCanvas.create_image(100,100,anchor = CENTER, image = filename) 
  ResponseLabel.pack(side = TOP, expand = YES, fill = X)
  skipframe = Frame(top) 
  skiplabel = Label(skipframe,text=" ") 
  skiplabel.pack(side = TOP) 
  SkipButton = Button(skipframe,text="Skip",command = FillImage,width=4) 
  SkipButton.pack(side = TOP)
  skipframe.pack(side = LEFT)
  scoreframe = Frame(top) 
  scorelabel = Label(scoreframe,text="Score:") 
  scorelabel.pack(side = TOP)
  ScoreText = StringVar() 
  ScoreText.set(score) 
  ScoreButton = Button(scoreframe,textvariable=ScoreText,width=4) 
  ScoreButton.pack(side = TOP) 
  scoreframe.pack(side = RIGHT)
  ImageCanvas.pack(side = TOP) 
  top.mainloop()

#Verifies the user's textbox input and initiates FillImage function 
def ValidateInput(userinput):
  global score 
  #match of entire name string (presidents name) 
  fullmatch = re.fullmatch(userinput,names[num], re.IGNORECASE) 
  if (fullmatch):
    Response.set("Correct!") 
    score = score + 1 
    FillImage() 
  else:
    #name_broken seperates strings by spaces and checks for correlation in strings
    name_broken = names[num].split() 
  for nameBrokenStr in name_broken:
    if (re.fullmatch(userinput,nameBrokenStr,re.IGNORECASE)):
      Response.set("Correct!") score = score + 1 
      FillImage()

  #This function takes the textbox input and stores it in a variable
  def GetInput(event):
    GuessInput = event.widget.get() 
    ValidateInput(GuessInput)

score = 0
#Window Definition
top = Tk() 
top.resizable(0,0) 
top.title("Name It!") 
UserInput = Entry(top, bd = 10)
UserInput.bind("<Return>", GetInput)
#Definition of String Variable used to change the ResponseLabel widget
Response = StringVar()
ReadData() 
Initialization() 
FillImage()
