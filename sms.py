from twilio.rest import Client 
 
account_sid = 'AC187a5812fc9ae7828d81cd168515f83d' 
auth_token = '313b01651e9ec0ccb608febadd8ca9a5' 
client = Client(account_sid, auth_token) 
 
def Wa_sms():
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Hi Pinabai ',      
                              to='whatsapp:+919096560060'

                          ) 
 
    print(message.sid)
