from flask import Flask
from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.contract import Contract
from ibapi.common import TickerId

app = Flask(__name__)

@app.route("/connectToBroker", methods=['GET'])
def connectToBroker(self):
    self.host = "localhost"
    self.port = 7497
    self.clientId = 0
    self.connect(self.host, self.port, self.clientId)
    return "connected to broker"

def disconnect(self):
    self.disconnect()


def get_last_price(self, contract):
    self.reqMarketDataType(3)
    self.reqMktData(0, contract, "", False, False, [])

@app.route("/order/")

@app.route("/last_price")
def last_price():
    ibapi = IBapi()
    ibapi.connect()
    contract = Contract()
    contract.symbol = "AAPL"
    contract.secType = "STK"
    contract.exchange = "SMART"
    contract.currency = "USD"
    ibapi.get_last_price(contract)
    ibapi.disconnect()
    return str(ibapi.last_price)

if __name__ == "__main__":
    app.run()

