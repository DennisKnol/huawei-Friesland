# huawei-lte-api
API For huawei LAN/WAN LTE Modems,
you can use this to simply send SMS, get information about your internet usage, signal, and tons of other stuff

Tested on:
* Huawei B310s-22
* Huawei B525s-23a
* Huawei B525s-65a
* Huawei B715s-23c
* Huawei E3131
* Huawei E5186s-22a
* Huawei B528s
* (probably will work for other Huawei LTE devices too)

Will NOT work on:
* Huawei B2368-22 (Incompatible firmware, testing device needed!)

PS: it is funny how many stuff you can request from modem/router without any authentication

## Installation

### PIP (pip3 on some distros)
```bash
$ pip install huawei-lte-api
```
### Repository
You can also use these repositories maintained by me
#### Debian and derivates

Add repository by running these commands

```
$ wget -O - https://apt.salamek.cz/apt/conf/salamek.gpg.key|sudo apt-key add -
$ echo "deb     https://apt.salamek.cz/apt all main" | sudo tee /etc/apt/sources.list.d/salamek.cz.list
```

And then you can install a package python3-huawei-lte-api

```
$ apt update && apt install python3-huawei-lte-api
```

#### Archlinux

Add repository by adding this at end of file /etc/pacman.conf

```
[salamek]
Server = https://arch.salamek.cz/any
SigLevel = Optional
```

and then install by running

```
$ pacman -Sy python-huawei-lte-api
```

## Usage

```python3
from huawei_lte_api.Client import Client
from huawei_lte_api.AuthorizedConnection import AuthorizedConnection
from huawei_lte_api.Connection import Connection

# connection = Connection('http://192.168.8.1/') For limited access, I have valid credentials no need for limited access
# connection = AuthorizedConnection('http://admin:MY_SUPER_TRUPER_PASSWORD@192.168.8.1/', login_on_demand=True) # If you wish to login on demand (when call requires authorization), pass login_on_demand=True
connection = AuthorizedConnection('http://admin:MY_SUPER_TRUPER_PASSWORD@192.168.8.1/')

client = Client(connection) # This just simplifies access to separate API groups, you can use device = Device(connection) if you want

print(client.device.signal())  # Can be accessed without authorization
print(client.device.information())  # Needs valid authorization, will throw exception if invalid credentials are passed in URL


# For more API calls just look on code in the huawei_lte_api/api folder, there is no separate DOC yet

```
Result dict
```python
{'DeviceName': 'B310s-22', 'SerialNumber': 'MY_SERIAL_NUMBER', 'Imei': 'MY_IMEI', 'Imsi': 'MY_IMSI', 'Iccid': 'MY_ICCID', 'Msisdn': None, 'HardwareVersion': 'WL1B310FM03', 'SoftwareVersion': '21.311.06.03.55', 'WebUIVersion': '17.100.09.00.03', 'MacAddress1': 'EHM:MY:MAC', 'MacAddress2': None, 'ProductFamily': 'LTE', 'Classify': 'cpe', 'supportmode': None, 'workmode': 'LTE'}
```

## Code examples
### Monitoring

* Monitoring traffic and signal https://github.com/littlejo/huawei-lte-examples

### SMS

* Relay received SMS into your email https://github.com/chenwei791129/Huawei-LTE-Router-SMS-to-E-mail-Sender


## Donations

* 250 CZK (9,79 EUR) for B535-232 fund, thx @larsvinc !

