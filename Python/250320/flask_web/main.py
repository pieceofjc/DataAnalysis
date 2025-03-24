from random import randint
from flask import Flask, render_template, request, redirect, session
from database import MyDB
import os
from dotenv import load_dotenv
import pandas as pd

# env 로드
load_dotenv()

# Flask class 생성
# 생성자 함수에는 파일의 이름
app = Flask(__name__)

# 시크릿키
app.secret_key = os.getenv('secret_key')

web_db = MyDB()
web_db.connect_sql()

# 세션 초기화

# localhost:5000/ 요청이 들어왔을때
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup2.html')
    elif request.method == 'POST':
        input_pass = request.form['password']
        print(input_pass)
        return {'success': True}
    
@app.route('/game', methods=['GET'])
def game():
    if 'user_nick' in session:
        return render_template('game.html', nickname = session['user_nick'])
    else:
        try:
            user_nick = request.args['nickname']
            session['user_nick'] = user_nick
            print(session['user_nick'])
            return render_template('game.html', nickname = session['user_nick'])
        except Exception as e:
            print(e)
            return redirect('/')
        
@app.route('/game_result', methods=['GET'])
def game_result():
    user_select = request.args.get('user', type=int)
    server_select = randint(1,3)
    print(user_select, server_select)

    result = "무승부"
    if user_select == 1: # 가위
        if server_select == 2:
            result = "패배"
        elif server_select == 3:
            result = "승리"
    elif user_select == 2: # 바위
        if server_select == 3:
            result = "패배"
        elif server_select == 1:
            result = "승리"
    elif user_select == 3: # 보
        if server_select == 1:
            result = "패배"
        elif server_select == 2:
            result = "승리"

    return_data = {
        'user' : user_select,
        'server' : server_select,
        'result' : result
    }
    print(f"[get_ajax] /game_result : GAME DATA [{return_data}] ")
    return return_data

@app.route('/signup2', methods=['GET','POST'])
def signup2():
    if request.method == 'GET':
        return render_template('signup.html')
    if 'user_nick' in session:
        return redirect("/")
    try:
        request.form['user_id']
        return render_template()
    except Exception as e:
        print(e)
        return redirect('/')

@app.route('/check_id', methods=['POST'])
def check_id():
    user_id = request.form['user_id']
    select_query = "select * from user_list where `id` like %s"
    df = web_db.execute_query(select_query, user_id)
    if len(df):
        return {'check_id': False} # 사용 불가
    else:
        return {'check_id': True} # 사용 가능
    
# 웹서버의 실행 
app.run(debug=True)
