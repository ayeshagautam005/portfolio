import getpass
import codecs

def decrypt_password(password):
    decrypted_password=codecs.decode(password, "rot_13")
    return decrypted_password

def change_passwd(username, new_passwd):

    #open the file in read mode and read all the lines into a list
    with open("passwd.txt", "r") as file:
        lines=file.readlines()
    
    user_found=False #Flag to track if the specified username  is found

    #open the file in write mode
    with open("passwd.txt", "w") as file:
        for line in lines:
            new_line=line.strip().split(':')

            #check if the username matches the first field in the line
            if username==new_line[0]:
                #write the updated line with new password to the file
                new_passwd_encoded=codecs.encode(new_passwd, "rot_13") #encoded new password
                file.write(f"{username}:{line.split(':')[1]}:{new_passwd_encoded}\n")
                user_found=True #set the flag to True if the username is found.
            else:
                #write the unchanged line to the file
                file.write(line)
    
    
    #print a message whether the password was changed or the user not found
    if user_found:    
        print("Password changed.")
    else:
        print("User not found.")

def main():
    #prompt the user to enter username, current password, new password and confirm password
    username=input("User: ").strip()



    with open("passwd.txt", "r") as file:
        for line in file:
            new_line=line.strip().split(':')
            if new_line[0] ==username:
                stored_passwd=decrypt_password(new_line[2])
                
                #prompt the user to enter the current password securely
                current_passwd_encoded=getpass.getpass("Current Password: ").strip()
                current_passwd=decrypt_password(codecs.encode(current_passwd_encoded,"rot_13")) #decode the current password
                print("dee", current_passwd)
                
                #check if current password matches the stored password
                if stored_passwd==current_passwd:
                    new_passwd=getpass.getpass("New Password: ").strip()
                    confirm_passwd=getpass.getpass("Confirm Password: ").strip()
                    
                    #check if the new password is different from the current password
                    if new_passwd!=current_passwd:
                        if new_passwd==confirm_passwd:
                            change_passwd(username, new_passwd)
                        else:
                           print("Passwords do not match")
                    else:
                        print("New password shouldn't be same as current password")
                else:
                    print("Incorrect current password.")
    print("User not found.")
        
if __name__=="__main__":
    main()
