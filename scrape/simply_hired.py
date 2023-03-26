from bs4 import BeautifulSoup
from selenium import webdriver
import time

def simplyHiredURL(searchString):
    URL = "https://www.simplyhired.com/search?q=" + searchString
    