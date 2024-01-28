import adduser, deluser, login, changepasswd
def main():
    while True:

        #display the menu options
        print("1. Add User")
        print("2. Delete User")
        print("3. Change Password")
        print("4. Login")
        print("5. Exit")

        #prompt the user to enter their choice
        choice =input("Enter your choice (1-5):").strip()

        if choice=='1':
             adduser.main()
        elif choice=='2':
            deluser.main()
        elif choice=='3':
            changepasswd.main()
        elif choice=='4':
            login.main()
        elif choice=='5':
            print("Exit")
            break
        elif choice=='':
            continue
 


if __name__=="__main__":
    main()