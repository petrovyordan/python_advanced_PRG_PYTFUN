# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 09:54:39 2022

@author: Yordan.Petrov
"""

"""BITCOIN PRICE LIVE"""
import json
import datetime
import websocket

# plot each new data record - True or False
class BitcoinPrice():
    def __init__(self, url, time_interval=60, verbose=False):
        self.url = url
        self.time_interval = time_interval
        self.verbose = verbose
        self.prices_list = []
        self.timestamps_list = []
        self.volumes_list = []
        self.volumes_prices_products_list = []
        self.total_volumes = []
        self.last_time = datetime.datetime.now()
        self.vwap = 0
        
    def on_message(self, ws, message):
        # get tha data from source
        json_message = json.loads(message)
        
        # extract and insert into lists respectively - price, timestamp, volume
        json_data = json_message['data'][0]
        self.prices_list.append(json_data["p"])
        self.timestamps_list.append(json_data["t"])
        self.volumes_list.append(json_data["v"])
        
        # print current record - depends on if variable "verbose" is True or False
        if self.verbose:
            print(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} price:{json_data['p']} volume:{json_data['v']}")
        
        # time interval - in seconds
        if datetime.datetime.now().second % self.time_interval == 0:
            # get the required price values
            max_price = max(self.prices_list)
            min_price = min(self.prices_list)
            closing_price = self.prices_list[-1]
            
            # calculate TypicalPrice
            typical_price = (max_price + min_price + closing_price) / 3
            
            # Calculate traded volume
            current_volume = sum(self.volumes_list)
            self.total_volumes.append(self.current_volume)
            volume_price_product = typical_price * current_volume
            
            self.volumes_prices_products_list.append(self.volume_price_product)
            
            # Calculate VWAP value
            self.vwap = sum(self.volumes_prices_products_list) / sum(self.total_volumes)
            
            print("VWAP is:")
            print(self.vwap)
            
            # Clear the lists
            self.prices_list.clear()
            self.timestamps_list.clear()
            self.volumes_list.clear()
    
    
    def on_error(self, ws, error):
        """prints the errors"""
        print(error)
    
    
    def on_close(self, ws):
        """on closing connection"""
        print("### closed ###")
    
    
    def on_open(self, ws):
        """opening connection"""
        ws.send('{"type":"subscribe","symbol":"BINANCE:BTCUSDT"}')
    
    
    def run_websocket(self):
        ws = websocket.WebSocketApp(url=self.url,
                                    on_message=self.on_message,
                                    on_error=self.on_error,
                                    on_close=self.on_close)
        ws.on_open = on_open
        ws.run_forever()


# url and token
url = "wss://ws.finnhub.io?token=c7n5o62ad3iabvejri30"
B = BitcoinPrice(url, 60, True)
B.run_websocket()