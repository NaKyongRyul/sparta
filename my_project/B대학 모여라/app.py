from pymongo import MongoClient
from flask import Flask, render_template, jsonify, request, redirect

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('ui.html')


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/detail/<meeting_id>')
def detail(meeting_id):
    meeting_found = db.meeting.find_one({'id': int(meeting_id)}, {'_id': False, 'pw': False})
    if meeting_found is None:
        return redirect('/')
    else:
        return render_template('detail.html', meeting=meeting_found)


@app.route('/meeting', methods=['POST'])
def meeeting():
    title_receive = request.form['title_give']
    pw_receive = request.form['pw_give']
    place_receive = request.form['place_give']
    time_receive = request.form['time_give']
    desc_receive = request.form['desc_give']
    todo_receive = request.form['todo_give']
    keyword_receive = request.form['keyword_give']

    # meeing 고유 식별 키 만들기
    total = db.meeting.count()

    doc = {
        'id': total + 1,
        'title': title_receive,
        'pw': pw_receive,
        'place': place_receive,
        'time': time_receive,
        'desc': desc_receive,
        'todo': todo_receive,
        'keyword': keyword_receive
    }
    print(title_receive, pw_receive, place_receive, time_receive, desc_receive, todo_receive, keyword_receive)

    db.meeting.insert_one(doc)

    return jsonify({'result': 'success', 'msg': '작성 완료'})


@app.route('/meeting', methods=['GET'])
def meeting_desc():
    meeting = list(db.meeting.find({}, {'_id': False, 'pw': False}))
    return jsonify({'result': 'success', 'all_meetings': meeting})


@app.route('/api/delete', methods=['POST'])
def meeting_delete():
    id = request.form['id']
    pw = request.form['pw']
    db.meeting.delete_one({'id': int(id), 'pw': pw})
    return jsonify({'result': 'success', 'msg': '모임이 삭제되었습니다.'})


@app.route('/api/modify', methods=['POST'])
def meeting_modify():

    # 수정된 글 정보를 입력받음
    id = request.form['id']
    # 비밀번호도 입력받아야함
    title_receive = request.form['title_give']
    pw_receive = request.form['pw_give']
    place_receive = request.form['place_give']
    time_receive = request.form['time_give']
    desc_receive = request.form['desc_give']
    todo_receive = request.form['todo_give']
    keyword_receive = request.form['keyword_give']

    meetings = db.meeting.find_one({'id': int(id), 'pw': pw_receive})

    if meetings is not None:
        newDoc = {
            'title': title_receive,
            'pw': pw_receive,
            'place': place_receive,
            'time': time_receive,
            'desc': desc_receive,
            'todo': todo_receive,
            'keyword': keyword_receive
        }

        db.meeting.update_one({'id': int(id)}, {'$set': newDoc})
        return jsonify({'result': 'success', 'msg': '수정이 완료되었습니다.'})

    else:
        return jsonify({'result': 'fail', 'msg': '비밀번호가 일치하지 않습니다.'})







@app.route('/api/auth', methods=['POST'])
def meeting_auth():
    id = request.form['id']
    pw = request.form['pw']
    # id와 pw가 일치하는 meeting이 있는지 확인
    meeting = db.meeting.find_one({'id': int(id), 'pw': pw})
    if meeting is None:
        # 일치하지 않는 경우 return fail
        return jsonify({'result': 'fail'})
    else:
        # 일치하는 경우 return success
        return jsonify({'result': 'success'})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)