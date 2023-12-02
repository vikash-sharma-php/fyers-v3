from configparser import ConfigParser
from fyers_apiv3 import fyersModel

config = ConfigParser()
config.read('config.ini')

client_id = config.get('FYERS_APP','client_id')
secret_key = config.get('FYERS_APP','secret_key')
redirect_uri = config.get('FYERS_APP','redirect_uri')
response_type = config.get('FYERS_APP','response_type')
grant_type = config.get('FYERS_APP','grant_type')
state = config.get('FYERS_APP','state')
# client_id = "IUV0GX1BP1-100"
# secret_key = "7AKQBV25FZ"
# redirect_uri = "http://127.0.0.1/"
# response_type = "code"
# grant_type = "authorization_code"

# Create a session model with the provided credentials
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type,
    grant_type=grant_type
)

# Generate the auth code using the session model
def generate_auth_code_url():
    generate_auth_code_url = session.generate_authcode()
    print("generate_auth_code_url :: " , generate_auth_code_url)

def get_access_token():
    auth_code = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkubG9naW4uZnllcnMuaW4iLCJpYXQiOjE3MDEzOTA2ODEsImV4cCI6MTcwMTQyMDY4MSwibmJmIjoxNzAxMzkwMDgxLCJhdWQiOiJbXCJ4OjBcIiwgXCJ4OjFcIiwgXCJ4OjJcIiwgXCJkOjFcIiwgXCJkOjJcIiwgXCJ4OjFcIiwgXCJ4OjBcIl0iLCJzdWIiOiJhdXRoX2NvZGUiLCJkaXNwbGF5X25hbWUiOiJYUjIzMTk0Iiwib21zIjoiSzEiLCJoc21fa2V5IjoiZDE1NzlmZTVmMjhmZmJkNzgwNjM0NWE5MDA1ZWJhMGViNmRlMmQwZDcwOTkwZWEyY2ZkYmI3YzEiLCJub25jZSI6IiIsImFwcF9pZCI6IklVVjBHWDFCUDEiLCJ1dWlkIjoiYzQ2MTIyMzA5NGQwNDIwYzg0YTZiOGIxMTRjMDJjZWYiLCJpcEFkZHIiOiIwLjAuMC4wIiwic2NvcGUiOiIifQ.GecFJapvdG1Rkqm-GiFK2jZPXvK8e6PmamylmYybHrA"
    session.set_token(auth_code)
    response = session.generate_token()
    access_token = response['access_token']
    print('acess token :: ' , access_token)

def get_clientId():
    config = ConfigParser()
    config.read('config.ini')
    client_id = config.get('FYERS_APP', 'client_id')
    return client_id

def get_token():
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE3MDEzOTA3NTgsImV4cCI6MTcwMTQ3NzAzOCwibmJmIjoxNzAxMzkwNzU4LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCbGFTbW1VSEg5cFJNRGh6eEt5RG5zbWhyQmR2X1MtU2tyUFplVmRCeWNCTFh6Q0dXV0I0NDd5VVM0dW9BYTB2cjZnbkUzNDdOUmFnbE1lNDRLSlNwTExfYlFpSS1NanhGWl9KaVptZ09aS2JsY1lPUT0iLCJkaXNwbGF5X25hbWUiOiJSQUpFRVYgUkFOSkFOIEtBTUFUIiwib21zIjoiSzEiLCJoc21fa2V5IjoiZDE1NzlmZTVmMjhmZmJkNzgwNjM0NWE5MDA1ZWJhMGViNmRlMmQwZDcwOTkwZWEyY2ZkYmI3YzEiLCJmeV9pZCI6IlhSMjMxOTQiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.pYQ8cKVZ9vk4mfkbaVV28epsK8U-HSZJDmzdOrgEHls"
    return token

def get_profile_info():
    access_token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE3MDEzOTA3NTgsImV4cCI6MTcwMTQ3NzAzOCwibmJmIjoxNzAxMzkwNzU4LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCbGFTbW1VSEg5cFJNRGh6eEt5RG5zbWhyQmR2X1MtU2tyUFplVmRCeWNCTFh6Q0dXV0I0NDd5VVM0dW9BYTB2cjZnbkUzNDdOUmFnbE1lNDRLSlNwTExfYlFpSS1NanhGWl9KaVptZ09aS2JsY1lPUT0iLCJkaXNwbGF5X25hbWUiOiJSQUpFRVYgUkFOSkFOIEtBTUFUIiwib21zIjoiSzEiLCJoc21fa2V5IjoiZDE1NzlmZTVmMjhmZmJkNzgwNjM0NWE5MDA1ZWJhMGViNmRlMmQwZDcwOTkwZWEyY2ZkYmI3YzEiLCJmeV9pZCI6IlhSMjMxOTQiLCJhcHBUeXBlIjoxMDAsInBvYV9mbGFnIjoiTiJ9.pYQ8cKVZ9vk4mfkbaVV28epsK8U-HSZJDmzdOrgEHls"
    fyers = fyersModel.FyersModel(client_id=client_id, token=access_token)
    profile = fyers.get_profile()
    funds = fyers.funds()
    print("Profile :: ", profile,"Funds :: ",funds)



if __name__== "__main__":
    #generate_auth_code_url()
    #get_access_token()
    get_profile_info()