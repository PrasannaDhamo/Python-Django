from twilio.rest import Client 
 
account_sid = 'AC72afce24613e859e132e13957f167501' 
auth_token = 'e691863170f16ce50f22901ece98b5cb' 
client = Client(account_sid, auth_token) 

message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Love yu babe❤❤❤',      
                              to='whatsapp:+919524355437' 
                          )
print(message.sid)
