from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection
from huawei_lte_api.api.Sms import Sms
import sched, time
s = sched.scheduler(time.time, time.sleep)

# connection = Connection('http://192.168.8.1/') For limited access, I have valid credentials no need for limited access
# connection = AuthorizedConnection('http://admin:MY_SUPER_TRUPER_PASSWORD@192.168.8.1/', login_on_demand=True) # If you wish to login on demand (when call requires authorization), pass login_on_demand=True
def ask_extra_gigs(sc):
    connection = AuthorizedConnection('http://admin:xxxx@192.168.8.1/')
    client = Client(connection) # This just simplifies access to separate API groups, you can use device = Device(connection) if you want
    latest_sms = str(list(list(client.sms.get_sms_list()["Messages"].values())[0][0].values())[3])
    print(latest_sms)
    if '500MB' in latest_sms:
        print('asking for data')
        for _ in range(0, 5):
            client.sms.send_sms([1280], "1GB EXTRA")
        s.enter(600, 1, ask_extra_gigs, (sc,))
    elif 'Gelukt!' in latest_sms:
        print('plenty of data left')
        s.enter(600, 1, ask_extra_gigs, (sc,))
    else:
        print('unexpected message')

s.enter(1, 1, ask_extra_gigs, (s,))
s.run()
