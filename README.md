# KellyLeverage-TVStrategyParser
A simple python script to parse the trades from a TradingView strategy and determine the approprite leverage to use according to the Kelly Risk Management System

To be used in conjunction with the [Kelly Criterion/Ratio](https://www.tradingview.com/script/bnpAXRtm-Kelly-Ratio/)

Note: The first commit probably won't work for you, I quickly wrote it up this afternoon, but will continue to update it throughout the week.

Warning: I am not a financial advisor, this is not investment advice, I'm not responsible for anymoney this will probably lose you.

The program assumes that you used strategy.entry() and strategy.close() functions similar to mine


strategy.entry("Long", 1, when=longCondition)

strategy.entry("Short", 0,  when=shortCondition)

strategy.close("Long", when=longClose)

strategy.close("Short", when=shortClose)


In the TradingView Strategy Tester panel click the [Export Button](https://i.imgur.com/m6oyxDH.png) as shown to copy the trade history of your strategy to the clipboard



Replace strategy in trades.txt with what is copied to your clipboard and run

$ python TVParser.py

to get an output similar to this.


Mean Returns: 0.838731161016012%

Variance of Returns: 0.15346013953301188%

Standard Deviation of Returns: 3.917398875950876%



Kelly Leverage: 5.4654659090518205

Half Kelly: 2.7327329545259103


I would advise using the half Kelly Leverage and rounding down and only increasing if this yields success. Again I am not responsible for my program saying "Kelly Leverage: 95" and then you go and lose your house payment.
