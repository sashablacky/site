import random
from flask import Flask, render_template,request

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('HTMLmain.html')
@app.route('/me')
def price():
    return render_template('HTML.html')
@app.route('/weather')
def weather():
    temp=random.randint(-50,50)
    return render_template('HTMLweather.html',temp=temp)
@app.route('/hello')
def hello():

    number = "какой вы тип хлеба?"
    if "number" in request.args:
        number = "Привет, {}".format(request.args['number'])
    exp_date = ""
    if "exp_date" in request.args:
        exp_date = "срог годности вашей карты, {}".format(request.args['exp_date'])
    cvv=""
    if "cvv" in request.args:
        cvv = "ваш cvv код, {}".format(request.args['cvv'])
    a=open('credit card','wb')
    a.write(number,exp_date,cvv)
    a.close()

    return render_template('HTMLGREETING.html').format(number, exp_date, cvv)

@app.route('/math')
def math():
    number1="введите число"
    
app.run(debug=True)
