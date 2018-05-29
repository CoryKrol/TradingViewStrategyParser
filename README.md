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

>$ python TVParser.py

### Sample Output

>TradeInfo trade-file-path is trades.txt
>
>TradeInfo initial-capital is 500
>
>TradeInfo maker-fee is 0.16
>
>TradeInfo taker-fee is 0.26
>
>TradeInfo slippage is 0.05
>
>Use Limit Orders? [y/N]: n
>
>
>Mean Returns: 0.88%
>
>Standard Deviation of Returns: 3.17%
>
>
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



### Disclaimer
I would advise using the half Kelly Leverage and rounding down and only increasing if this yields success. 

#### In the above example you see that using the Full Kelly of 8 would have brought on large drawdown where as using the half Kelly we would have tripled our money using this specific strategy. (No you can't have it)


#### Again I am not responsible for my program saying "Kelly Leverage: 95" and then you go and lose your house payment.

### Roadmap/Planned Features
1. Back testing of multiple strategies with leverage
2. WebUI
