import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://sports.news.naver.com/kbaseball/record/index.nhn?category=kbo', headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

trs = soup.select('#regularTeamRecordList_table > tr')

for tr in trs:
    title = tr.select_one('td.tm > div > span').text #---> 여기서 span은 알아서 적어야 하는건가요?
    rank = tr.select_one('th').text
    print(rank, title)
