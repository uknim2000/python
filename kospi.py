# 네이버 증시 페이지에 대신 접속해서
# 현재 코스피지수 가져오는 프로그램
import requests
import bs4

# 이 주소로 요청을 보내면 응답으로 html 파일이 도착할 것
html = requests.get('https://finance.naver.com/sise/sise_index.nhn?code=KOSPI')

# html text를 내가 보기 좋게 접근할 수 있도록 변경.
# #now_value는 네이버 코스피 사이트에서 코스피 넘버 '검사'로 찾아낸 값
soup = bs4.BeautifulSoup(html.text, 'html.parser')
kospi = soup.select_one('#now_value')

print(kospi.text)
