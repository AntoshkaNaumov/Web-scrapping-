# Необходимо парсить страницу со свежими статьями и выбирать те статьи,
# в которых встречается хотя бы одно из ключевых слов (эти слова определяем в начале скрипта).
# Поиск вести по всей доступной preview-информации (это информация, доступная непосредственно с текущей страницы).
# Вывести в консоль список подходящих статей в формате: <дата> - <заголовок> - <ссылка>.

import requests
import bs4

HEADERS = {
    'Cookies': 'yandexuid=7872100861644332491; yuidss=7872100861644332491; my=YwA=; ymex=1972109901.yrts.1656749901;'
               ' yandex_gid=117428; gdpr=0; _ym_uid=1645464466702207110; amcuid=4972560311656757599;'
               ' is_gdpr=1; is_gdpr_b=CNzDcxCdfBgBKAI=; _ym_d=1657306071;'
               ' i=63x9hmXsEdY2Rm98G9IlyFPzf/tqOHgDmb0okoZ4J4X5vjVpzciz81TK0wfRR6Ml0qbobFAs0hr37Rm50XqmbH79DMY=;'
               ' cycada=jC8elBVjyes7g2aKMvnupxSWf2EiKnaLQUudBH8T9PU=; yabs-sid=196879461657384365',
    'Acceept-Language': 'ru-RU,ru;q=0.9',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'no-cors',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-User': '?1',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/103.0.0.0 Safari/537.36',
    'sec-ch-ua-mobile': '?0'}

# определяем список ключевых слов
KEYWORDS = {'дизайн', 'фото', 'web', 'Python'}

base_url = 'https://habr.com'
url = base_url + '/ru/all/'
response = requests.get(url, headers=HEADERS)
text = response.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    previews = article.find_all('div', class_='article-formatted-body article-formatted-body article-formatted-body_version-2')
    previews = set(preview.find('p').text for preview in previews)
    previews = {i for i in str(previews).split()}
    date = article.find('time').text
    title = article.find('a', class_='tm-article-snippet__title-link')
    href = title['href']
    span_title = title.find('span').text
    if KEYWORDS & previews:
        result = f'Название cтатьи => {span_title} / Дата статьи {date} / Ссылка {base_url + href}'
        print(result)


