import mysql.connector

def access_pokemon_table():
    connection = mysql.connector.connect(user = 'Test1', database = 'example', password = 'Emanuel625')

    cursor = connection.cursor()

    testQuery = ("SELECT * FROM pokemon")

    cursor.execute(testQuery)

    for item in cursor:

        

        print(item)


    cursor.close()

    connection.close()

#This section should be a method that create_user




#This section should be one for user_login




#This section should be a method for transfering money between users
#Use conditional statements for this section



#This section should be for checking account balance




#This section should be for checking account 