
def register():
    print('-------------------------------------------------')
    print('Press 1 to create account or press 2 to login:')
    print('-------------------------------------------------')
 
    menuInput = int(input())
  
    if int(menuInput) == 1:
        print('\nTime to create a username and password!\n')
        username = input("Create Username: ")
        password = input("Create Password ")
        file = open("userdata.txt","a")
        file.write(username)
        file.write(" ")
        file.write(password)
        file.write("\n")
        file.close()
        print('\nLets login: \n')
        return login()

    if int(menuInput) == 2:
        if login():
            print("You are now logged in...")
            return True
        else:
            return False