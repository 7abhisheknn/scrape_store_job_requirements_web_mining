from scrape import naukri
from scrape import simply_hired

def getSkills(searchString):
    skills = naukri.naukri(searchString)
    skills.extend(simply_hired.simplyHired(searchString))
    return skills