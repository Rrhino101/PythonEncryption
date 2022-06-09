import os # This is the os module that is being imported, this shouldn't be changed because changing it may cause the program not to work
import random # This is the random module that is being imported, this shouldn't be changed because changing it may cause the program not to work
from json import dumps,loads # this imports certain functions from the json module,  this shouldn't be changed because changing it may cause the program not to work
from time import sleep # this imports certain fuctions from the time module,  this shouldn't be changed because changing it may cause the program not to work
##
Fruity_Goodness = {'Banana': "8 9 6 6", 'Apple': "4 1 2 3",'Orange': "7 8 9 5",'Pineapple': "5 8 9 3",'Apricot': "8 3 9 5",'Plum': "7 6 2 1",'Blackberry': "1 5 3 8",'Cherry': "4 9 7 7",'Coconut': "6 2 9 4",'Coffee Bean': "1 7 3 2",'Guava': "9 6 2 2",'Custard Apple': "5 3 6 7"}# The Dictionary that holds all of the usernames and passwords
NewMessage = []#I need to read each byte, apply the cipher and enter into this array   
OriginalMessage = [] # this is where the file will be saved

def spreadtotext(name): # converts spreadsheet to text, this is the name of the users file asigned to thisfile
    base = os.path.splitext(name)[0] #this takes away the file's suffix
    changefile = os.rename(name, base + ".txt") # this changes the files suffix
    changefile
    return base

def texttospread(name): # this converts the text to a spreadsheet, # asigns the file name to thisfile
    base = os.path.splitext(name)[0] # separates the file's suffix
    suffix = input("Whats the original extension of the file, without the dot? (e.g xlsx ):")
    os.rename(name, base +"."+suffix)# renames the file
    
def Dict(Fruity_Goodness):# this def is focused on the dictionary
    Username = random.choice(list(Fruity_Goodness)) # This randomly selects the username
    print("This is your username for this file:",Username)#This line gives the user a username
    Password = str(Username) #in order to get the pin from the dictionary instead of the username
    KEY = Algorithm(Fruity_Goodness,Password)# This calls up the algorithm def
    return KEY,Password,Fruity_Goodness [str(Password)]



def Dict1(Fruity_Goodness,KEY2):# this dictionary verifies the usernames
    try:
        Password = input("Enter a your username here: ")# This gets the username from the user
        verify = Password in Fruity_Goodness # it will return either a True or False
        if verify == True:# This makes sure if "password" is the same as the "username" given
            KEY = Algorithm(Fruity_Goodness,Password)# This calls up the algorithm def
            KEY = int(KEY)# converts key to an integer
            if KEY2 == KEY: # checking if the username is correct by verifying the keys so it can decrypt
                return KEY # returns Key
            else:
                print("That isn't the correct Username")
                Dict1(Fruity_Goodness,KEY2) # it repeates the function
        else:# If incorrect then it doesn't give the user the password
            print ("That isn't the user name you have been given")
            Dict1(Fruity_Goodness,KEY2) # repeates the define function
    except TypeError or UnboundLocalError:
        print ("Could you enter your username again please")

        
def Algorithm(Fruity_Goodness,Password):# This is where the algorithm is held
    key1,key2,key3,key4 = Fruity_Goodness [str(Password)].split(" ")# This asigns the password to 4"keys"
    key1 = int(key1) # Turning the string of key1 to an integer
    key2 = int(key2)# Turning the string of key2 to an integer
    key3 = int(key3)# Turning the string of key3 to an integer
    key4 = int(key4)# Turning the string of key4 to an integer
    KEY = key1+key2*key3//key4 #The actual algorithm  
    return KEY # Returns the key

   
def Get_Name():
    try:
        name = input("What is the full name of the file? (extention included):") # the name of the file
        name = spreadtotext(name) # runs the definition that changes the spreadsheet to text
        file = open(name+".txt", "r+b")#rb means that it will read bytes
        readfile = file.read() # asigns the file to readfile
        file.close() # closes the file
        KEY,Username,Password = Dict(Fruity_Goodness)#This will be using Caesar cipher
        Encrypt(readfile,name,KEY)
    except FileNotFoundError:
        print ("Cannot find specified file")
        Get_Name()

def Encrypt(readfile,name,KEY):    #########THIS IS ENCRYPTING
    for each in range (len(readfile)):
        what =(readfile[each])# reads each byte
        if len(readfile) == range(0,KEY): # checks if its between 0 and the key
            what = what + KEY # applies cipher
            NewMessage.append(what)# then appends to array
        else: # if the cipher isn't applied
            NewMessage.append(what)# appends to array
    Saving(name,KEY)

