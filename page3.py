from flask import Flask, request, render_template, g
from SZI_INFO import SZI_models
import os

SECRET_KEY = 'ffrfrmeknsdnsvkjk3nbhjzzzz'

app = Flask(__name__)
app.config.from_object(__name__)

models = []

@app.route("/")
def index():
    return render_template('page3.html')


# Обработка СЗИ
@app.route("/", methods=['POST', 'GET'])
def choose_model():
    if 'model' in request.form:
        model = request.form.getlist('model')[-1]
    elif 'model2' in request.form:
        model = request.form.getlist('model2')[-1]

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
