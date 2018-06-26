from alpha_vantage.timeseries import TimeSeries
from datetime import datetime
from enum import Enum
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

#demonstration of all functions in alpha vantage API

API_key = 'ASWJAF02A51KK5QQ'

#interface, input the name of stock and other requirements
def main():
    print("Welcome to use alpha vantage API!")
    Time_series('AAPL','60min','full','Monthly')


def Time_series(name,time,output,type):
    #ts = TimeSeries(key=API_key, output_format='pandas')
    ts = TimeSeries(key=API_key)
    if(type=='Intraday'):
        data, meta_data = ts.get_intraday(symbol=name,interval=time, outputsize=output)
        #print_time_series(data,name,time,type)
        return data
    elif(type=='Day Adjusted'):
        data, meta_data = ts.get_daily_adjusted(symbol=name,outputsize=output)
        print_time_series(data,name,time,type)
    elif(type=='Weekly'):
        data, meta_data = ts.get_weekly(symbol=name)
        print_time_series(data,name,time,type)
    elif(type=='Weekly Adjusted'):
        data, meta_data = ts.get_weekly_adjusted(symbol=name)
        print_time_series(data,name,time,type)
    elif(type=='Monthly'):
        data, meta_data = ts.get_monthly(symbol=name)
        #print_time_series(data,name,time,type)
        description(data,name,time,type)
    elif(type=='Monthly Adjusted'):
        data, meta_data = ts.get_monthly_adjusted(symbol=name)
        print_time_series(data,name,time,type)

def print_plotting_chart(data,name,time,type):
    prices = data.drop('5. volume',1)
    data['date'] = pd.to_datetime(data.index)
    plt.plot(data['date'],data['1. open'],label='1. open')
    plt.plot(data['date'],data['2. high'],label='2. high')
    plt.plot(data['date'],data['3. low'],label='3. low')
    plt.plot(data['date'],data['4. close'],label='4. close')
    plt.xlabel('Date')
    plt.title(type+' Times Series for the '+name+' stock ('+time+')')
    plt.grid()
    plt.legend()
    plt.show()

def description(data,name,time,type):
    print('Mean of '+type+' Times Series for the '+name+' stock ('+time+')')
    print(data.describe())
    print('Variance of '+type+' Times Series for the '+name+' stock ('+time+')')
    print(data.var())
    print('Range of '+type+' Times Series for the '+name+' stock ('+time+')')
    print(data.max()-data.min())
    print('Median of '+type+' Times Series for the '+name+' stock ('+time+')')
    print(data.median())




if __name__== "__main__":
    main()
