import requests
from bs4 import BeautifulSoup

# AIRDOの運賃一覧ページのURL
url = 'https://www.airdo.jp/'

# ページの内容を取得
response = requests.get(url)
response.encoding = response.apparent_encoding  # 文字エンコーディングを適切に設定

# BeautifulSoupでHTMLを解析
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.prettify())

# 運賃情報が含まれるセクションを特定して抽出（サイト構造により適宜修正）
fares_section = soup.find('section', {'id': 'fares'})

if fares_section:
    fares = fares_section.find_all('div', class_='fare')

    for fare in fares:
        fare_name = fare.find('h3').text.strip()
        fare_details = fare.find('p').text.strip()
        print(f'運賃名: {fare_name}')
        print(f'詳細: {fare_details}')
        print('---')
else:
    print('運賃情報が見つかりませんでした。サイトの構造が変わった可能性があります。')
