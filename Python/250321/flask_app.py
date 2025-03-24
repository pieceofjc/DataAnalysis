# 기본적인 웹 서버 설정 
# flask 웹프레임워크 로드 
from flask import Flask, render_template, request, redirect, url_for
from database import MyDB
import pandas as pd
import os

# Flask class 생성
app = Flask(__name__)

# MyDB Class 생성
web_db = MyDB()

# 127.0.0.1:5000/ url 생성
@app.route('/')
def index():
    return render_template('index.html')


# dashboard를 보여주는 url 생성 
@app.route("/dashboard")
def dashboard():
    ticker = request.args['ticker']
    print(f"'[get] /dashboard : {ticker}")
    dir_name = os.path.abspath(__file__)
    csv_name = os.path.join(dir_name, '../data', f'{ticker}.csv')
    df = pd.read_csv(csv_name)
    df = df.tail(50)
    
    date_list = df['Date'].to_list()
    close_list = df['Adj Close'].to_list()
    volume_list= df['Volume'].to_list()
    dict_data = df.to_dict(orient="records")
    cols_list = list(dict_data[0].keys())
        
    return render_template(
        'dashboard.html',
        x_data = date_list,
        y_data = close_list,
        y_data2 = volume_list,
        table_data = dict_data,
        table_cols = cols_list    
    )

# 웹서버 실행 
app.run(debug=True)