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
    auth_code = "********"
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
    token = "****"
    return token

def get_profile_info():
    access_token="********"
    fyers = fyersModel.FyersModel(client_id=client_id, token=access_token)
    profile = fyers.get_profile()
    funds = fyers.funds()
    print("Profile :: ", profile,"Funds :: ",funds)



if __name__== "__main__":
    #generate_auth_code_url()
    #get_access_token()
    get_profile_info()
