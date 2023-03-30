from scrape import scrape_main

q=input("Enter your job title: ")
print(scrape_main.getSkills(q,1))
q=input("Enter your job title: ")
print(scrape_main.getSkills(q,1))


# from config import config
# print(config.chromeDriverPath)
# print(config.mongoDbURL)

# from dbms import mdb
# print(mdb.queryList("test1"))