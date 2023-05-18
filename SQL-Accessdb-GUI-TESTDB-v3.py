from sre_parse import FLAGS
from sys import flags
import pyodbc
import pandas as pd
import tkinter as tk
from tkinter import DISABLED, ttk
from tkinter import filedialog
from tkcalendar import Calendar

import warnings
# Ignore future warnings:
warnings.simplefilter('ignore')

''' Constants'''
# Constants used for the GUI colors
Blue = '#87B7E1'
Red = '#D0281A'
Grey = "#D6DADE"

root=tk.Tk(screenName="Ian's window")
root.config(background = Grey)

frame2 = tk.Frame(root, bg = Grey, pady = 10, padx = 10)
frame2.pack()    # Need this to enable the frame

frame = tk.Frame(root, bg = Grey, pady = 10, padx = 10)
frame.pack()    # Need this to enable the frame

cal = Calendar(frame)

# Attempt to change tkinter theme
style = ttk.Style(root)
style.theme_use('classic')  # I like the classic theme

# declaring string variable for the file path and answers to questions
connlist = [0] 
nameList = [0]  
fileList = [0] 

# creating the tuple for entry into Access file
InpTuple = [] 
entry1var = tk.IntVar()
entry2var = tk.StringVar()
entry2var.set("Name?")
entry3var = 0
entry4var = tk.StringVar()
numlist = []
namelist = []
dblist = []

dfentry2 = []
dfentry3 = []

Options = ['Blue', 'Ian', 'Xylas']

File = "entry2-3.csv"
File_Blue = "entry2-3-Blue.csv"
File_Ian = "entry2-3-Ian.csv"
File_Xy = "entry2-3-Xy.csv"
flag = 0

# grab data from csv file--------------------------------------------------------------
if flag == 1:
    CSV = File_Blue
    print("CSV-BLUEEE*__-")
elif flag == 2:
    CSV = File_Ian
elif flag == 3:
    CSV = File_Xy
else:
    CSV = File

df = pd.read_csv(CSV)
# convert the values of the dataframe to entries in a list
dflist = df.values.tolist()
for i in dflist[-1]:
    # print(f'last entry = {i}')
    # make last value = entry3var
    entry3var = i
    if entry3var == str:
        entry3var = '0'  # 0 is a string because later I convert it to an integer

# print(entry3var)
# grab data from csv file--------------------------------------------------------------

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "c:\\",
                                          title = "Select a File",
                                          filetypes = (("Access files",
                                                        "*.accdb*"),
                                                        ))
    label_file_explorer.configure(text="File Opened: "+filename)
    nameList.append(filename)

def submit():
    loadfile = str(nameList[-1])
    print("Your Microsoft Access file path is : " + loadfile)
    fileList.append(loadfile)

    FILE = fileList[-1]
    conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};' + f'DBQ={FILE};')
    # r means raw string...
    connlist.append(conn)

    cursor = conn.cursor()
    print('\n B3f0R insertion \n')
    cursor.execute('SELECT * FROM TESTDB')
    for row in cursor.fetchall():
        print (row)
        dblist.append(row)


def entry1():   # Index number (unique)
    X = entry1var.get()
    print(f'You entered: {X}')

    InpTuple.append(X)
   

def entry2():
    X = entry2var.get()
    print(f'You entered: {X}') 

    if X == 'Blue':
        File = File_Blue
        flag = 1
    if X == 'Ian':
        File = File_Ian
        flag = 2
    if X == 'Xylas':
        File = File_Xy
        flag = 3
        
    # ===============================
    if flag == 1:
        CSV = File_Blue
    elif flag == 2:
        CSV = File_Ian
    elif flag == 3:
        CSV = File_Xy
    else:
        CSV = File

    df = pd.read_csv(CSV)
    # convert the values of the dataframe to entries in a list
    dflist = df.values.tolist()
    for i in dflist[-1]:
        # print(f'last entry = {i}')
        # make last value = entry3var
        entry3var = i
        if entry3var == str:
            entry3var = '0'  # 0 is a string because later I convert it to an integer


    
    # appending data to excel 
    dfentry2.append(X)
    InpTuple.append(X)
    
    # appending data to excel 
    dfentry2df = pd.DataFrame(dfentry2)
    dfentry2df.to_csv(File, mode='a')   # mode = 'a' == append

    X = entry3var
    X = int(X)
    X = X + 1

    InpTuple.append(X) 
    # appending data to excel 
    dfentry3.append(X)

    # appending data to excel 
    dfentry3df = pd.DataFrame(dfentry3)
    dfentry3df.to_csv(File, mode='a')   # mode = 'a' == append



def entry4():   # Needs a date
    X = entry4var.get()
    print(f'You entered: {X}')  
    
    InpTuple.append(X) 

def entry5():   # Needs a date
    X = cal.get_date()
    print(f'You entered: {X}')  
    
    InpTuple.append(X) 

def maincode():
    conn = connlist[-1] # test to see if this works...
    cursor = conn.cursor()
    print('\n B3f0R insertion \n')
    cursor.execute('SELECT * FROM TESTDB')
    for row in cursor.fetchall():
        print (row)
    
    inptup = tuple(InpTuple)
    cursor.execute('INSERT INTO TESTDB VALUES (?,?,?,?,?)', inptup)

    print('\n After insertion: \n')
    cursor.execute('SELECT * FROM TESTDB')
    for row in cursor.fetchall():
        print (row)

    print('\n \n If you get an error, make sure you put in a UNIQUE, unnused index number. \n You will have to restart the application. \n \n')


    conn.commit() 
    conn.close()


#%% Create Buttons, entry boxes, etc. (widgets)

# Create a File Explorer label
label_file_explorer = tk.Label(frame2, text = "Find Your Access File", fg = "black", bg = Blue)
button_explore = tk.Button(frame2, text = "Browse Files", command = browseFiles)
# Button that will call the Submit function for the file browser
Enter = tk.Button(frame2, text = 'Enter Microsoft Access File', command = submit)

entry1entry =  tk.Entry(frame, textvariable = entry1var, font = ('calibre',10,'normal'), bg="white", fg = 'black')
entry1button =  tk.Button(frame, text = 'Enter unique index number', command = entry1)

# entry2entry =  tk.Entry(frame, textvariable = entry2var, font = ('calibre',10,'normal'), bg="white", fg = 'black')
entry2entry = tk.OptionMenu(frame, entry2var, *Options)
entry2button =  tk.Button(frame, text = 'Enter Your name', command = entry2)

entry4entry =  tk.Entry(frame, textvariable = entry4var, font = ('calibre',10,'normal'), bg="white", fg = 'black')
entry4button =  tk.Button(frame, text = 'Name of favorite state', command = entry4)

entry5button = tk.Button(frame, text = 'Enter a date', command = entry5)

# Main code buttons
RunCode = tk.Button(root, text = "Run Application", command = maincode, bg = Blue)


#%% Add widgets to root window


label_file_explorer.grid(row = 0, column = 0, ipady= 10)
button_explore.grid(row = 1, column = 0)
Enter.grid(row = 2, column = 0)

entry1entry.grid(row = 0, column = 0)
entry1button.grid(row = 0, column = 1)

entry2entry.grid(row = 1, column = 0)
entry2button.grid(row = 1, column = 1)

# entry3entry.grid(row = 2, column = 0)
# entry3button.grid(row = 2, column = 1)

entry4entry.grid(row = 3, column = 0)
entry4button.grid(row = 3, column = 1)

cal.grid(row = 4, column = 0)   
entry5button.grid(row = 5, column = 0) 

RunCode.pack()

root.mainloop()