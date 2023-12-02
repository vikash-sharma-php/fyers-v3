from fyers_apiv3.FyersWebsocket import data_ws


def onmessage(message):
    """
    Callback function to handle incoming messages from the FyersDataSocket WebSocket.

    Parameters:
        message (dict): The received message from the WebSocket.

    """
    print("Response:", message)


def onerror(message):
    """
    Callback function to handle WebSocket errors.

    Parameters:
        message (dict): The error message received from the WebSocket.


    """
    print("Error:", message)


def onclose(message):
    """
    Callback function to handle WebSocket connection close events.
    """
    print("Connection closed:", message)


def onopen():
    """
    Callback function to subscribe to data type and symbols upon WebSocket connection.

    """
    # Specify the data type and symbols you want to subscribe to
    data_type = "SymbolUpdate"

    # Subscribe to the specified symbols and data type
    symbols = ['NSE:SBIN-EQ', 'NSE:ADANIENT-EQ' , 'NSE:NIFTYBANK-INDEX']
    fyers.subscribe(symbols=symbols, data_type=data_type)

    # Keep the socket running to receive real-time data
    fyers.keep_running()


# Replace the sample access token with your actual access token obtained from Fyers
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE3MDEzOTA3NTgsImV4cCI6MTcwMTQ3NzAzOCwibmJmIjoxNzAxMzkwNzU4LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCbGFTbW1VSEg5cFJNRGh6eEt5RG5zbWhyQmR2X1MtU2tyUFplVmRCeWNCTFh6Q0dXV0I0NDd5VVM0dW9BYTB2cjZnbkUzNDdOUmFnbE1lNDRLSlNwTExfYlFpSS1NanhGWl9KaVptZ09aS2JsY1lPUT0iLCJkaXNwbGF5X25hbWUiOiJSQUpFRVYgUkFOSkFOIEtBTUFUIiwib21zIjoiSzEiLCJoc21fa2V5IjoiZDE1NzlmZTVmMjhmZmJkNzgwNjM0NWE5MDA1ZWJhMGViNmRlMmQwZDcwOTkwZWEyY2ZkYmI3YzEiLCJmeV9pZCI6IlhSMjMxOTQiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.pYQ8cKVZ9vk4mfkbaVV28epsK8U-HSZJDmzdOrgEHls"

# Create a FyersDataSocket instance with the provided parameters
fyers = data_ws.FyersDataSocket(
    access_token=access_token,  # Access token in the format "appid:accesstoken"
    log_path="",  # Path to save logs. Leave empty to auto-create logs in the current directory.
    litemode=False,  # Lite mode disabled. Set to True if you want a lite response.
    write_to_file=False,  # Save response in a log file instead of printing it.
    reconnect=True,  # Enable auto-reconnection to WebSocket on disconnection.
    on_connect=onopen,  # Callback function to subscribe to data upon connection.
    on_close=onclose,  # Callback function to handle WebSocket connection close events.
    on_error=onerror,  # Callback function to handle WebSocket errors.
    on_message=onmessage  # Callback function to handle incoming messages from the WebSocket.
)

# Establish a connection to the Fyers WebSocket
fyers.connect()

