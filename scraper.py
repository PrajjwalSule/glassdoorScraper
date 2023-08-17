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

    companydomains = []
    CompanyIndustryClass = "d-block mt-0 css-56kyx5"
    CompanyIndustry = WebsitePage.find_all('span', {'class':CompanyIndustryClass, "data-test":"employer-industry"})
    for domain in CompanyIndustry:
        companydomains.append(domain.text)

    companyreviews = []
    CompanyReviewClass = "mt-xsm mt-md-0"
    CompanyReview = WebsitePage.find_all('h3',{'class':CompanyReviewClass, "data-test":"cell-Reviews-count"})
    for review in CompanyReview:
        if review.text[-1] == "L":
            newreview = review.text[::-1]
            newreview = float(newreview[1:])
            updatedreview = newreview * 1000000
        elif review.text[-1] == "T":
            newreview = review.text[::-1]
            newreview = float(newreview[1:])
            updatedreview = newreview * 1000

        companyreviews.append(int(updatedreview))

    
    companysalaries = []
    CompanySalaryClass = "mt-xsm mt-md-0"
    CompanySalary = WebsitePage.find_all('h3', {'class':CompanySalaryClass, 'data-test':"cell-Salaries-count"})
    for salary in CompanySalary:
        if salary.text[-1] == "L":
            newsalary = salary.text[::-1]
            newsalary = float(newsalary[1:])
            updatedsalary = newsalary * 1000000
        elif salary.text[-1] == "T":
            newsalary = salary.text[::-1]
            newsalary = float(newsalary[1:])
            updatedsalary = newsalary * 1000

        companysalaries.append(int(updatedsalary))

    return companysalaries








if __name__ == "__main__":
    url = 'https://www.glassdoor.co.in/Reviews/index.htm'
    webpage, response = WebsitePage(url)
    data = DataExtractor(webpage)
    print(response)
    print(data)




