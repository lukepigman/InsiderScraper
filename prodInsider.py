
import alpaca_trade_api as tradeapi
from google.auth.transport.requests import Request
import scraper
import math
import time
from datetime import date
import creds
import utils

user = creds.key
pwd = creds.password
url = creds.url
api = tradeapi.REST(user, pwd, url)

def start():
    count = 0
    while 1 > 0:
        stock = scraper.scrape()
        executeStock(stock)
        print(count)
        count = count + 1
        time.sleep(30)
        


def executeStock(stock):
    positions = api.list_positions()
    ownedStocks =[]
    for position in positions:
        ownedStocks.append(position.symbol)
    orders = api.list_orders(status='all',limit=10)
    orderedAlreadyList =[]
    today = date.today().strftime('%Y-%m-%d')
    for order in orders:
        if(str(order.submitted_at)[:10] == today):
            orderedAlreadyList.append(order.symbol)
        
    bp= api.get_account().buying_power
    allotmentPerStock = float(bp) * utils.percentOfBP
    dontBuyList = ownedStocks + orderedAlreadyList
    dontBuyList = set(dontBuyList)
    if stock not in dontBuyList:
        try:
            symbol_bars = api.get_barset(stock, 'minute', 1).df.iloc[0]
            symbol_price = symbol_bars[stock]['close'] 
            quantity = math.floor(round(allotmentPerStock) / symbol_price)
            api.submit_order(
            symbol=stock,
            qty=quantity,
            side='buy',
            type='limit',
            time_in_force='day',
            limit_price=symbol_price + .01
            # order_class='bracket',
            # stop_loss={'stop_price': symbol_price * 0.97,
            #         'limit_price':  symbol_price * 0.96},
            # take_profit={'limit_price': symbol_price * 1.06}
        )
            print('order placed')
        except Exception:
            print('order not placed')
    else:
        print("no new stock to buy")

start()