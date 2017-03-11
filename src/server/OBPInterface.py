import requests

class OBPInterface:

    def __init__(self):
        self.bankID = -1
        self.accountID = -1
        self.token = -1


    def getBankID(self):
        return self.bankID

    def setBankID(self, bankID):
        self.bankID = bankID

    def getAccountID(self):
        return self.accountID

    def setAccountID(self, accountID):
        self.accountID = accountID

    def postRequest(self, uri, data):
        r = request.post("https://apisandbox.openbankproject.com/obp/v2.2.0" + uri, data})

        return r.json()

    def getRequest(self, uri):
        r = request.get("https://apisandbox.openbankproject.com/obp/v2.2.0" + uri, data = {"Autherization" : "DirectLogin token=\""+self.token+"\""})
        r.status_code
        r.headers['content-type']
        r.encoding
        r.text
        return r.json()

    def login(self, username, password):
        result = postRequest("/my/logins/direct", data = {"Authorization":"DirectLogin username=\""+username+"\","
                        + "password=\""+password+"\", consumer_key=\"hznak4pyka33m2pn2yq5gr5le0x2itnnsbyht4jp\"","Content-Type": "application/json" })
        self.token = result["token"]

    def root(self):
        return getRequest("/root")

    def getBanks(self):
        return getRequest("/banks")

    def getBankDetails(self):
        if(self.bankID == -1):
            return None
        return getRequest("/banks/" + self.bankID)

    def getAccountDetails(self):
        if(self.accountID == -1 or self.bankID == -1):
            return None
        return getRequest("/my/banks/" + self.bankID + "/accounts/" + self.accountID + "/account")

    def getTransactions(self):
        if(self.accountID == -1 or self.bankID == -1):
            return None
        return getRequest("/my/" + self.bankID + "/rbs/accounts/" + self.accountID + "/transactions")
