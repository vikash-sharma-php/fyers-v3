#Strategy camarilla
#Exit/SL- Cross back opposite sid of the candle

import time
from fyers_apiv3 import fyersModel
from fyers_apiv3.FyersWebsocket import data_ws
from utility import *
from login import *
from datetime import datetime,timedelta
import pandas as pd


current_date = datetime.now()
previous_date = current_date - timedelta(days=2)
formatted_current_date = current_date.strftime("%Y-%m-%d")
formatted_previous_date = previous_date.strftime("%Y-%m-%d")

client_id = get_clientId()
token = get_token()
fyers_obj = fyersModel.FyersModel(client_id=client_id, token=token)

symbol = "NSE:RELIANCE-EQ"
symbolData = get_symbol_date(symbol,"15","1",formatted_previous_date,formatted_previous_date,"1")

data = fyers_obj.history(data=symbolData)
open_price = float(data['candles'][0][1])
high_price = float(data['candles'][0][2])
low_price =  float(data['candles'][0][3])
close_price= float(data['candles'][0][4])
volume = float(data['candles'][0][5])
print("Response:", data)
print("Open Price ::", open_price,"High Price ::",high_price , "Low Price ::",low_price ,"Close Price ::",close_price,low_price ,"Volume ::",volume )

time.sleep(2)
websocket_access_token = client_id+':'+token
data_type= "SymbolUpdate"

is_break_hig =  False
is_break_low = False
stop_loss = None

expiry= "23DEC"
option_symbol = symbol.split("-")[0] + expiry
call_symbol = ""
put_symbol = ""

# Function to fetch historical data and calculate Camarilla levels
def get_camarilla_levels(high,low,close):
    # Calculate Camarilla levels
    c_p = (high + low + close) / 3
    c=close
    h_l = high - low
    r5 = ((high/low)*close)
    r4 = int(c + 1.1 * h_l / 2)
    r3 = int(c + 1.1 * h_l / 4)
    r2 = int(c + 1.1 * h_l / 6)
    r1 = int(c + 1.1 * h_l / 12)
    s1 = int(c - 1.1 * h_l / 12)
    s2 = int(c - 1.1 * h_l / 6)
    s3 = int(c - 1.1 * h_l / 4)
    s4 = int(c - 1.1 * h_l / 2)
    s5 = (close-(r5-close))
    camarilla_data={'C': int(c_p),'R5':int(r5), 'R4': r4, 'R3': r3, 'R2': r2, 'R1': r1, 'S1': s1, 'S2': s2, 'S3': s3, 'S4': s4, 'S5':int(s5)}
    return camarilla_data

camarilla_data = get_camarilla_levels(high_price,low_price,close_price)

# Print the DataFrame with Camarilla levels
print("Camarilla Data ::",camarilla_data)
def onmessage(message):
    print("Response:", message)
    global fs,is_break_hig,is_break_low,stop_loss,option_symbol,call_symbol,put_symbol,call_put_symbol,camarilla_data

    if 'ltp' in message:
        ltp = float(message['ltp'])
        print("Last updated price :: ", ltp)
        if ltp>high_price and not is_break_hig:
            trade = get_trade_input_option(ltp,option_symbol,"CE",1,"",25)
            call_symbol= str(trade['symbol'])
            orderDetails = fyers_obj.place_order(data=trade)
            print("Input Message :: ", trade)
            print("Order placed :: ",orderDetails)
            is_break_hig = True
            is_break_low = False
            stop_loss  = low_price

        elif ltp<low_price and not is_break_low:
            trade = get_trade_input_option(ltp, option_symbol, "PE",1,"",25)
            put_symbol= str(trade['symbol'])
            orderDetails = fyers_obj.place_order(data=trade)
            print("Input Message :: ", trade)
            print("Order placed :: ", orderDetails)
            is_break_low = True
            is_break_hig = False
            stop_loss = high_price

        if is_break_hig and ltp<stop_loss:
            trade = get_trade_input_option(ltp,option_symbol,"CE",-1,call_symbol,25)
            orderDetails = fyers_obj.place_order(data=trade)
        elif is_break_low and ltp>stop_loss:
            trade = get_trade_input_option(ltp,option_symbol,"PE",-1,put_symbol,25)
            orderDetails = fyers_obj.place_order(data=trade)


fs = data_ws.FyersDataSocket(
    access_token=token,  # Access token in the format "appid:accesstoken"
    log_path="",  # Path to save logs. Leave empty to auto-create logs in the current directory.
    litemode=True,  # Lite mode disabled. Set to True if you want a lite response.
    write_to_file=False,  # Save response in a log file instead of printing it.
    reconnect=True,  # Enable auto-reconnection to WebSocket on disconnection.
    #on_connect=onopen,  # Callback function to subscribe to data upon connection.
    #on_close=onclose,  # Callback function to handle WebSocket connection close events.
    #on_error=onerror,  # Callback function to handle WebSocket errors.
    on_message=onmessage  # Callback function to handle incoming messages from the WebSocket.
)
fs.connect()
symbol = [symbol]
fs.subscribe(symbols=symbol,data_type=data_type)
fs.keep_running()

