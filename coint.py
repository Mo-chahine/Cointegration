import pandas as pd 
import matplotlib.pyplot as plot

nas_sp= pd.read_csv('nassp.csv',skiprows=0)
df = nas_sp

col_names = [ 'nas', 'sp']
df.columns = col_names

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import matplotlib.pyplot as plt

plt.subplot(2,1,1)
plt.plot(df['nas'], label = 'nas')
plt.plot(df['sp'], label = 'sp')
plt.legend(loc= 'best', fontsize='small')


plt.subplot(2,1,2)
plt.plot(df['nas'] - df['sp'], label='Spread')
plt.legend(loc= 'best', fontsize='small')
plt.axhline(y=0, linestyle='--', color='k')
plt.show()


from statsmodels.tsa.stattools import adfuller

result_nas = adfuller(df['nas'])
print('p value of nasdaq is', result_nas[1])
result_sp = adfuller(df['sp'])
print('p value of sp 500 is', result_sp[1])

result_spread = adfuller(df['nas'] - df['sp'])
print('the p value of the spread is ', result_spread[1])



