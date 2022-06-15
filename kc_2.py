#Import and plot Apple stock price
import pandas as pd
import 
.pyplot as plt
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'assets', '2014_apple_stock.csv')

df = pd.read_csv(filename)
#Convert date in string to date in datetime format
df.AAPL_x = pd.to_datetime(df.AAPL_x)

#Group Date by month with average monthly price
df_monthly = df.groupby(pd.Grouper(key='AAPL_x', freq='M')).mean().reset_index()

#Plot the data
df_monthly.plot(x='AAPL_x', y='AAPL_y',
                label='Apple stock price', figsize=(10, 7))
plt.xlabel("MONTH")
plt.ylabel("PRICE")
plt.show()

