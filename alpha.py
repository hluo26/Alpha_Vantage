from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#demonstration of all functions in alpha vantage API

API_key = 'ASWJAF02A51KK5QQ'

#interface, input the name of stock and other requirements
def main():
    print("Welcome to use alpha vantage API!")
    Time_series('AAPL','60min','full','monthly')


def Time_series(name,time,output,type):
    ts = TimeSeries(key=API_key, output_format='pandas')
    if(type=='day'):
        data, meta_data = ts.get_intraday(symbol=name,interval=time, outputsize=output)
        print_time_series(data,name,time)
    elif(type=='day_adjusted'):
        data, meta_data = ts.get_daily_adjusted(symbol=name,outputsize=output)
        print_time_series(data,name,time)
    elif(type=='weekly'):
        data, meta_data = ts.get_weekly(symbol=name)
        print_time_series(data,name,time)
    elif(type=='weekly_adjusted'):
        data, meta_data = ts.get_weekly_adjusted(symbol=name)
        print_time_series(data,name,time)
    elif(type=='monthly'):
        data, meta_data = ts.get_monthly(symbol=name)
        print_time_series(data,name,time)
    elif(type=='monthly_adjusted'):
        data, meta_data = ts.get_monthly_adjusted(symbol=name)
        print_time_series(data,name,time)

def print_time_series(data,name,time):

    prices = data.drop('5. volume',1)
    data['date'] = pd.to_datetime(data.index)
    plt.plot(data['date'],prices)
    plt.title('Intraday Times Series for the '+name+' stock ('+time+')')
    plt.grid()
    plt.show()




if __name__== "__main__":
    main()
