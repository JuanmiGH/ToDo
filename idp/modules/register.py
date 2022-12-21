from modules.condb import conexion

condb = conexion()

def fnc_register(name, mail, password, img64):
    with condb.cursor() as cursor:
        cursor.execute("INSERT INTO usr(name, mail, password, img) VALUES (%s, %s, %s, %s)",
                    (name, mail, password, img64))
        condb.commit()
    return True