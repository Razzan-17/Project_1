from flask import Flask, render_template, request, abort

from lock import PASSWORD
from work_BD import BDManager

app = Flask(__name__)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method =='POST':
        if request.form.get('password') == PASSWORD:
            return 'Сегодня, всё время'
        else:
            return abort(404)
    elif request.method =='GET':
        return render_template('admin_auth.html')
    else:
        return abort(403)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/projects')
def projects():
    db = BDManager()
    data = db.select_data_all()
    return render_template('projects.html', data=data)


if __name__ == '__main__':
    app.run()
