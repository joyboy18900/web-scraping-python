import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:84.0) Gecko/20100101 Firefox/84.0",
}

result_news = {}
result_news["news_details"] = []
term = '\"1mill\"'
current_page = 1
page = requests.get('https://html.duckduckgo.com/html/?q='+ term +' -site:facebook.com -site:instagram.com&s='+str(current_page*30)+'&dc='+str(current_page*30+1), headers=headers).text
main_result = BeautifulSoup(page, "html.parser")

for container in main_result.findAll('div', class_='result results_links results_links_deep web-result'):
    news_heading = container.find('a', class_='result__a').text
    news_desc = container.find('a', class_='result__snippet').text
    news_link_url = container.find('a', class_='result__url')['href']
    news_link_text = container.find('a', class_='result__url').text
    news_link_icon = container.find('img', class_='result__icon__img')['src']
    result_news['news_details'].append({
      'news_heading': news_heading,
      'news_snippet': news_desc,
      'news_link': news_link_url.strip(),
      'news_soruce': news_link_text.strip(),
      'news_icon': news_link_icon.strip()
    })

print(result_news)
