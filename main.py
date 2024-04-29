import mysql.connector

User = ''
Password = ''

program = True




#We use this code to find out if a user is already made in the server
def target(target):
    target_found = False
    try:
        conn = mysql.connector.connect(
            user='root',
            password='Emanuel625.',
            database = 'example'
        )

        cursor = conn.cursor()
        cursor.execute('SELECT user FROM mysql.user')
        users = cursor.fetchall()

        for user in users:
            if str(user[0]) == target:
                print("Found target")
                target_found = True

        cursor.close()
        conn.close()
        return target_found
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
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

    connection = mysql.connector.connect(user = 'root', password = 'Emanuel625.')

    cursor = connection.cursor()

    username = desired_username

    cursor.execute('SELECT username FROM users WHERE username = %(username)s', (username,))
    checkUsername = mycursor.fetchone()
    if checkUsername != 0:
        print('Username is not exist')
    else:
        print('Logged In!')





#Has to be last because it includes preciously made functions
def user_action():
    print("What can I help you with Today")
    action = int(input("1.) Login\n2.) Create Account\n3.)Exit\n"))
    print(action)
    if action == 1:
        login()
    elif action == 2:
        create_user()
    elif action == 3:
        program == False
        return
    else:
        action = int(input("Please use either 1, 2, or 3 as your repsonse"))





login()


# while program == True:
#     print("Welcome to Ema banks")
#     user_action()


