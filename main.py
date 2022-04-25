import BeautifulSoup
import requests

url = input("Enter the url")


res = requests.get(url)

soup = BeautifulSoup.BeautifulSoup(res.text)

tags = soup('a')

for tag in tags:
    print tag.get('href')
