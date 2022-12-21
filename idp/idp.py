from flask import Blueprint, render_template, redirect, url_for
from werkzeug.security import generate_password_hash
from flask_login import logout_user
import base64

from .modules.login import fnc_login
from .modules.register import fnc_register

from .forms.login import frm_login
from .forms.register import frm_register

idp = Blueprint('idp', __name__, template_folder='templates')


@idp.route('/login', methods=["GET", "POST"])
def login():
    frlogin = frm_login()    
    if frlogin.validate_on_submit():
        mail = frlogin.mail.data
        password = frlogin.password.data
        
        if fnc_login(mail, password):
            return redirect(url_for('home'))
        else:
            return render_template('login.html', frlogin=frm_login(), title='Login', error='Wrong user or password')

    return render_template('login.html', frlogin=frlogin, title='Login')


@idp.route('/register', methods=["GET", "POST"])
def register():
    frregister = frm_register()
    if frregister.validate_on_submit():
        name = frregister.name.data
        mail = frregister.mail.data
        password = generate_password_hash(frregister.password.data)
        img = frregister.img.data
        img64 = base64.b64encode(img.read())

        if fnc_register(name, mail, password, img64):
            if fnc_login(mail, frregister.password.data):
                return redirect(url_for('home'))
            else:
                return render_template('login.html', frlogin=frm_login(), title='Operation failed', error='An error has occurred')
        else:
            return render_template('register.html', frregister=frm_register(), title='Operation failed', error='An error has occurred')

    return render_template('register.html', frregister=frregister, title='Register')


@idp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))