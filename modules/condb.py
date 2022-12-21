import pymysql

def conexion():
    return pymysql.connect(host='host',
                                user='user',
                                password='pass',
                                db='dbname')