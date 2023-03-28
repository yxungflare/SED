from flask import Flask, request, render_template, g
from SZI_INFO import FDataBase
import sqlite3
import os

DATABASE = 'SZI.db'
SECRET_KEY = 'ffrfrmeknsdnsvkjk3nbhjzzzz'

app = Flask(__name__)
app.config.from_object(__name__)

# Переопределяем путь к бд
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'SZI.db')))


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn

def create_db():
    db = connect_db()
    with app.open_resource('create_table.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


def get_db():
    # Соединение с бд, если не было установлено
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
    return g.link_db


models = []


@app.route("/")
def index():
    return render_template('page3.html')


# Обработка СЗИ
@app.route("/", methods=['POST', 'GET'])
def choose_model():
    db = get_db()
    dbase = FDataBase(db)
    print(dbase.getMenu())
    if request.method == 'POST':
        SZI1 = request.form.get('model')
        SZI2 = request.form.get('model2')
        if SZI1:
            model = SZI1
        if SZI2:
            model = SZI2

        if model not in models:
            models.append(model)
            # Проверяем уникальность для СЗИ 1
            if len(models) > 1 and model in ['Sobol', 'Rosomaha', 'Fantom', 'Accord', 'BlockHost']:
                for m in models:
                    if m != model and m in ['Sobol', 'Rosomaha', 'Fantom', 'Accord', 'BlockHost']:
                        del models[models.index(m)]
            # СЗИ 2
            elif len(models) > 1 and model in ['Rutoken', 'PKIClient', 'Cryptopro', 'VipNet', 'SecretDisk']:
                for m in models:
                    if m != model and m in ['Rutoken', 'PKIClient', 'Cryptopro', 'VipNet', 'SecretDisk']:
                        del models[models.index(m)]
            print(models)
            
        return render_template('page3.html', models=models, model=model)


@app.teardown_appcontext
def close_db(error):
    # разрываем соединение, если его не было
    if hasattr(g, 'link_db'):
        g.link_db.close()


@app.route("/page2.html")
def choose_window():
    return render_template('page2.html')


# Полная обработка
# Нужно проработать: удалить элемент массива, если чекбокс не выбран 

@app.route("/estimate", methods=['POST'])
def estimate():
    if request.method == 'POST':
        print(models)
        if list(request.form)[0]:
            return render_template('estimate.html', models=models)
    

# Инфа о Соболе
@app.route("/htdocs/Sobol.html")
def Sobol():
    return render_template('htdocs/Sobol.html')


# Инфа о Росомахе
@app.route("/htdocs/Rosomaha.html")
def Rosomaha():
    return render_template('/htdocs/Rosomaha.html')


# Инфа о Фантоме
@app.route("/htdocs/Fantom.html")
def Fantom():
    return render_template('/htdocs/Fantom.html')


# Инфа о Аккорде
@app.route("/htdocs/Accord.html")
def Accord():
    return render_template('/htdocs/Accord.html')


# Инфа о БлокХосте
@app.route("/htdocs/BlockHost.html")
def BlockHost():
    return render_template('/htdocs/BlockHost.html')


# Инфа о БлокХосте
@app.route("/htdocs/SecretDisk.html")
def SecretDisk():
    return render_template('/htdocs/SecretDisk.html')


# Инфа о ВипНет
@app.route("/htdocs/VipNet.html")
def VipNet():
    return render_template('/htdocs/VipNet.html')


# Инфа о Рутокен
@app.route("/htdocs/Rutoken.html")
def Rutoken():
    return render_template('/htdocs/Rutoken.html')


# Инфа о КриптоПро
@app.route("/htdocs/Cryptopro.html")
def Cryptopro():
    return render_template('/htdocs/Cryptopro.html')


# Инфа о ПКИ Клиент
@app.route("/htdocs/PKIClient.html")
def PKIClient():
    return render_template('/htdocs/PKIClient.html')


@app.route("/page4.html", methods=['POST', 'GET'])
def success_window():
    return render_template('page4.html')




if __name__ == '__main__':
    app.run(debug=True)
