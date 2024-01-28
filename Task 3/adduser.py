import codecs

def add_user(username, realname, password):

    #open the passwd.txt file in append mode 
    with open("passwd.txt", "a") as file:
        file.write(f"{username}:{realname}:{password} \n") #write the new user information
        
        #close the file
        file.close()

        #print a message indicating that the user has been created
        print("User Created.")


def main():
    #prompt the user to enter new user information
    username=input("Enter new username: ").strip()
    realname=input("Enter real name: ").strip()
    password=input("Enter password: ").strip()

    password=codecs.encode(password, "rot_13")
    #open the file in read mode
    with open("passwd.txt", "r") as file:
        users=file.read()

        #check if the username already exists in the file
        if username in users:
            print("Cannot add. Most likely username already exists.")
        #if the username doesn't exist, call the add_user function to add the new user
        else:
            add_user(username, realname, password)

if __name__=="__main__":
    main()