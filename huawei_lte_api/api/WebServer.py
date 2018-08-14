
from huawei_lte_api.ApiGroup import ApiGroup
from huawei_lte_api.AuthorizedConnection import authorized_call


class WebServer(ApiGroup):
    def publickey(self):
        return self._connection.get('webserver/publickey')

    def token(self):
        return self._connection.get('webserver/token')