import login
import model

def register():
    print('-------------------------------------------------')
    print('Press 1 to create account or press 2 to login:')
    print('-------------------------------------------------')

    menuInput = int(input())

    if int(menuInput) == 1:
        print('\nTime to create a username and password!\n')
        username = input("Create Username: ")
        password = input("Create Password ")
        userinfo = model.UserData(username = username, password = password, wins = 0, losses = 0)
        model.session.add(userinfo)
        model.session.commit()
        print('\nLets login: \n')
        return login.login()

    if int(menuInput) == 2:
        status, user = login.login()
        if status == True:
            print(f"You are now logged in {user.username}!")
            return True, user
        else:
            return False