from bs4 import BeautifulSoup
import requests
import csv

#  creating csv file
file = open('hacker_news.csv', 'w', newline='')
writer = csv.writer(file)
writer.writerow(["title", "link"])

#  preparing the soup
URL = "https://news.ycombinator.com/"
response = requests.get(url=URL)
for_soup = response.text
soup = BeautifulSoup(for_soup, "html.parser")

#  cooking the soup
useful_infos = soup.find_all(name="a", rel="noreferrer")
site_sources = soup.find_all(name="span", class_="sitestr")
scores = soup.find_all(name="span", class_="score")

for _ in useful_infos:
    link = _.get("href")
    title = _.getText()
    writer.writerow([title, link])

file.close()
