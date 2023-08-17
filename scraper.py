from bs4 import BeautifulSoup
import requests


# url = 'https://www.glassdoor.co.in/Reviews/index.htm'

def WebsitePage(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code < 200 or response.status_code > 299:
        raise Exception(f'Failed to load the page {url}')
    page_content = response.text
    webpage =  BeautifulSoup(page_content, 'html.parser')
    return webpage, response






# if __name__ == "__main__":
#     url = 'https://www.glassdoor.co.in/Reviews/index.htm'
#     a,b = topic_page_authentication(url)
#     print(b)




