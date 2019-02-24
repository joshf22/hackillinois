# Wallet
# Will track money through change in stock transactions
# Uses variables GE - General Electric, USD - USD value, Stock - Real time stock value
# Fee_total - Stock transaction fees, initial - Initial stock value

class Wallet (object):
    def __init__(self, GE, USD, Stock, initial): 
        self.Stock_type = GE                       
        self.USD_value = USD                        
        self.Stock_value = Stock                     
        self.Fee_total = 0.0                        
        self.initial_value = USD + (initial * Stock)  
        self.market_start = initial                 
        self.total_val = self.initial_value

    def toString(self):
        return(self.Stock_type + " wallet contains: " + str(self.USD_value) + " dollars and " + str(self.Stock_value) + " " +
        self.Stock_type + " with " + str(self.Fee_total) +
         " in fees || Wallet Start: " + str(self.initial_value) + " | Wallet Curr: " + str(self.total_val))

    def total(self, Market_price):
        self.total_val = self.USD_value + (self.Stock_value * Market_price) - self.Fee_total
        return(self.total_val)

    #def realtime_reload(self, authClient):                 # Needed to track real time value of stock
    #    self.USD_value = authClient.get_account('')
    #    self.Stock_value = authClient.get_account('')