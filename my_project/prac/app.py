from flask import Flask, render_template, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<button>button</button>'

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/test', methods=['GET'])
def test_get():
    title_receive = request.args.get('title_give')
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 GET!'})
#파이썬 딕셔너리를 제이슨 딕셔너리로 바꾼다

@app.route('/test', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)