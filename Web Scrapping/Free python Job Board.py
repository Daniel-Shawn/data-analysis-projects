from bs4 import BeautifulSoup
import requests
import pandas as pd, numpy as np


# List/ Array for all the jobs.
#it will contain a dictionary of the details
job_list = []

response = requests.get('https://pythonjobs.github.io/')
soup = BeautifulSoup(response.content, 'html.parser')


#function for returning a dictionary
def create_dict(title, date, type, company, link):
    job_list.append(
        {
            'title': title,
            'date': date,
            'type': type,
            'company': company,
            'link': link
        }
    )




all_jobs = soup.find_all('div', class_='job')

for each_job in all_jobs:
    job_name = each_job.find('h1')
    #extracting link from the h1 title
    job_link = job_name.find('a')['href']
    job_name = job_name.text
    job_date = each_job.find_all('span', class_='info')[1]
    job_date = job_date.text
    job_type = each_job.find_all('span', class_='info')[2]
    job_type = job_type.text
    job_company = each_job.find_all('span', class_='info')[3]
    job_company = job_company.text
    job_location = each_job.find_all('span', class_='info')[0]
    job_location = job_location.text
    create_dict(job_name, job_date, job_type, job_company, job_link)


print(job_list)