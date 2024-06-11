#!C:\Python\python.exe

from Connection import Connection

class On():
    def execute(self):
        try:
            conn = Connection("localhost", "root", "", "db")
            mydb = conn.connect()
            mycursor = mydb.cursor()
            sql = "UPDATE state SET state = 'ON' WHERE ID = 1;"
            mycursor.execute(sql)
            mydb.commit()
            # print("State updated to ON in the database")
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
        finally:
            mycursor.close()
            mydb.close()

class Off():
    def execute(self):
        try:
            conn = Connection("localhost", "root", "", "db")
            mydb = conn.connect()
            mycursor = mydb.cursor()
            sql = "UPDATE state SET state = 'OFF' WHERE ID = 1;"
            mycursor.execute(sql)
            mydb.commit()
            # print("State updated to OFF in the database")
        except mysql.connector.Error as err:
            print("Error: {}".format(err))
        finally:
            mycursor.close()
            mydb.close()