def Saving(name,KEY):    #########THIS IS Saving
    Saving = open(name+'.txt','w') # creates the file that is saved
    Saving.write(str(KEY)) # converts it to a string
    Saving.write("\n")# this will be used later to separate the key and the file
    ## trying json
    programmedata = dumps(NewMessage) # asigns the file to program data
    Saving.write(programmedata) # writes the file
    Saving.close() # closes the file and it has been saved


def Loading():#########THIS IS Loading
    try:
        name = input("What is the full name of the file? (extention included, which should be .txt):") # the name of the file
        Loading = open(name,'r') # opens the file so it can be decrypted
        KEY2 = Loading.readline()## you can save the password so you check it against the dictionary and get the correct Key from the algorithm
        programmedata = Loading.read()
        NewMessage2 = loads(programmedata)# separates the key and the file
        Loading.close() # closes the file
        KEY2 = int(KEY2) # converts the key to an integer
        KEY = Dict1(Fruity_Goodness,KEY2) # initiates checking the key
        Decrypt(NewMessage2,name,KEY) #runs the decrypt definintion
    except FileNotFoundError:
        print ("Cannot find specified file")
        Loading()

###########THIS IS Fixing the array
##TempMessage = [] # A temporary array
##for every in range(len(NewMessage2)): # this gets all the bytes
##    num =(NewMessage2[every])# reads each byte
##    print("The num that is being worked on",num)
##    sleep(2)
##    num = num.split(", ")
##    print ("Split num",num)
##    sleep(2)
##    verify = isinstance(num, int)
##    print (verify)
##    if verify == True:
##        TempMessage.append(num)# splits each byte and appends it to the temporary array


def Decrypt(NewMessage2,name,KEY):#########THIS IS DECRYPTING, The same as encrypting but in reverse
    try:
        for each2 in range (len(NewMessage2)): # this gets all the bytes
          what =(NewMessage2[each2]) # reads each byte
          if len(NewMessage2) == range(1,KEY): # checks if its between 0 and the key
              what = what - KEY # reverts cipher to original 
              OriginalMessage.append(what)# appends to array
          else: # if the byte isnt affected
              OriginalMessage.append(what)# appends to array
        Changing_Back(name)
    except TypeError:
        Dict1(Fruity_Goodness,KEY)

def Changing_Back(name):
    file2 = open(name, "w+b") # this creates the new file
    file2.write(bytes(OriginalMessage)) # this writes it to a file
    file2.close() # closes the file
    texttospread(name) # this converts it back
  
def Main(): # This is the fuction that starts the program, it takes in your choices and then decides wether to encrypt or decrypt depending on your choices
    choice = input("Would you like to Encrypt or Decrypt a file? e/d: ").lower() # This allows the user to enter their choices, you can edit this by changing the green words inside the speach marks to make it say something else 
    if choice == "encrypt" or choice == 'e': # Here it states that choice has to either be encrypt or e to proceed here, you can change the green words inside the words inside the speach marks to change what it accepts or you could add an or then more speach marks to accept another input  
        Get_Name() # Once it goes into this it will start to aquire your file's details, if you changed the name of the define function then you'll need to change it here 
        choice = input("Would you like to encrypt again? Y/N: ").lower() # This allows the user to enter their choices, you can edit this by changing the green words inside the speach marks to make it say something else
        if choice == "y" or choice == "yes": # Here it states that choice has to either be encrypt or e to proceed here, you can change the green words inside the words inside the speach marks to change what it accepts or you could add an or then more speach marks to accept another input
            Get_Name()# Once it goes into this it will start to aquire a different file's details, if you changed the name of the define function then you'll need to change it here
        else :# It will only go here if the choice is anything but y or yes
            exit()# This forces the program to exit, you can change this to break, to just stop the program or you can change it to main(), this will allow it to start the program from the begining
    elif choice == "decrypt" or "d": # Here it states that choice has to either be decrypt or d to proceed here, you can change the green words inside the words inside the speach marks to change what it accepts or you could add an or then more speach marks to accept another input
        Loading()# Once it goes into this it will start to aquire your file's details, if you changed the name of the define function then you'll need to change it here
        choice = input("Would you like to decrypt again? Y/N: ")
        if choice == "Y":
            Loading()
        else :
            exit()
    else:
        Main()
Main()
