import requests
from bs4 import BeautifulSoup


"""
This python code scrapes the web, specifically the Fake jobs site and returns the content
"""



page = requests.get('https://realpython.github.io/fake-jobs/')

#Returns the HTML skeleton
html = page.text


#Parsing the html content through beautiful soup
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="ResultsContainer")


# Scrapping the job titles, companies and locations from the website
list_of_jobs = results.find_all("div", class_="card-content")
for each in list_of_jobs:
    #print(each.find("h2", class_="title").text)
    #print(each.find("h3", class_="company").text)
    #print(each.find("p", class_="location").text)
    title = each.find("h2", class_="title").text
    company = each.find("h3", class_="subtitle is-6 company").text
    location = each.find("p", class_="location").text


#finding a particular string from the scrapped data
python_jobs = results.find_all(
    "h2", string=lambda text: "python" in text.lower()
)


#finding the parent element of a particular element
for each_h2_element in python_jobs:
    python_job_element = each_h2_element.parent.parent.parent



# Finding links in the webpage
job_element_count = 1
for job_element in list_of_jobs:
    links = job_element.find_all("a")
    title = job_element.find("h2", class_="title").text
    for link in links:
        pass
        #print(f"{job_element_count}- Link for job {title}: {link['href']}\n")
    job_element_count += 1



# Finding the 'Apply' links in each job <div>
job_element_count = 1
for job_element in list_of_jobs:
    links = job_element.find_all("a")[1]['href']
    title = job_element.find("h2", class_="title").text
    #print(f"{job_element_count}- Link for job {title}: {links}\n")
    job_element_count += 1




