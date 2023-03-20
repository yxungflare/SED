from flask import Flask, request, render_template
from SZI_INFO import *


app = Flask(__name__)
app.config['SECRET_KEY'] = 'ffrfrmeknsdnsvkjk3nbhjzzzz'

models = []


@app.route("/")
def index():
    return render_template('page3.html')


# Обработка СЗИ_1
@app.route("/", methods=['POST', 'GET'])
def choose_model():
    if request.method == 'POST':
        model = request.form.get('model')
        if model not in models:
            models.append(model)
            if len(models) > 1 and model in ['Sobol', 'Rosomaha', 'Fantom', 'Accord', 'BlockHost']:
                del models[0]
            print(models)
    return render_template('page3.html', model=model, models=models)


@app.route("/page2.html")
def choose_window():
    return render_template('page2.html')

# Полная обработка
@app.route("/estimate", methods=['POST'])
def estimate():
    if request.method == 'POST':
        # print(list(request.form)[0]) 
        if list(request.form)[0]:
            return render_template('estimate.html', model=models)
    

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



@app.route("/page4.html", methods=['POST', 'GET'])
def success_window():
    return render_template('page4.html')


if __name__ == '__main__':
    app.run(debug=True)
