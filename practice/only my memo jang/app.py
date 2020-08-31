from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만들거나 사용합니다.


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/memo', methods=['POST'])
def post_article():
    url_receive = request.form['url_give']
    comment_receive = request.form['comment_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    img = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']

    print(title, img, desc)

    doc = {
        'url': url_receive,
        'comment': comment_receive,
        'title': title,
        'img': img,
        'desc': desc
    }

    db.memo.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '저장이 완료되었습니'})


@app.route('/memo', methods=['GET'])
def read_articles():
    comment = list(db.memo.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'comments': comment})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)