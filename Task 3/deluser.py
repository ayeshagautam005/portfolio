def delete_user(username):
    #open the file in read mode and read all lines into a list
    with open("passwd.txt", "r") as file:
        lines=file.readlines()

    #open the file in write mode 
    with open("passwd.txt", "w") as file:
        for line in lines:
            new_line=line.strip().split(':')

            #check if the username in the current line does not match the specified username
            if username!=new_line[0]:
                file.write(line)

            else:
                #print a message indicating that the user has been deleted
                print("User Deleted.")

def main():
    #prompt the user to enter the username to be deleted
    username=input("Enter username: ").strip()

    #open the file in read mode and read all users into a string
    with open("passwd.txt", "r") as file:
        users=file.read()

        #check if the specified username exists in the users string
        if username in users:
            delete_user(username) #call the delete_user function to delete the user
        else:
            print("User not found.")


if __name__=="__main__":  
    main()
