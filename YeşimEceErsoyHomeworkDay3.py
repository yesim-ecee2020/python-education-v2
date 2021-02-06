#Yeşim Ece Ersoy Homework Day 3

#Question1
username = ['myusername']
password = ['mypassword']

user_name = input("Your username: ")
passwords = input("Your Password: ") 

if user_name in username and passwords in password:
    print("You are logged in...")
else:
    print("Invalid login!")
    
    
#Question2
users = {
    "MyName1": "Password1",
    "MyName2": "Password2",
    "MyName3": "Password3" 
}
while True:
    username = input("User Name: ")
    password = input("Password: ")
if username in users.keys() and password == users[users] :
        print("You are logged in...")
        
        
else:
        print("Invalid Login!")   
