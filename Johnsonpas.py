"""
this python script is a extremly crude password mananger
i'm hoping to eventualy make a login system
Aswell as a encrypted passwordfile
plese dont kill me for this I'm just starting out.


"""
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
        print (passr)
        
    elif user == 'x':
        break
