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
    CompanyNames = []
    CompanyNameClass = "align-items-center mb-xsm"
    CompanyName = WebsitePage.find_all('span', {"class":CompanyNameClass})
    for name in CompanyName:
        CompanyNames.append(name.text[:-4])

    CompanySizes = []
    CompanySizeClass = "d-block mt-0 css-56kyx5"
    ComapanySize = WebsitePage.find_all('span', {'class':CompanySizeClass, 'data-test':'employer-size'})
    for size in ComapanySize:
        CompanySizes.append(size.text[:-9].strip())

    CompanyDomains = []
    CompanyIndustryClass = "d-block mt-0 css-56kyx5"
    CompanyIndustry = WebsitePage.find_all('span', {'class':CompanyIndustryClass, "data-test":"employer-industry"})
    for domain in CompanyIndustry:
        CompanyDomains.append(domain.text)

    CompanyReviews = []
    CompanyReviewClass = "mt-xsm mt-md-0"
    CompanyReview = WebsitePage.find_all('h3',{'class':CompanyReviewClass, "data-test":"cell-Reviews-count"})
    for review in CompanyReview:
        if review.text[-1] == "L":
            newreview = review.text[::-1]
            newreview = newreview[1:]
            newreview = float(newreview[::-1])
            updatedreview = newreview * 1000000

        elif review.text[-1] == "T":
            newreview = review.text[::-1]
            newreview = newreview[1:]
            newreview = float(newreview[::-1])
            updatedreview = newreview * 1000

        else:
            updatedreview = float(review.text)

        CompanyReviews.append(int(updatedreview))

    
    CompanySalaries = []
    CompanySalaryClass = "mt-xsm mt-md-0"
    CompanySalary = WebsitePage.find_all('h3', {'class':CompanySalaryClass, 'data-test':"cell-Salaries-count"})
    for salary in CompanySalary:
        if salary.text[-1] == "L":
            newsalary = salary.text[::-1]
            newsalary = newsalary[1:]
            newsalary = float(newsalary[::-1])
            updatedsalary = newsalary * 1000000

        elif salary.text[-1] == "T":
            newsalary = salary.text[::-1]
            newsalary = newsalary[1:]
            newsalary = float(newsalary[::-1])
            updatedsalary = newsalary * 1000

        else:
            updatedsalary = float(salary.text)


        CompanySalaries.append(int(updatedsalary))


    CompanyJobs = []
    CompanyJobClass = "mt-xsm mt-md-0"
    CompanyJob = WebsitePage.find_all('h3', {'class':CompanyJobClass, "data-test":"cell-Jobs-count"})
    for job in CompanyJob:
        if job.text[-1] == "L":
            newjob = job.text[::-1]
            newjob = newjob[1:]
            newjob = float(newjob[::-1])
            updatedjob = newjob * 100000

        elif job.text[-1] == "T":
            newjob = job.text[::-1]
            newjob = newjob[1:]
            newjob = float(newjob[::-1])
            updatedjob = newjob * 1000

        else:
            updatedjob = float(job.text)

        
        CompanyJobs.append(int(updatedjob))


    CompanyRatings = []
    CompanyRatingClass = "pr-xsm ratingsWidget__RatingsWidgetStyles__rating"
    CompanyRating = WebsitePage.find_all('span',{'class':CompanyRatingClass, "data-test":"rating"})
    for rating in CompanyRating:
        CompanyRatings.append(int(rating.text))


    comapanylocations = []
    CompanyLocationClass = "d-block mt-0 css-56kyx5"
    CompanyLocation = WebsitePage.find_all('span', {'class':CompanyLocationClass, "data-test":"employer-location"})
    for location in CompanyLocation:
        comapanylocations.append(int(location.text[:3].strip()))


    

    
    return CompanyRatings










if __name__ == "__main__":
    url = 'https://www.glassdoor.co.in/Reviews/index.htm'
    webpage, response = WebsitePage(url)
    data = DataExtractor(webpage)
    print(response)
    print(data)




