from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    app.config["MySQL_HOST"]= "Localhost"
    app.config["MySQL_USER"]= "root"
    app.config["MySQL_PASSWORD"]= "root"
    app.config["MySQL_DB"]= "hiretrack_db"

    mysql.init_app(app)


