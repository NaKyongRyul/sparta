from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 설치 먼저 해야겠죠?)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.

# MongoDB에 insert 하기

# 'users'라는 collection에 데이터를 생성합니다.
db.users.insert_one({'name': '덤블도어', 'age': 116})
db.users.insert_one({'name': '맥고나걸', 'age': 85})
db.users.insert_one({'name': '스네이프', 'age': 60})
db.users.insert_one({'name': '해리', 'age': 40})
db.users.insert_one({'name': '허마이오니', 'age': 40})
db.users.insert_one({'name': '론', 'age': 40})