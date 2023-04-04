## main.py
from flask import Flask, render_template
app = Flask(__name__)

# 초기 화면
@app.route('/')
def index():
    return render_template('index.html')

# 동적 URL 파라미터 받기
@app.route('/parameter/<string:param1>/<param2>')
def parameter(param1, param2):
    return render_template('parameter.html', param1=param1, param2=param2)


if __name__ == '__main__':
    app.run(debug=True)