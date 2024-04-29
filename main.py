import mysql.connector
import random


User = ''
Password = ''

program = True


#We use this code to find out if a user is already made in the server
def target(target):
    target_found = False
    try:
        connector = mysql.connector.connect( user = 'root', password = 'Emanuel625.', database = 'example' )

        cursor = connector.cursor()
        cursor.execute('SELECT user FROM mysql.user')
        users = cursor.fetchall()

        for user in users:
            if str(user[0]) == target:
                print("Found target")
                target_found = True

        cursor.close()
        connector.close()
        return target_found
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
def generate_access_number():
    
    try:
        temp_access_number = random.randrange(10000,99999)

        connector = mysql.connector.connect( user = 'root', password = 'Emanuel625.', database = 'example')

        cursor = connector.cursor()
        cursor.execute("SELECT Access_Number FROM account")
        Access_number = cursor.fetchall()

        for number in Access_number:
           print(number[0])
           if number[0] == temp_access_number:
             generate_access_number()

        cursor.close()
        connector.close()
        print(temp_access_number)
        return temp_access_number
    except mysql.connector.error as err:
        print(F"Error: {err}")


#Function that will ask for the username and password 
def login():
    global user
    global Password
    username = input("Please enter your Username:\n")
    password = input("Please enter your Password:\n")
    avaliable = target(username)
    if avaliable == False:
        print('Please try again')
    else:
        user = username
        Password = password
        print("Login Successfull")


def create_user():
    desired_username = input("Please enter your Username:\n")
    desired_password = input("Please input your Password:\n")

    avaliable = not target(desired_username)

    if avaliable == False:
        print("Username is already taken")
        create_user()
    else:
        try:
            connector = mysql.connector.connect(user = 'root', password = 'Emanuel625.', database = 'example')

            cursor = connector.cursor()
            cursor.execute(f"CREATE USER'{desired_username}'@'localhost' IDENTIFIED BY '{desired_password}'")
            print("User Created")


            starting_value = float(input("How much is in your starting acount?\n"))
            #The isinstance allows us to check if the value is that type of value
            while(isinstance(starting_value, float) == False):
                starting_value = float(input("Please insert a decimal placed number (Ex: 100.00, 200.00)\n"))
            

            cursor.execute(f"INSERT INTO account(Account_balance,Account_owner,Account_password,Access_Number)VALUES ({starting_value}, {desired_username}, {desired_password}, {generate_access_number()})")

            cursor.close()
            connector.close()
            print("User Created")
        except mysql.connector.Error as err:
            print(f"Error: {err}")


#Has to be last because it includes preciously made functions
def user_action():
    print("What can I help you with Today")
    action = int(input("1.) Login\n2.) Create Account\n3.)Exit\n"))
    print(action)
    if action == 1:
        login()
    elif action == 2:
        create_user()
        user_action()
    elif action == 3:
        program == False
        print("Come again")
        return
    else:
        action = int(input("Please use either 1, 2, or 3 as your repsonse"))



while program == True:
    print("Welcome to Ema banks")
    user_action()
