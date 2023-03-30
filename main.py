from scrape import scrape_main

q=input("Enter your job title: ")
print(scrape_main.getSkills(q))


# from config import config
# print(config.chromeDriverPath)
# print(config.mongoDbURL)