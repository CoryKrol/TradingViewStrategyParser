import Trade
import config_creator


def parse_trades(trade_path):
    trade_list = []
    with open(trade_path, 'r') as f:
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

            trade_list.append(Trade.Trade(side=side, open_price=open_price, close_price=close_price))
    return trade_list


def get_kelly_criterion(trade_list, fees_slippage):
    wins = []
    losses = []

    for t in trade_list:
        trade_profit_loss = t.get_profit_loss() - 2 * fees_slippage
        if trade_profit_loss > 0:   # Profitable trade
            wins.append(trade_profit_loss)
        else:                       # Losing trade or break even
            losses.append(trade_profit_loss)

    number_of_wins = len(wins)
    number_of_losses = len(losses)
    probability_of_winning = number_of_wins / (number_of_wins + number_of_losses)

    sum_trades = 0
    for w in wins:
        sum_trades += w

    average_winning_trade = sum_trades / float(number_of_wins)

    sum_trades = 0
    for l in losses:
        sum_trades -= l

    average_losing_trade = sum_trades / float(number_of_losses)

    return probability_of_winning - ((1 - probability_of_winning) / (average_winning_trade / average_losing_trade))


def get_kelly_leverage(trade_list, fees_slippage):
    profit_sum = 0
    number_of_trades = len(trade_list)

    for t in trade_list:
        profit_sum = profit_sum + t.get_profit_loss() - (2 * fees_slippage)

    mean = profit_sum / number_of_trades
    squared_difference_sum = 0

    for t in trade_list:
        squared_difference_sum = squared_difference_sum + pow((t.get_profit_loss() - (2 * fees_slippage) - mean), 2)

    variance = squared_difference_sum / float(number_of_trades)

    print("\n\nMean Returns: " + '{0:.2f}'.format(100 * mean) + '%')
    print("Standard Deviation of Returns: " + '{0:.2f}'.format(100 * pow(variance, 0.5)) + '%')

    return mean / variance


def leveraged_backtester(initial_capital, fees_slippage, leverage):
    trade_capital = initial_capital
    for i in trades:
        if trade_capital < 0:
            break
        order_size = trade_capital * leverage
        profit_loss = i.get_profit_loss() - (2 * fees_slippage)
        capital_gain_loss = order_size * profit_loss
        trade_capital = trade_capital + capital_gain_loss

    profit_loss_net = trade_capital - capital
    print("\n\nInitial Capital: $" + '{0:.2f}'.format(capital))
    print(str(leverage) + ":1 Leveraged Profit/Loss: $" + '{0:.2f}'.format(profit_loss_net))
    print(str(leverage) + ":1 Leveraged P/L Percent: " + '{0:.2f}'.format(100 * profit_loss_net / capital) + '%')


if __name__ == "__main__":
    path = config_creator.get_setting("./settings.ini", 'TradeInfo', 'trade-file-path')
    capital = float(config_creator.get_setting("./settings.ini", 'TradeInfo', 'initial-capital'))

    maker_fee = config_creator.get_setting("./settings.ini", 'TradeInfo', 'maker-fee')
    taker_fee = config_creator.get_setting("./settings.ini", 'TradeInfo', 'taker-fee')

    slippage = float(config_creator.get_setting("./settings.ini", 'TradeInfo', 'slippage')) / 100

    use_limit_orders = input("Use Limit Orders? [y/N]: ")
    use_limit_orders = str.upper(use_limit_orders)
    if use_limit_orders[0] == 'Y':
        fee = float(maker_fee) / 100
    else:
        fee = float(taker_fee) / 100

    fees_and_slippage = fee + slippage

    trades = parse_trades(path)

    kelly_leverage = get_kelly_leverage(trades, fees_and_slippage)
    kelly_criterion = get_kelly_criterion(trades, fees_and_slippage)

    print("\n\nKelly Leverage: " + '{0:.2f}'.format(kelly_leverage))
    print("Half Kelly: " + '{0:.2f}'.format(kelly_leverage / 2))
    print("Kelly Ratio: " + '{0:.2f}'.format(100 * kelly_criterion) + '%')

    for i in range(int(kelly_leverage), 0, -1):
        leveraged_backtester(initial_capital=capital, fees_slippage=fees_and_slippage, leverage=i)

