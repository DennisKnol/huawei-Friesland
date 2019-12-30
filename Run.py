from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection
from huawei_lte_api.api.Sms import Sms
import sched, time

s = sched.scheduler(time.time, time.sleep)


def ask_extra_gigs(sc):
    connection = AuthorizedConnection('http://admin:DitIsEenWachtwoord20!8@192.168.8.1/')
    client = Client(connection)
    latest_sms = next(iter(next(iter(client.sms.get_sms_list()['Messages'].values()))))['Content']
    if '500MB' in latest_sms:
        print('asking for data')
        for _ in range(0, 5):
            client.sms.send_sms([1280], "1GB EXTRA")
        s.enter(600, 1, ask_extra_gigs, (sc,))
    elif 'Gelukt!' in latest_sms:
        print('plenty of data left')
        s.enter(600, 1, ask_extra_gigs, (sc,))
    else:
        client.sms.send_sms([+31611621115], "Onverwacht bericht")
        print('unexpected message')


s.enter(1, 1, ask_extra_gigs, (s,))
s.run()
