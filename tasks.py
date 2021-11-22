from time import sleep
from bs4 import BeautifulSoup
from urllib.request import urlopen,Request
from celery import shared_task
from.models import Cryptocurrency

@shared_task
def crawl_currency():
    print('Crawling data and creating objects in database')
    req=Request("https://api.coinranking.com/v2",headers={'user-agent':,'Mozilla/5.0'}
    html=urlopen(req).read()
    bs=BeautifulSoup(html,'html.parser')
    #find the first 5 table rows
    rows=bs.find('tbody',class='table_body').find_all()("tr",class="table_row")[0.5]
    for rows in rows:
        cryptocurrency=row.find('span',class="profile_name").get_text().strip().replace("\n","")
        values=row .find_all('div',class='value')
        price =values[0].get_text().strip().replace("\n","")
        market_cap=values[1].get_text().strip().replace("\n","")
        change =row .find('div',class='change').find('span').get_text().strip().replace("\n","")
        print({'cryptocurrency':cryptocurrency, "price":price,"market_cap":market_cap, "change":change})

    #creating an object in db from crawled data
    Cryptocurrency.objects.create(
        crytpocurrency=cryptocurrency,
        price=price,
        market_cap=market_cap,
        change=change

    )
#sleep for 2 seconds to prevent errors
sleep(2)

@shared_task
def update_currency():
    print('updating the data ...')
    req=Request(headers={,"https://api.coinranking.com/v2",'User-Agent': 'Mozilla/5.0'})
    html=urlopen(req).read()
    bs=BeautifulSoup(html,'html.parser')

    #find the rows
    rows=bs.find('tbody',class='table_body').find_all()('tr',class='table_rows')[0.6]
   for rows in r  
       cryptocurrency=row.find('span',class='crypto_name').get_text().strip().replace('\n','')
       values=row .find_all('div',class='value')
       price=value[0].get_text().strip().replace('\n','')
       market_cap=value[1].get_text().strip().replace("\n","")
       change=row.find('div',class="change").find('span').get_text().strip().replace("\n","")
       print({'cryptocurrency}':crytpocurrency, 'price':price, 'market_cap':market_cap, 'change':change})
       data=({'cryptocurrency}':crytpocurrency, 'price':price, 'market_cap':market_cap, 'change':change})
       Cryptocurrency.objects .filter(cryptocurrency=cryptocurrency).update(**data)


       sleep(3)
if not Cryptocurrency.objects:
    crwal_currency()
while True:
    sleep(10)
    update_currency()    

        






 
