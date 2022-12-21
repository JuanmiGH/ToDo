from modules.condb import conexion
from flask_login import current_user

condb = conexion()

def tasks_todo():
    try:
        cursor = condb.cursor()
        condb.commit()
        sql = "SELECT * FROM tasks WHERE propietario = {} and estado = 'todo'".format(current_user.get_id())
        cursor.execute(sql)
        tasks = cursor.fetchall()

        return tasks
    
    except Exception as ex:
        return ex

def tasks_doing():
    try:
        cursor = condb.cursor()
        condb.commit()
        sql = "SELECT * FROM tasks WHERE propietario = {} and estado = 'doing'".format(current_user.get_id())
        cursor.execute(sql)
        tasks = cursor.fetchall()

        return tasks
    
    except Exception as ex:
        return ex

def tasks_done():
    try:
        cursor = condb.cursor()
        condb.commit()
        sql = "SELECT * FROM tasks WHERE propietario = {} and estado = 'done'".format(current_user.get_id())
        cursor.execute(sql)
        tasks = cursor.fetchall()

        return tasks
    
    except Exception as ex:
        return ex

def move_task_to(id, moveto):
    if moveto == 'doing' or moveto == 'done' or moveto == 'todo':
        try:
            cursor = condb.cursor()
            sql = "SELECT propietario FROM tasks WHERE id = {}".format(id)
            cursor.execute(sql)
            task = cursor.fetchone()

            if task[0] == current_user.get_id():
                cursor.execute("UPDATE tasks SET estado = %s WHERE id = %s",(moveto, id))
                condb.commit()
                return True
            else:
                return False
        
        except Exception as ex:
            print(ex)
            return False
    else:
        return False

def check_task_propietary(id):
    try:
        cursor = condb.cursor()
        sql = "SELECT propietario FROM tasks WHERE id = {}".format(id)
        cursor.execute(sql)
        task = cursor.fetchone()

        if task[0] == current_user.get_id():
            return True
        else:
            return False

    except Exception as ex:
        print(ex)
        return False

def retrive_task_data(id):
    try:
        cursor = condb.cursor()
        sql = "SELECT * FROM tasks WHERE id = {}".format(id)
        cursor.execute(sql)
        task_data = cursor.fetchone()
    except Exception as ex:
        print(ex)
        return False

    return task_data

def update_task(id, tasktitle, text, estimatedTime, deadline):
    try:
        cursor = condb.cursor()
        cursor.execute("UPDATE tasks SET titulo = %s, texto = %s, t_estimado = %s, deadline = %s WHERE id = %s",(tasktitle, text, estimatedTime, deadline, id))
        condb.commit()
        return True
    except Exception as ex:
        print(ex)
        return False

        