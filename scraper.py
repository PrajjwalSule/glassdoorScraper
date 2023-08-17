from bs4 import BeautifulSoup
import requests
import pandas as pd


# url = 'https://www.glassdoor.co.in/Reviews/index.htm'

def WebsitePage(url):
    # This function configure the web page
    headers = {'User-Agent': 'Mozilla/5.0 (Ubuntu; Linux x86_64; Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.status_code < 200 or response.status_code > 299:
        raise Exception(f'Failed to load the page {url}')
    page_content = response.text
    webpage =  BeautifulSoup(page_content, 'html.parser')
    return webpage, response


def DataExtractor(WebsitePage):
    # This function will extract all the necessary information from configured page.
    CompanyNames = []
    try:
        CompanyNameClass = "align-items-center mb-xsm"
        CompanyName = WebsitePage.find_all('span', {"class":CompanyNameClass})
        for name in CompanyName:
            CompanyNames.append(name.text[:-4])
    except Exception as e:
        print(e)

    CompanySizes = []
    try:
        CompanySizeClass = "d-block mt-0 css-56kyx5"
        ComapanySize = WebsitePage.find_all('span', {'class':CompanySizeClass, 'data-test':'employer-size'})
        for size in ComapanySize:
            CompanySizes.append(size.text[:-9].strip())
    except Exception as e:
        print(e)

    CompanyDomains = []
    try:
        CompanyIndustryClass = "d-block mt-0 css-56kyx5"
        CompanyIndustry = WebsitePage.find_all('span', {'class':CompanyIndustryClass, "data-test":"employer-industry"})
        for domain in CompanyIndustry:
            CompanyDomains.append(domain.text)
    except Exception as e:
        print(e)

    CompanyReviews = []
    try:
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
    except Exception as e:
        print(e)

    
    CompanySalaries = []
    try:
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
    
    except Exception as e:
        print(e)


    CompanyJobs = []
    try:
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
    
    except Exception as e:
        print(e)


    CompanyRatings = []
    try:
        CompanyRatingClass = "pr-xsm ratingsWidget__RatingsWidgetStyles__rating"
        CompanyRating = WebsitePage.find_all('span',{'class':CompanyRatingClass, "data-test":"rating"})
        for rating in CompanyRating:
            CompanyRatings.append(float(rating.text))
    except Exception as e:
        print(e)


    comapanylocations = []
    try:
        CompanyLocationClass = "d-block mt-0 css-56kyx5"
        CompanyLocation = WebsitePage.find_all('span', {'class':CompanyLocationClass, "data-test":"employer-location"})
        for location in CompanyLocation:
            comapanylocations.append(int(location.text[:3].strip()))
    except Exception as e:
        print(e)


    # make a dataframe
    company_dict = {
        'Company':CompanyNames,
        'Size' : CompanySizes,
        'Industry':CompanyDomains,
        'Salaries':CompanySalaries,
        'Jobs' :CompanyJobs,
        'Rating': CompanyRatings,
        'Location': comapanylocations,
        'Review':CompanyReviews
    }

    CompanyDataFrame = pd.DataFrame(company_dict)
    
    
    return CompanyDataFrame


def CSVMaker(dataframe, filename):
    # This function will make the dataframe into csv file
    dataframe.to_csv(f"{filename}.csv", index=None)




if __name__ == "__main__":
    url = 'https://www.glassdoor.co.in/Reviews/index.htm'
    webpage, response = WebsitePage(url)
    data = DataExtractor(webpage)

    CSVMaker(data, 'CompaniesData')
    print(response)




