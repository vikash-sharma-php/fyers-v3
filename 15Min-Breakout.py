#Strategy 15 min breakout
#Entry Breakout Above or below 15 min
#Exit/SL- Cross back opposite sid of the candle

import time
from fyers_apiv3 import fyersModel
from fyers_apiv3.FyersWebsocket import data_ws
from utility import *
from login import *
from datetime import datetime,timedelta

current_date = datetime.now()
previous_date = current_date - timedelta(days=1)
formatted_current_date = current_date.strftime("%Y-%m-%d")
formatted_previous_date = previous_date.strftime("%Y-%m-%d")

client_id = get_clientId()
token = get_token()
fyers_obj = fyersModel.FyersModel(client_id=client_id, token=token)

symbol = "NSE:RELIANCE-EQ"
symbolData = get_symbol_date(symbol,"15","1",formatted_previous_date,formatted_previous_date,"1")

data = fyers_obj.history(data=symbolData)
print("Response history data ::",data)
high_price = float(data['candles'][0][2])
low_price =  float(data['candles'][0][3])
print("Response:", data)
print("High Price ::",high_price)
print("Low Price ::",low_price)
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
def onmessage(message):
    print("Response:", message)
    global fs,is_break_hig,is_break_low,stop_loss,option_symbol,call_symbol,put_symbol,call_put_symbol

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

