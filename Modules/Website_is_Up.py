# Python script to check wheather the site is up or not
# Request Module is the third party module we need to intsall it before importing 
# Command for importing it:- sudo apt install python3-requests


import requests
import bs4       # type: ignore #used for getting source code in pretified form 
import smtplib   # used for sending mails 

product_url = "https://www.lucioai.com/"

res = requests.get(product_url, timeout=5)
print(res)
print(dir(res))
print(res.status_code)
print(res.text)



product_url = "https://www.lucioai.com/"

res = requests.get(product_url, timeout=5)
if res.status_code != 200:
    pass

soup = bs4.BeautifulSoup(res.text)

ele = soup.select('#comp-lv7ztxae > p > span')
print(ele)