from bs4 import BeautifulSoup
import requests
import pandas as pd


# url = 'https://www.glassdoor.co.in/Reviews/index.htm'

def WebsitePage(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code < 200 or response.status_code > 299:
        raise Exception(f'Failed to load the page {url}')
    page_content = response.text
    webpage =  BeautifulSoup(page_content, 'html.parser')
    return webpage, response


def DataExtractor(WebsitePage):
    companynames = []
    CompanyNameClass = "align-items-center mb-xsm"
    CompanyName = WebsitePage.find_all('span', {"class":CompanyNameClass})
    for name in CompanyName:
        companynames.append(name.text[:-4])

    companysizes = []
    CompanySizeClass = "d-block mt-0 css-56kyx5"
    ComapanySize = WebsitePage.find_all('span', {'class':CompanySizeClass, 'data-test':'employer-size'})
    for size in ComapanySize:
        companysizes.append(size.text[:-9].strip())

    domains = []
    CompanyIndustryClass = "d-block mt-0 css-56kyx5"
    CompanyIndustry = WebsitePage.find_all('span', {'class':CompanyIndustryClass, "data-test":"employer-industry"})
    for domain in CompanyIndustry:
        domains.append(domain.text)

        

    return domains







if __name__ == "__main__":
    url = 'https://www.glassdoor.co.in/Reviews/index.htm'
    webpage, response = WebsitePage(url)
    data = DataExtractor(webpage)
    print(response)
    print(data)




