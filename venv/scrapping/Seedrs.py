from bs4 import BeautifulSoup
import urllib2


url = "https://www.seedrs.com/tanorganic"
page = urllib2.urlopen(url)
soup = BeautifulSoup(page.read(), "html.parser")

target = soup.find("dl", class_="investment_sought")
print target.text

figure = target.find("dd").text
print figure
