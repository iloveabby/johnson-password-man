"""
this python script is a extremly crude password mananger
i'm hoping to eventualy make a login system
Aswell as a encrypted passwordfile
plese dont kill me for this I'm just starting out.


"""
while True:
    user = input('r to read passwords w to save, x to break')

    if user == 'w':
        passdir = input('type dir to save passwords include filename too.')
        password = open(passdir, 'a')
        account = str(input('type account'))
        pas = str(input('type pass'))
        password.write(account )
        password.write('\n')
        password.write(pas)
        password.close()
    elif user == 'r':
        dir = input('please type the path and the file')
        passr = open(dir, 'r').read()
        print (passr)
        
    elif user == 'x':
        break
