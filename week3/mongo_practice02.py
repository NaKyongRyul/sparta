from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta_ninework

target_movie = db.movies.find_one({'title': '월-E'})
target_star = target_movie['star']


db.movies.update_many({'star': target_star}, {'$set': {'star': '0'}})


print('hello github')
