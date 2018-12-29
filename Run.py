from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection
from huawei_lte_api.api.Sms import Sms
import time

# connection = Connection('http://192.168.8.1/') For limited access, I have valid credentials no need for limited access
# connection = AuthorizedConnection('http://admin:MY_SUPER_TRUPER_PASSWORD@192.168.8.1/', login_on_demand=True) # If you wish to login on demand (when call requires authorization), pass login_on_demand=True

connection = AuthorizedConnection('http://admin:wowapasswordhowcrazy@192.168.8.1/')

client = Client(connection) # This just simplifies access to separate API groups, you can use device = Device(connection) if you want

# print(client.device.signal())  # Can be accessed without authorization
# print(client.device.information())  # Needs valid authorization, will throw exception if invalid credentials are passed in URL
# print(client.sms.sms_count())


# for _ in range(0, 5):
#     client.sms.send_sms([1280], "1GB EXTRA")
latest_sms = str(list(list(client.sms.get_sms_list()["Messages"].values())[0][0].values())[3])
while True:
    print("lol")
    if "500MB" in latest_sms:
        print("asking for data")
        for _ in range(0, 5):
            client.sms.send_sms([1280], "1GB EXTRA")
    elif "Gelukt!" in latest_sms:
        print("plenty of data left")
        time.sleep(5)
    else:
        print("unexpected message")





#get list of received SMS' (check returned data)
# for sms in client.sms.get_sms_list:
#     #(message == expected ?)
#     print(sms)


# # Get list of received sms, i'm not sure how returned data of this call look, so this needs some testing
# for sms in client.sms.get_sms_list():
#     # Check if message is expected message etc.
#     if sms.message == 'expected_content' and sms.phone_number == 'expected_sender':
#         # If it is expected message, react on it by sending SMS, we need to check status of send_sms, again i don't know return data of this call, so it needs some testing
#         if client.sms.send_sms('PHONE_NUMBER', 'SMS_MESSAGE')['send'] == 'ok':
#             # We sent our SMS successfully, lets delete old message we was reacting on, this again needs some testing
#             client.sms.delete_sms([sms.id])
