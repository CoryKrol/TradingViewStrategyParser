class Trade:
    """
    A class to represent a trade and holds all data related to opening and closing of an un-levered position
    """
    def __init__(self, side, open_price, close_price):
        """
        Constructor
        """
        self.open_price = open_price
        self.close_price = close_price
        if side == 'Long':
            self.side = True
        else:
            self.side = False

    def get_profit_loss(self):
        if self.side:
            return (self.close_price - self.open_price) / self.open_price
        else:
            return (self.open_price - self.close_price) / self.open_price
