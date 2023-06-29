from flask import Flask, request, render_template, g
from SZI_INFO import *
import os

SECRET_KEY = 'ffrfrmeknsdnsvkjk3nbhjzzzz'

app = Flask(__name__)
app.config.from_object(__name__)

models = []
update_models = []

models_ksz = []

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
    model4 = request.form.get('model4')
    model5 = request.form.get('model5')
    model6 = request.form.get('model6')
    model7 = request.form.get('model7')
    model8 = request.form.get('model8')
    model9 = request.form.get('model9')
    model10 = request.form.get('model10')
    model11 = request.form.get('model11')

    print(request.form)
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
    # СЗИ 4
    if model4 not in models and model4 and model4 != 'choose':
        models.append(model4)
        [update_models.append(elem) for elem in SZI_models if elem[0] == model4]
        # Проверяем уникальность для СЗИ 4
        if len(models) > 1 and model4 in model_set_4:
            for m in models:
                if m != model4 and m in model_set_4:
                    for elem in update_models:
                        if elem[0] != model4 and elem[0] in model_set_4:
                            del update_models[update_models.index(elem)]
                    del models[models.index(m)]

    # СЗИ 5
    if model5 not in models and model5 and model5 != 'choose':
        models.append(model5)
        [update_models.append(elem) for elem in SZI_models if elem[0] == model5]
        # Проверяем уникальность для СЗИ 5
        if len(models) > 1 and model5 in model_set_5:
            for m in models:
                if m != model5 and m in model_set_5:
                    for elem in update_models:
                        if elem[0] != model5 and elem[0] in model_set_5:
                            del update_models[update_models.index(elem)]
                    del models[models.index(m)]
    
    # СЗИ 6
    if model6 not in models and model6 and model6 != 'choose':
        models.append(model6)
        [update_models.append(elem) for elem in SZI_models if elem[0] == model6]
        # Проверяем уникальность для СЗИ 6
        if len(models) > 1 and model6 in model_set_6:
            for m in models:
                if m != model6 and m in model_set_6:
                    for elem in update_models:
                        if elem[0] != model6 and elem[0] in model_set_6:
                            del update_models[update_models.index(elem)]
                    del models[models.index(m)]
        
    # СЗИ 7
    if model7 not in models and model7 and model7 != 'choose':
        models.append(model7)
        [update_models.append(elem) for elem in SZI_models if elem[0] == model7]
        # Проверяем уникальность для СЗИ 7
        if len(models) > 1 and model7 in model_set_7:
            for m in models:
                if m != model7 and m in model_set_7:
                    for elem in update_models:
                        if elem[0] != model7 and elem[0] in model_set_7:
                            del update_models[update_models.index(elem)]
                    del models[models.index(m)]

    # СЗИ 8
    if model8 not in models and model8 and model8 != 'choose':
        models.append(model8)
        [update_models.append(elem) for elem in SZI_models if elem[0] == model8]
        # Проверяем уникальность для СЗИ 8
        if len(models) > 1 and model8 in model_set_8:
            for m in models:
                if m != model8 and m in model_set_8:
                    for elem in update_models:
                        if elem[0] != model8 and elem[0] in model_set_8:
                            del update_models[update_models.index(elem)]
                    del models[models.index(m)]
    # СЗИ 9
    if model9 not in models and model9 and model9 != 'choose':
        models.append(model9)
        [update_models.append(elem) for elem in SZI_models if elem[0] == model9]
        # Проверяем уникальность для СЗИ 9
        if len(models) > 1 and model9 in model_set_9:
            for m in models:
                if m != model9 and m in model_set_9:
                    for elem in update_models:
                        if elem[0] != model9 and elem[0] in model_set_9:
                            del update_models[update_models.index(elem)]
                    del models[models.index(m)]

    # СЗИ 10
    if model10 not in models and model10 and model10 != 'choose':
        models.append(model10)
        [update_models.append(elem) for elem in SZI_models if elem[0] == model10]
        # Проверяем уникальность для СЗИ 10
        if len(models) > 1 and model10 in model_set_10:
            for m in models:
                if m != model10 and m in model_set_10:
                    for elem in update_models:
                        if elem[0] != model10 and elem[0] in model_set_10:
                            del update_models[update_models.index(elem)]
                    del models[models.index(m)]

    # СЗИ 11
    if model11 not in models and model11 and model11 != 'choose':
        models.append(model11)
        [update_models.append(elem) for elem in SZI_models if elem[0] == model11]
        # Проверяем уникальность для СЗИ 11
        if len(models) > 1 and model11 in model_set_11:
            for m in models:
                if m != model11 and m in model_set_11:
                    for elem in update_models:
                        if elem[0] != model11 and elem[0] in model_set_11:
                            del update_models[update_models.index(elem)]
                    del models[models.index(m)]
    print(models)
    print(update_models)
    return render_template('page3.html', models=models, model=model, model2=model2, 
                           model3=model3, model4=model4, model5=model5, model6=model6,
                           model7=model7, model8=model8, model9=model9, model10=model10, model11=model11)

@app.route("/page1.html")
def choose_window():
    return render_template('page1.html')


@app.route("/ready", methods=['POST', 'GET'])
def ready_KSZ():
    check_cash = 0
    priority = request.form.get('priority')
    ksz_model = request.form.get('ksz_models')
    if request.form.get('price'):
        cash = int(request.form.get('price'))
        check_cash = 1
        ksz_model = ''
    else:
        cash = 500000
    print(request.form, ksz_model)
    if request.form.get('reset_data'):
        check_cash = 0
        cash = 500000
        priority = ''
        ksz_model = ''
    return render_template('ready.html', priority=priority, cash=cash, check_cash=check_cash, ksz_model=ksz_model)
# ====!==== 



@app.route("/page2.html")
def first_page():
    return render_template('page2.html')


# Полная обработка

@app.route("/estimate", methods=['POST'])
def estimate():
    if request.method == 'POST':
        print(models)
        if list(request.form)[0]:
            total_price = 0
            total_sec = 1.0
            # Создаем массив, в котором будут хранится надежности компонентов
            ur = []
            # список угроз
            menace = []

            for m in models:
                for i in SZI_models:
                    if m in i:
                        # Итоговая стоимость системы
                        total_price += int(i[1])
                        print(total_price)
                        # Итоговая надежность системы
                        ur.append(float(i[3]))
                        print(ur)
                        menace.append(i[2])

            for reliability in ur:
                total_sec *= (1 - reliability)
            system_reliability = (1 - total_sec) * 100

            # массив угроз и их покрытий
            new_manace_ur = zip(menace, ur)
            print(new_manace_ur)
            return render_template('estimate.html', models=models, price=total_price, reliability=system_reliability, new_manace_ur=new_manace_ur)
    

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
