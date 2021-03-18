import requests
from lxml import html

def scrape():
    site = requests.get("http://www.openinsider.com/screener?s=&o=&pl=&ph=10&ll=&lh=&fd=14&fdr=&td=0&tdr=&fdlyl=&fdlyh=1&daysago=&xp=1&vl=25&vh=&ocl=&och=&sic1=-1&sicl=100&sich=9999&isceo=1&iscfo=1&grp=0&nfl=&nfh=&nil=&nih=&nol=&noh=&v2l=&v2h=&oc2l=&oc2h=&sortcol=0&cnt=100&page=1")
    tree = html.fromstring(site.content)
    stock = tree.xpath('//*[@id="tablewrapper"]/table/tbody/tr[1]/td[4]/b/a/text()')
    print(stock[0] + " scraped.")
    return stock[0]