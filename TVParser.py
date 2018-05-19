import Trade
import config_creator
import math

path = config_creator.get_setting("./settings.ini", 'TradeInfo', 'trade-file-path')
capital = float(config_creator.get_setting("./settings.ini", 'TradeInfo', 'initial-capital'))
trades = []

maker_fee = config_creator.get_setting("./settings.ini", 'TradeInfo', 'maker-fee')
taker_fee = config_creator.get_setting("./settings.ini", 'TradeInfo', 'taker-fee')

use_limit_orders = input("Use Limit Orders? [y/N]: ")
use_limit_orders = str.upper(use_limit_orders)
if use_limit_orders[0] == 'Y':
    fee = float(maker_fee) / 100
else:
    fee = float(taker_fee) / 100

with open(path, 'r') as f:
    # Throw away first 36 lines
    for num in range(1, 37):
        f.readline()

    for line in f:
        open_data = line.split()

        side = open_data[2]
        open_price = float(open_data[6])

        close_data = f.readline().split()

        if len(close_data) < 4:
            break

        if close_data[2] == 'Close':
            close_price = float(close_data[8])
        else:
            close_price = float(close_data[5])

        trades.append(Trade.Trade(side=side, open_price=open_price, close_price=close_price))

    profit_sum = 0
    for i in trades:
        profit_sum = profit_sum + i.get_profit_loss()

    mean = profit_sum / len(trades)
    squared_difference_sum = 0
    for i in trades:
            squared_difference_sum = squared_difference_sum + pow((i.get_profit_loss() - mean), 2)

    variance = squared_difference_sum / float(len(trades))

    standard_deviation = math.sqrt(variance)

    kelly_leverage = mean/variance

    print("\n\nMean Returns: " + '{0:.2f}'.format(100*mean) + '%')
    print("Standard Deviation of Returns: " + '{0:.2f}'.format(100 * standard_deviation) + '%')
    print("\n\nKelly Leverage: " + '{0:.2f}'.format(kelly_leverage))
    print("Half Kelly: " + '{0:.2f}'.format(kelly_leverage/2))

    trade_capital = capital
    for i in trades:
        if trade_capital < 0:
            break
        order_size = trade_capital * math.floor(kelly_leverage)
        profit_loss = i.get_profit_loss() - (2 * fee)
        capital_gain_loss = order_size * profit_loss
        trade_capital = trade_capital + capital_gain_loss

    profit_loss_net = trade_capital - capital
    print("\n\nInitial Capital: $" + '{0:.2f}'.format(capital))
    print("\n\nKelly Leverage: " + str(math.floor(kelly_leverage)))
    print("Kelly Leveraged Profit/Loss: $" + '{0:.2f}'.format(profit_loss_net))
    print("Kelly Leveraged P/L Percent: " + '{0:.2f}'.format(100*profit_loss_net/capital) + '%')

    print("\n")
    trade_capital = capital
    for i in trades:
        if trade_capital < 0:
            break
        order_size = trade_capital * math.floor(0.5 * kelly_leverage)
        profit_loss = i.get_profit_loss() - (2 * fee)
        capital_gain_loss = order_size * profit_loss
        trade_capital = trade_capital + capital_gain_loss

    profit_loss_net = trade_capital - capital
    print("\n\nHalf Kelly: " + str(math.floor(kelly_leverage / 2)))
    print("Half Kelly Leveraged Profit/Loss: $" + '{0:.2f}'.format(profit_loss_net))
    print("Half Kelly Leveraged P/L Percent: " + '{0:.2f}'.format(100*profit_loss_net/capital) + '%')