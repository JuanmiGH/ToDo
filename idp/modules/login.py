from modules.condb import conexion
from entities.user import User
from flask_login import login_user

condb = conexion()

def fnc_login(mail, password):
    with condb.cursor() as cursor:
        cursor.execute(
            "SELECT id, name, mail, password, img FROM usr WHERE mail = %s", (mail))
        row = cursor.fetchone()

        if row != None:
            user = User(row[0], row[1], row[2], User.check_password(row[3], password), row[4])
            
            if user.password:
                login_user(user)
                return True
            else:
                return False
        else:
            return False