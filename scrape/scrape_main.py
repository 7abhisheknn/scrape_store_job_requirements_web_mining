from scrape import naukri
from scrape import simply_hired
from dbms import mdb
import time

def getSkills(searchString, noOfPages=5):
    l=mdb.queryList(searchString)
    if l!=[]:
        return l
    skills = naukri.naukri(searchString, noOfPages)
    skills.extend(simply_hired.simplyHired(searchString, noOfPages))
    
    mdb.insert(searchString, skills)
    return skills