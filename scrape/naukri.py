from bs4 import BeautifulSoup
from selenium import webdriver
import time

def naukriURL(searchString):
    template = "https://www.naukri.com/{}-jobs"
    searchString = searchString.replace(' ', '-')
    url = template.format(searchString)
    return url

def naukri(searchString):
    driver = webdriver.Chrome("C:\\WebDrivers\\chromedriver_win32\\chromedriver.exe")
    URL = naukriURL(searchString)
    driver.get(URL)
    time.sleep(2)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    jobListDiv=soup.find(class_='list')
    jobArticleList = jobListDiv.find_all('article',class_='jobTuple')
    jobURLList=[]
    for jobArticle in jobArticleList:
        jobURLList.append(jobArticle.find('a', class_='title ellipsis').get('href'))

    skills=[]
    for jobURL in jobURLList:
        driver.get(jobURL)
        time.sleep(2)
        soupJob = BeautifulSoup(driver.page_source, 'html.parser')
        keySkillDiv = soupJob.find(class_='key-skill')
        keySkillSpanList = keySkillDiv.find_all('span')
        for keySkillSpan in keySkillSpanList:
            skills.append(keySkillSpan.text)
    driver.close()
    return skills
