import model

def login():
    username = input("Please enter your username: ")
    user_info = model.session.query(model.UserData).filter_by(username=username).first()
    password = input("Please enter your password: ")  

    if password != user_info.password:
        print("Incorrect credentials.")
        return False, None

    return True, user_info

