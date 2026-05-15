from bs4 import BeautifulSoup
import requests
x=input()
res = requests.get("https://www.google.com/search?q=" + x)
html = BeautifulSoup(res.text, "html.parser")
name_list = html.findAll("h3")
for tag in name_list:
    print(tag.text)
    url = tag.find_previous("a")["href"]
    print(url)
    print() 
