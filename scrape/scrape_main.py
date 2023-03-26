from scrape import naukri

def getSkills(searchString):
    skills = naukri.naukri(searchString)
    return skills