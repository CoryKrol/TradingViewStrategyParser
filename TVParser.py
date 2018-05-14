import Trade
import math

path = "trades.txt"
trades = []

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

    print("\n\nMean Returns: " + str(100*mean) + '%')
    print("Standard Deviation of Returns: " + str(100 * standard_deviation) + '%')
    print("\n\nKelly Leverage: " + str(kelly_leverage))
    print("Half Kelly: " + str(kelly_leverage/2))