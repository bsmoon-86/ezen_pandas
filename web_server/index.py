# flask 라이브러리 로드 
from flask import Flask, render_template

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


app.run(host='0.0.0.0', port = 3000)