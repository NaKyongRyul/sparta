import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=pnt&date=20200716',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser') #--> 파이썬이 html을 이해하도록 설정
tr_list = soup.select_one('#old_content > table > tbody > tr')
for tr in tr_list:
    rank_image = tr.select_one('td:nth-child(1) > img')
    title_image = tr.select_one('td.title > div > a')
    point_image = tr.select_one('td.point')
    if title is not None:
        name = title.text #--> <>  <> 안에 값을 가져오는거는 text 아닌거는 속성이라서 ['']안에 넣기


print('zzzzzz')


