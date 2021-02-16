"""
This is the 3rd version of this script.  I've made a some quality of life changes. 
I'm still working on the enryption system.It's a lot harder than I though to set up
Over all nothing much has changed. Just a litle less bloat. I might port this script
to bash or lua for more light weight usage.
"""



import os.path 
loginfile = os.path.exists('login.txt') 
if loginfile == False: #this block checks if you have a login file
    login = open('login.txt','w')    
    login.write(input('You do not have a login password.Type your login passowrd'))
    login.close()

login = open('login.txt','r').read()
userlogin = input('Type your login password') #checks if  you login matches with the file

if userlogin != login: #if it's wrong this block is excuted and closes the program
    print('password wrong')
    exit()
passdir = input('Type the filepath and press enter.')

while True:
    user = input('r to read passwords w to save')
    if user == 'w':# this section is excucted if the user presses w and writes to the file 
        password = open(passdir, 'a')
        password.write('\n')
        password.write(str(input('Please type the service')))
        password.write('\n')
        password.write(str(input('Please type acount name')))
        password.write('\n')
        password.write(str(input('type your password')))
        password.close()
    elif user == 'r': # this is the same as before but with r it reads the file and displays it
        passr = open(passdir, 'r').read()
        print(passr)
    else: # this stops the loop and breaks the program
        break

