"""
This is the Second version of this script. I've added a basic login system. It's nothing impressive.
I'm hoping to optimize this soon. I think I can make it a little more light weight.
I dont like bloat. Maybe someday I will set up a encryption system.

"""



import os.path
loginfile = os.path.exists('login.txt')
if loginfile == False:
    login = open('login.txt','w')
    login.write(input('You do not have a login password.Type your login passowrd'))
    login.close()

login = open('login.txt','r').read()
userlogin = input('Type your login password')

if userlogin != login:
    print('password wrong')
    exit() 
while True:
    user = input('r to read passwords w to save, x to break')
    if user == 'w':
        passdir = input('Type the filepath and press enter. .')
        password = open(passdir, 'a')
        account = str(input('type your account name'))
        pas = str(input('type your password'))
        password.write(account )
        password.write('\n')
        password.write(pas)
        password.close()
    elif user == 'r':
        dir = input('Please type the the file path of the passwordfile.')
        passr = open(dir, 'r').read()
        print(passr)
    elif user == 'x':
        break

