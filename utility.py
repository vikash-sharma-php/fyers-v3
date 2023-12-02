def get_trade_input_option(ltp, option_symbol,call_type,side,ordered_symbol,qty):
    if len(str(int(ltp))) < 5:
        default_round = -1
    else:
        default_round = -2
    round_to_strike = int(round(float(ltp), default_round))
    if len(ordered_symbol) == 0:
        ordering_symbol = str(option_symbol) + str(round_to_strike) + call_type
    else:
        ordering_symbol=ordered_symbol
    trade = {
        "symbol": ordering_symbol,
        "qty": qty,
        "type": 2,
        "side": side,
        "productType": "CNC",  # INTRADAY,CNC
        "limitPrice": 0,
        "stopPrice": 0,
        "disclosedQty": 0,
        "offlineOrder": "False",
        "stopLoss": 0,
        "takeProfit": 0}
    return trade

def get_symbol_date(symbol,resolution,date_format,range_from,range_to,cont_flag):
    symbolData= {
    "symbol": symbol,
    "resolution": resolution,
    "date_format": date_format,
    "range_from": range_from,
    "range_to": range_to,
    "cont_flag": cont_flag}
    print("Input Data :: ",symbolData)
    return  symbolData

def get_trade_input_equity(ltp, symbol,qty,type,side,prduct_type,limt_price,stop_price,stop_loss,take_profit):
    trade = {
        "symbol": symbol,
        "qty": qty,
        "type": 2,
        "side": side,
        "productType": prduct_type ,  # "INTRADAY","CNC"
        "limitPrice": limt_price,
        "stopPrice": stop_price,
        "disclosedQty": 0,
        "offlineOrder": "False",
        "stopLoss": stop_loss,
        "takeProfit": take_profit}
    return trade




