# flask 라이브러리 로드 
from flask import Flask, redirect, render_template, request
import list
import pandas as pd

# Flask(현재 파일의 이름) 클래스 생성
# __name__ : 현재 파일의 이름
app = Flask(__name__)

# api 생성
# 네비게이터 함수
# 해당하는 주소로 요청이 들어오면 바로 아래의 함수를 호출
# "/"이 주소의 뜻은 localhost:3000/
@app.route("/")
def index():
    return render_template('index.html')

# localhost:3000/second 요청이 들어오면
@app.route("/second")
def second():
    return render_template('second.html')

# localhost:3000/data [post]요청이 들어오면
@app.route("/data", methods=['post'])
def data():
    # 유저가 보낸 데이터를 받아서 변수에 대입
    # get 방식으로 데이터가 들어오는 경우
    # input_data = request.args['input_text']
    # input_password = request.args['input_pass']
    # print(request.args)
    # post 방식으로 데이터가 들어오는 경우
    input_data = request.form['input_text']
    input_password = request.form['input_pass']
    print(request.form)
    # print(input_data)
    # input_data가 test이고 input_password가 1234인 경우라는 조건식
    if (input_data == 'test') & (input_password == '1234'):
        return render_template('main.html', _id = input_data)
    else:
        # 다른 주소로 이동
        return redirect("/")
    
# 데이터를 보내주는 api를 생성
# localhost:3000/open_data
@app.route('/open_data')
def open_data():
    # path = "../csv/2017/"
    # end = ".csv"
    # df = list.list_data(path, end)
    df = pd.read_csv('../csv/corona.csv')
    df.drop("Unnamed: 0", axis=1, inplace=True)
    dict_data = df.to_dict("records")
    return dict_data


app.run(host='0.0.0.0', port = 3000)