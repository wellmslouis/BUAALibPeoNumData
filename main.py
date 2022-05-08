from lxml.html import etree
import requests
from bs4 import BeautifulSoup
import time
import csv

def getHTMLText(url,headers):
    try:
        r = requests.get(url, headers,timeout=30)
        r.raise_for_status()  # 如果状态不是200，引发HTMLError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"

def get_num():
    url = "https://mlib.buaa.edu.cn/m-buaa-extension/index"
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43'}
    # content = requests.get(url, headers).content

    text = getHTMLText(url, headers)
    soup = BeautifulSoup(text, "lxml")
    # print(soup)

    num = soup.find("strong", class_="orange").text
    return str(num)



if __name__ == "__main__":
    txt_name = str(time.strftime('%Y-%m-%d', time.localtime(time.time())))+".csv"
    while True:
        file = open(txt_name, mode='a',newline="")
        csvfile=csv.writer(file)
        date=str(time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time())))+" "
        num=get_num()
        # line=date+num+"\n"
        line=[date,num]
        # file.write(line)
        csvfile.writerow(line)

        print(line,end="")
        file.close()
        time.sleep(60)
