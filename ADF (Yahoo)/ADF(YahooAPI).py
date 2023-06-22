import matplotlib.pyplot as plt
import yfinance as yf
import datetime
import pandas as pd
import statsmodels.tsa.stattools as ts
from scipy.stats import linregress

def download_data(stock, start, end):
    stock_data = {}
    ticker = yf.download(stock, start, end)
    stock_data['price'] = ticker ['Adj Close']
    return pd.DataFrame(stock_data)

def plot_pairs(data1, data2):
    fig, (ax1, ax2) = plt.subplots(2)
    fig.suptitle('Pair of Stocks')
    ax1.plot(data1)
    ax2.plot(data2)
    plt.show()#

def scatter_plot(data1, data2):
    plt.scatter(data1.values, data2.values)
    plt.xlabel("SP 500")
    plt.ylabel("Nasdaq")
    plt.show()


if __name__ == '__main__':
    start_date = datetime.datetime(2022, 1, 1)
    end_date = datetime.datetime(2023, 6, 1)

    pair1 = download_data('^GSPC', start_date, end_date)
    pair2 = download_data('^IXIC', start_date, end_date)
                
    print(pair1.values)
    print(pair2.values)

    plot_pairs(pair1, pair2)
    scatter_plot(pair1, pair2)

    result = linregress(pair1.values[:, 0], pair2.values[:, 0])

    residuals = pair1 - result.slope * pair2

    adf = ts.adfuller(residuals)
    print("Take first Value below and compare in the ranges of 1, 5, 10 percent confidence.")
    print(adf)
    print('/n')
    print(result)          



#if __name__ == '__main__':
#    for x in range(2008,2022):
#        for y in range (1,11):
#            start_date = datetime.datetime(x, y, 1)
#            end_date = datetime.datetime(x+1, y+1,1)

#            pair1 = download_data('^GSPC', start_date, end_date)
#            pair2 = download_data('^IXIC', start_date, end_date)
                
            #print(pair1.values)#
            #print(pair2.values)#

#            plot_pairs(pair1, pair2)
#            scatter_plot(pair1, pair2)

#            result = linregress(pair1.values[:, 0], pair2.values[:, 0])

#            residuals = pair1 - result.slope * pair2

#            adf = ts.adfuller(residuals)
#            print(adf)
#        y = y + 1
#    x = x+1#




