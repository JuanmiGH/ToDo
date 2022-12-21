from flask import Flask, render_template, redirect, url_for, request
import os
from datetime import datetime
from flask_login import LoginManager, login_required, current_user

from models.model_user import ModelUser

from idp.idp import idp

from modules.condb import conexion
from modules.newtask import newTask
from modules.tasks import *

from forms.addtask import frm_addtask

app = Flask(__name__, instance_path='/')
app.register_blueprint(idp, url_prefix='/idp')
app.config['SECRET_KEY'] = 'YourSK'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['MAX_CONTENT_LENGTH'] = 1 * 1024 * 1024  # 1MB max-limit para las imágenes de perfil.

login_manager_app = LoginManager(app)
login_manager_app.login_view = "/idp/login"

condb=conexion()

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(condb, id)

def nearDeadline(taskDeadline):
    deadline = datetime.strptime(taskDeadline, '%d/%m/%Y')
    today = datetime.today().strftime('%d/%m/%Y')
    today = datetime.strptime(today, '%d/%m/%Y')
    diff = deadline - today   

    if (diff.days) <= 0:
        return 'danger'
    elif (diff.days >0) and (diff.days <= 10):
            return 'warning'
    else:
        return False

@app.route('/', methods=["GET", "POST"])
@login_required
def home():
    hptitle = ' - Task List'
    taskError=None
    fraddtask = frm_addtask()

    tasksTodo = tasks_todo()
    tasksDoing = tasks_doing()
    tasksDone = tasks_done()
    if type(tasksTodo) != tuple:
        taskError=tasksTodo
    if type(tasksDoing) != tuple:
        taskError=tasksDoing
    if type(tasksDone) != tuple:
        taskError=tasksDone

    if fraddtask.validate_on_submit():
        tasktitle = fraddtask.title.data
        text = fraddtask.text.data
        estimatedTime = fraddtask.estimatedTime.data
        deadline = fraddtask.deadline.data
        user = current_user.get_id()
        createdOn = datetime.today().strftime('%d/%m/%Y')
        fraddtask.title.data, fraddtask.text.data, fraddtask.estimatedTime.data, fraddtask.deadline.data = '', '', '', ''

        if newTask(user, estimatedTime, deadline, createdOn, text, tasktitle):
            frError=None
            return redirect(url_for('home'))
        else: 
            frError='An error has occurred'
            return redirect(url_for('home'))

    else:
        frError= fraddtask.errors

    return render_template('home.html', title=hptitle, fraddtask=fraddtask, frError=frError, todo=tasksTodo, doing=tasksDoing, done=tasksDone, taskError=taskError, fncDeadline=nearDeadline)

@app.route('/moveTask/<idtask>/<moveto>')
@login_required
def moveTask(idtask, moveto):
    if idtask and moveto:
        if move_task_to(idtask, moveto):
            return redirect(url_for('home'))
        else:
            frError='An error has occurred'
            return redirect(url_for('home'))
    return redirect(url_for('home'))


@app.route('/upd-task/<idtask>', methods=["GET", "POST"])
@login_required
def updtask(idtask):
    frupdtask = frm_addtask()
    hptitle = "View - Edit Task"
    if idtask:
        if request.method == 'GET':
            if check_task_propietary(idtask):
                frError = None
                task_data = retrive_task_data(idtask)
                frupdtask.title.data=task_data[8]
                frupdtask.text.data=task_data[7]
                frupdtask.estimatedTime.data=task_data[3]
                frupdtask.deadline.data=task_data[4]
            else:
                frError = 'You are not the owner of this task'
                return redirect(url_for('home'))
        else:
            if frupdtask.validate_on_submit():
                tasktitle = frupdtask.title.data
                text = frupdtask.text.data
                estimatedTime = frupdtask.estimatedTime.data
                deadline = frupdtask.deadline.data

                if update_task(idtask, tasktitle, text, estimatedTime, deadline):
                    return redirect(url_for('home'))
                else:
                    frError='An error has occurred'
                    return redirect(url_for('home'))
            else:
                frError= 'Check the red warnings below the inputs'
    else:
        return redirect(url_for('home'))
        
    return render_template('task.html', title=hptitle, frupdtask=frupdtask, frError=frError)


if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)