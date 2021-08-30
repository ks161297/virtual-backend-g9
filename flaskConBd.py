from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'empresa'
app.config['MYSQL_PORT'] = '3306'

mysql = MySQL(app)

@app.route('/')
def inicio():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM DEPARTAMENTO")

if __name__ == '__main__':
    app.run(debug=True)