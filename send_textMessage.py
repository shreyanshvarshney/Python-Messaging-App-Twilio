#hello friends, these modules are updated as of 2019 and written in python 3.5

from twilio.rest import Client

account_sid = '' #your twilio account sid 
auth_token = '' #your twilio account auth token number

# Find the above SID and auth_token at https://twilio.com/user/account

client = Client(account_sid, auth_token)

my_message = '' #type your message inside string quotations.
message = client.messages \
                .create(
                     body=my_message,
                     from_='+Your Twilio Number', #your twilio account phone number. For eg. +13341124123
                     to='+Receiver Cell Number'   #your friend phone number with country code. For eg. +913411241233
                 )

print(message.sid +" ,message sent successfully.")

#When you run it in python IDLE you will show up a SID. That means you successfully sent your message to receiver :)
#Remember you should login with your Twilio account first to send message.
