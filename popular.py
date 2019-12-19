import requests
import bs4

html = requests.get('https://www.naver.com/')
soup = bs4.BeautifulSoup(html.text, 'html.parser')

keywords = soup.select('span.ah_k')

# keywords = ['a', 'b', 'c']
# for keyword in keywords:
#     print(keyword.text)

# 배열[0:n] -> 배열의 0번째 인덱스부터 n-1번째
# 인덱스들의 요소를 가져와서 배열로 만든다.

real_keywords = keywords[0:20]
real_real_keywords = [keyword.text for keyword in real_keywords]

# 무엇이 1등인지 모르게 가나다순 정렬해버리기
problem = sorted(real_real_keywords)
print('아래 보기 중에서 1위를 고르세요')
print(problem)
answer = input('당신이 입력한 답: ')

# 배열[0] :배열의 첫번째요소
if answer == real_real_keywords[0]:
    print('정답입니다.')
else:
    print('오답입니다.')



# [0,1,2,3,...100]
# numbers = [i*2 for i in range(0,101)]
# print(numbers)

# numbers = []
# for i in range(0,101):
#     nembers.append(i)
# print(nembers)
