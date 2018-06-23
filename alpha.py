from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
import matplotlib
import matplotlib.pyplot as plt

#demonstration of all functions in alpha vantage API

API_key = 'ASWJAF02A51KK5QQ'

#interface, input the name of stock and other requirements
def main():
    print("Welcome to use alpha vantage API!")
    Time_series('MSFT','1min','full','monthly_adjusted')


def Time_series(name,time,output,type):
    ts = TimeSeries(key=API_key, output_format='pandas')
    if(type=='day'):
        data, meta_data = ts.get_intraday(symbol=name,interval=time, outputsize=output)
        data['4. close'].plot()
        plt.title('Intraday Times Series for the MSFT stock (1 min)')
        plt.show()
    elif(type=='day_adjusted'):
        data, meta_data = ts.get_daily_adjusted(symbol=name,outputsize=output)
        data['4. close'].plot()
        plt.title('Daily Adjusted Times Series for the MSFT stock')
        plt.show()
    elif(type=='weekly'):
        data, meta_data = ts.get_weekly(symbol=name)
        data['4. close'].plot()
        plt.title('Weekly Times Series for the MSFT stock')
        plt.show()
    elif(type=='weekly_adjusted'):
        data, meta_data = ts.get_weekly_adjusted(symbol=name)
        data['4. close'].plot()
        plt.title('Weekly Times Series for the MSFT stock')
        plt.show()
    elif(type=='monthly'):
        data, meta_data = ts.get_monthly(symbol=name)
        data['4. close'].plot()
        plt.title('Weekly Times Series for the MSFT stock')
        plt.show()
    elif(type=='monthly_adjusted'):
        data, meta_data = ts.get_monthly_adjusted(symbol=name)
        data['4. close'].plot()
        plt.title('Weekly Times Series for the MSFT stock')
        plt.show()




if __name__== "__main__":
    main()
