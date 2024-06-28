import requests
from bs4 import BeautifulSoup as bs

# url = "http://localhost:5000/"
# response = requests.get(url)
# soup = bs(response.text, "html.parser")
# body = soup.find("body").text.strip()
# print(body)
# data = body.split()
# print(data)

txt = "one one was a race horse, two two was one too."

x = txt.replace("o", "t")
print(x)