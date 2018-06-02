# KellyLeverage-TVStrategyParser
A simple python script to parse the trades from a TradingView strategy and determine the approprite leverage to use according to the Kelly Risk Management System

## The Kelly System
To be used in conjunction with the [Kelly Criterion/Ratio](https://www.tradingview.com/script/bnpAXRtm-Kelly-Ratio/)

## Warning
### I am not a financial advisor, this is not investment advice, I'm not responsible for any money this will probably lose you.


## TradingView Strategy Settings and Trade Export
The program assumes that you used strategy.entry() and strategy.close() functions similar to mine


>strategy.entry("Long", 1, when=longCondition)
>
>strategy.entry("Short", 0,  when=shortCondition)
>
>strategy.close("Long", when=longClose)
>
>strategy.close("Short", when=shortClose)


In the TradingView Strategy Tester panel click the [Export Button](https://i.imgur.com/m6oyxDH.png) as shown to copy the trade history of your strategy to the clipboard


## Settings
1. Rename the sample_settings.ini file to settings.ini and adjust your settings accordingly.

2. Create a trades.txt (or whatever you changed the settings to) file and copy the exported TradingView trade information into it

## Running
Navigate to the folder and run

>$ python tv_parser.py

### Sample Output

>TradeInfo trade-file-path is trades.txt
>
>TradeInfo initial-capital is 500
>
>TradeInfo maker-fee is 0.16
>
>TradeInfo taker-fee is 0.26
>
>TradeInfo slippage is 0.02
>
>Use Limit Orders? [y/N]: n
>
>
>Mean Returns: 1.91%
>
>Standard Deviation of Returns: 6.83%
>
>
>Kelly Leverage: 4.10
>
>Half Kelly: 2.05
>
>Kelly Criterion: 21.61%
>
>Initial Capital: $500.00
>
>4:1 Leveraged Profit/Loss: $220.49
>
>4:1 Leveraged P/L Percent: 44.10%
>
>
>
>
>Initial Capital: $500.00
>
>3:1 Leveraged Profit/Loss: $183.17
>
>3:1 Leveraged P/L Percent: 36.63%
>
>
>
>
>Initial Capital: $500.00
>
>2:1 Leveraged Profit/Loss: $133.33
>
>2:1 Leveraged P/L Percent: 26.67%
>
>
>
>
>Initial Capital: $500.00
>
>1:1 Leveraged Profit/Loss: $71.82
>
>1:1 Leveraged P/L Percent: 14.36%


### Disclaimer
I would advise using the lowest possible leverage and slowly increase the leverage every month. Don't just increase after a few wins because chances are good that you are due for some losses.

>Kelly Leverage: 8.73
>
>Half Kelly: 4.37
>
>Initial Capital: $500.00
>
>
>Kelly Leverage: 8
>
>Kelly Leveraged Profit/Loss: $-290.58
>
>Kelly Leveraged P/L Percent: -58.12%
>
>
>
>
>Half Kelly: 4
>
>Half Kelly Leveraged Profit/Loss: $1065.53
>
>Half Kelly Leveraged P/L Percent: 213.11%

#### In the above example from an older version of the script you see that using the Full Kelly of 8 would have brought on large drawdown bringing the account close to ruin where as using the half Kelly we would have tripled our money using this specific strategy.


#### Again I am not responsible for my program saying "Kelly Leverage: 95" and then you go and lose your house payment.

### Roadmap/Planned Features
1. Output monthly profits and losses
2. Leveraged backtesting for specific months
3. Back testing of multiple strategies with leverage
4. WebUI
