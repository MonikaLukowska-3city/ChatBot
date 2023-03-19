import os
import pyodbc
from flask import Flask
from flask import request

port = os.environ['FLASK_PORT']
app = Flask(__name__)

@app.route('/users', methods=['POST'])
def test():
   data = request.json

   DATABASE_NAME = os.getenv('DATABASE_NAME')
   DATABASE_SERVER = os.getenv('DATABASE_SERVER')
   DATABASE_LOGIN = os.getenv('DATABASE_LOGIN')
   DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
   DATABASE_PORT = os.getenv('DATABASE_PORT')
   con_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + DATABASE_SERVER + "," + DATABASE_PORT + ";Encrypt=no;DATABASE=" + DATABASE_NAME + ";UID=" + DATABASE_LOGIN +  ";PWD=" + DATABASE_PASSWORD
   
   print(f"con_string: {con_string}")

   conn = pyodbc.connect(con_string)
   query = f"select name, surname from chatbot.dbo.users where cif = ?"

   cursor = conn.cursor()
   cursor.execute(query, [data['cif']])
   result = cursor.fetchone()
   cursor.close()


   return {      
      "msg" : f"Hello {result[0]} {result[1]}"
   }


'''
   
'''

if __name__ == '__main__':   
   app.run(port=port, debug=True, host="0.0.0.0")