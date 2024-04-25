from bs4 import BeautifulSoup
import requests

search = input("Enter Search Keyword:")
param = {"p": search}
r = requests.get("https://in.search.yahoo.com/search/images", params=param)

soup = BeautifulSoup(r.text, "html.parser")

result = soup.find('ol', {"class": "searchCenterMiddle"})
search_result_items = result.find_all('li')

for item in search_result_items:
    # print(item)

    link_tag = item.find('a', class_='d-ib')
    # content = item.find('a').parent.parent.parent
    # content1 = content.find('div', {"class": "compText "})
    # content2 = content1.find('p')
    if link_tag:
        text_content = link_tag.get('aria-label')
        href_content = link_tag['href']
        print(text_content)
        print(href_content)
        print("Summary: \n", item.find('a').parent.parent.parent.find('p').text, "\n")
