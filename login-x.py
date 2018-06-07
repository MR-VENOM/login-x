#coded by mr-venom 
#all right reserved
from os import system
from os import path
import time
RED, WHITE, CYAN, GREEN, END = '\033[91m', '\33[46m', '\033[36m', '\033[1;32m', '\033[0m'
def startup():
    if path.isfile(".credits.txt") == False:
        system("figlet login-x")
        system('> .credits.txt')
        x = input('enter new password : ').format(GREEN , END)
        file = open(".credits.txt" , 'w')
        file.write(x)
        file.close()
        exit()
          
def login():
    while True:
        try:
            x = input("enter password :").format(GREEN , END)
            file =open(".credits.txt" , "r")
            y = file.read()
            file.close()
            if x == y:
                system('figlet access')
                system('figlet granted')
                break
            else:
                system('figlet access')
                system('figlet denied')
        except:
            system('figlet permission')
            system('figlet denied')
            continue        
startup()
login()
