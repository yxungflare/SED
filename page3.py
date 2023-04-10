from flask import Flask, request, render_template, g
from SZI_INFO import *
import os

SECRET_KEY = 'ffrfrmeknsdnsvkjk3nbhjzzzz'

app = Flask(__name__)
app.config.from_object(__name__)

models = []
update_models = []

def clear_update_models():
    pass


@app.route("/")
def index():
    return render_template('page3.html')


# Обработка СЗИ
@app.route("/", methods=['POST', 'GET'])
def choose_model():
    model = request.form.get('model') 
    model2 = request.form.get('model2')
    model3 = request.form.get('model3')
    print(request.form)
    print(model, model2, model3)
    # СЗИ 1
    if model not in models and model and model != 'choose':
        models.append(model)
        [update_models.append(elem) for elem in SZI_models if elem[0] == model]
        # Проверяем уникальность для СЗИ 1
        if len(models) > 1 and model in model_set_1:
            for m in models:
                if m != model and m in model_set_1:
                    for elem in update_models:
                        if elem[0] != model and elem[0] in model_set_1:
                            del update_models[update_models.index(elem)] 
                    del models[models.index(m)]
    # СЗИ 2
    if model2 not in models and model2 and model2 != 'choose':
        models.append(model2)
        [update_models.append(elem) for elem in SZI_models if elem[0] == model2]
        # Проверяем уникальность для СЗИ 2
        if len(models) > 1 and model2 in model_set_2:
            for m in models:
                if m != model2 and m in model_set_2:
                    for elem in update_models:
                        if elem[0] != model2 and elem[0] in model_set_2:
                            del update_models[update_models.index(elem)]
                    del models[models.index(m)]
    # СЗИ 3
    if model3 not in models and model3 and model3 != 'choose':
        models.append(model3)
        [update_models.append(elem) for elem in SZI_models if elem[0] == model3]
        # Проверяем уникальность для СЗИ 3
        if len(models) > 1 and model3 in model_set_3:
            for m in models:
                if m != model3 and m in model_set_3:
                    for elem in update_models:
                        if elem[0] != model3 and elem[0] in model_set_3:
                            del update_models[update_models.index(elem)]
                    del models[models.index(m)]
    print(models)
    print(update_models)
    return render_template('page3.html', models=models, model=model, model2=model2, model3=model3)


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
