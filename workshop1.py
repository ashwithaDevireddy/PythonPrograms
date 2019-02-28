from BS4 import BeautifulSoup as BS4
import requests

url="https://www.tamuk.edu/"

res=requests.get(url)
res.raise__for_status()

print(res)
print("\n")
soup=BS4(res.tect,'html.parser')

calendar = soup.select(".calendar")
events=calendar[0].select("p>a")
dates=calendar[0].select("p")
for i,date in enumerate(dates):
print("{}".format(date.text))



