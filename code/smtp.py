

import smtplib
import getpass

def Main():
    
    print("\n\n*************************welcome************************\n")
    print("\nWelcom to Email Service \n")
    print("Enter your login details - \n")
    
    
    gmail_user = input("\n\nUserName : ")
    gmail_password = getpass.getpass("Password : ")

    try:
        
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        
        print("\n\nConnection established ")
        
        server.ehlo()
        server.login(gmail_user, gmail_password)
        
        print("\n\nYou have Successfully logged in your account ",gmail_user)
   
    except Exception as e:
        
        print("\n\nError!!! in Connection ")
        print(e)
        
        exit(0)
    
    sent_from = gmail_user

    i = int(input("\n\nEnter no. of recipients - "))

    print("\n\nEnter Recipients Email Addressess - \n")

    to = []

    for k in range(i):
        
        to.append(input())
        print()


    subject = input("\n\nPlease Type in Subject of The Mail - ")

    print("\n\nType in Your Message (Type in EOF to FINISH)\n\n")


    message=[]

    while True:
        
        msg = input()
        
        if msg.upper() == 'EOF' :
            
            break
        
        else :

            message.append(msg)

    print("\n\nMessege is Ready for Delivery\n\n ")
    
    body = '\n'.join(message)

    email_text = """From:%s  
To:%s 
Subject:%s
%s
"""%(sent_from, ", ".join(to), subject, body)

    try:
        
        print("\n\nEmail sending is  in process  - \n  ")
        
        server.sendmail(sent_from, to, email_text)
        server.close()
    
    except Exception as e:
        
        print('\nSomething went wrong...',e)
   
    else:
        
        print("\nMessage Delivered to - \n")
        
        for i in to:
            
            print(i)
            print()
        
        
        print("\n\n**********************Exiting********************\n\n")
        print("\n\nThanks For using Mail Service \n\n")

if __name__ == "__main__":
    
    Main()


