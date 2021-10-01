from flask import Flask,render_template,request
import joblib
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

@app.route('/predict',methods=["GET","POST"])
def predict():
    try:
        dateValue = int("".join(request.form["dateofprediction"].split("-")))
        close = round(joblib.load("static/CLOSE_predict.pkl").predict([[dateValue]])[0][0],3)
        high = round(joblib.load("static/HIGH_predict.pkl").predict([[dateValue]])[0][0],3)
        low = round(joblib.load("static/LOW_predict.pkl").predict([[dateValue]])[0][0],3)
        open = round(joblib.load("static/OPEN_predict.pkl").predict([[dateValue]])[0][0],3)
        turnover = round(joblib.load("static/TURNOVER_predict.pkl").predict([[dateValue]])[0][0],3)
        volume = round(joblib.load("static/VOLUME_predict.pkl").predict([[dateValue]])[0][0],3)
        vwap = round(joblib.load("static/VWAP_predict.pkl").predict([[dateValue]])[0][0],3)
        dateValue = request.form["dateofprediction"]
        return render_template('homePage.html',predicted=True,data=[dateValue,open,close,high,low,turnover,volume,vwap])
    except:
        return render_template('homePage.html',predicted=False)

@app.route('/')
def index():
    return render_template('homePage.html',predicted=False)

if __name__ == '__main__':
    app.run(debug=True)
