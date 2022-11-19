import http.client
import random

def sendSMS(mobileNumber, message):
    conn = http.client.HTTPSConnection("rest.nexmo.com")
    payload = 'from=Vonage%20APIs&text='+str(message)+'&to=91'+str(mobileNumber)+'&api_key=b88f337d&api_secret=Tg8ZCh1NlGxKsz01'
    print(payload)
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }
    conn.request("POST", "/sms/json", payload, headers)
    res = conn.getresponse()
    data = res.read()
    return data.decode("utf-8")

NO2=random.randint(0,30)
CO2=random.randint(0,25)
CO=random.randint(0,5)

if NO2 >= 10 or CO2 >= 10 :
    print("ALERTING PEOPLE....!!!")
    print("CO2="+ str(CO2) + " AND NO2="+ str(NO2) + " LEVELS are reached crtical...")
    print("""
    
  ______   _____   _____    ______                _        ______   _____    _______ 
 |  ____| |_   _| |  __ \  |  ____|       /\     | |      |  ____| |  __ \  |__   __|
 | |__      | |   | |__) | | |__         /  \    | |      | |__    | |__) |    | |   
 |  __|     | |   |  _  /  |  __|       / /\ \   | |      |  __|   |  _  /     | |   
 | |       _| |_  | | \ \  | |____     / ____ \  | |____  | |____  | | \ \     | |   
 |_|      |_____| |_|  \_\ |______|   /_/    \_\ |______| |______| |_|  \_\    |_|   

    """)


alertMessage = "FIRE ALERT !!!... THE FIRE ALERT HAS BEEN ACTIVATED IN THE CANTEEN AREA OF THE OFFICE PLEASE LEAVE THE BUILDING IMMEDIATELY"
print(alertMessage)
response = sendSMS(8925174052, alertMessage)
print(response)
print("SMS SENT SUCCESSFULLY, IF YOU DID NOT RECEIVE ANY ALERT MESSAGE PLEASE TRY AGAIN.")