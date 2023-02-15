from tabnanny import check


def script():
    check="0"
   
    while check=="0":
        generator()
        check= input('''Press 0 to restart the program or press any key to end it ''')
    
    


print ("Remember to follow my on github (shaowastaken) and contact me on telegram @Shaowastaken if you need anything")

def generator():
    import os, random, string

    charsamount = int (input (''' Insert the amount of character required to create your password '''))


    chars = string.ascii_letters + string.digits + '!@#$%^&*()'
    os.urandom(64)

    checkdoc="n"

    password= ''.join([ random.choice(chars) for i in range (charsamount)])

    print (password)
    print ("Remember to follow my on github (shaowastaken) and contact me on telegram @Shaowastaken if you need anything")

    lines=['', password]

    checkdoc="n"
       
    while checkdoc=="n": 
    
            checkdoc= input('''Press y to save it on generatedpassword.txt ( you can find it in the folder where the exe is) or press any key to skip this step ''')
            if checkdoc=="y" or checkdoc=="Y":
                with open('passwordgeneretad.txt', 'a') as f:
                    f.write('\n'.join(lines))
     
   


script()