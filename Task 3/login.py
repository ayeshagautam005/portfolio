import codecs
import getpass

def decrypt_password(password):
    decrypted_password=codecs.decode(password, "rot_13")
    return decrypted_password

def login_user(username, password):
  
    #open the file in read mode
    with open("passwd.txt", "r") as file:
        for line in file:
            new_line=line.strip().split(':')

            #check if the username and password match the corresponding fields in the line
            if username==new_line[0]:
                decrypted_password=decrypt_password(new_line[2].strip())
                print("decrypted password:", decrypted_password)
                
                #check if the password matches
                if password==decrypted_password:
                    return True
        return False


def main():
    #prompt the user to enter the username
    username=input("User: ").strip()

    #prompt the user to enter the password securely
    password=getpass.getpass("Password:").strip()
    
    #check if authenctication is successful and the stored password matches the entered password
    if login_user(username, password):
        print("Access granted.")
    else:
        print("Access denied.")

if __name__=="__main__":
    main()