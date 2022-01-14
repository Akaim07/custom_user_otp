import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
def sendsms(otp,number):
    account_sid = 'ACcfb1cb3d80a88bffbf64c91b9cbdd815'
    auth_token = '1cd4f9136317d12262327fe9ff0c88af'
    Otp=otp
    client=Client(account_sid,auth_token)
 
    message = client.messages.create(
                     body='This is OTP Valid for 15 Minutes {}'.format(Otp),
                     from_='+17067706094',
                     to=number
                 )

    print('message has been send..')    
