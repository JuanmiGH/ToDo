from modules.condb import conexion
condb=conexion()

def newTask(user, estimatedTime, deadline, createdOn, text, tasktitle):
    with condb.cursor() as cursor:
        cursor.execute("INSERT INTO tasks(propietario, estado, t_estimado, deadline, fdcreacion, fdcierre, texto, titulo) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                (user, 'todo', estimatedTime, deadline, createdOn, '', text, tasktitle))
        condb.commit()
    return True