#####################################################################################
# PRE-PROCESSING RAW FINANCIAL DATA OF A TICKER TO PASS INTO XGBOOST FOR LEARNING  #
####################################################################################

import yfinance as yf
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sys

# Put code in OOP class StockPreprocessData

# class StockPreprocessData

#     def _init_(self):

# initiate ompany name as user input
ticker_symbol = 'AAPL' # str(input(" Enter TICKER: "))

# create Ticker object
ticker = yf.Ticker(ticker_symbol)

# raw financial data of last 30 days
historical_data = ticker.history(period="1mo")
# remove time from date 
historical_data.index = historical_data.index.tz_localize(None)

# turn data into df for a cleaner look
raw_data = pd.DataFrame(historical_data)

# include Date as a column 

def include_indexcol(data):
    """

    'Date' is originally an index in yfinance. 
    
    Return:'Date' becomes one of the columns, not an index anymore.  

    Alternatively use one-liner from Pandas
    # raw_data = raw_data.reset_index()
    """
    # name of index column should be Date 
    index_name = data.index.name or 'i'
    # turn index of DataFrame into a list e.g [March 7th, ...]
    indexcol_is_list = list(data.index)    

    # define new dict 'Date' that will added to general new raw data as e.g {'Date':[March7th, ...]}
    date_dict = {index_name:indexcol_is_list}
    # add the index list with the name 'Date' to the new DataFrame by iteratively adding {'Date':[March7th, ...]} to {'Close':[100, ...]}
    for col in data: 
        date_dict[col] = data[col].values.tolist() 

    # convert back to DataFrame for a clean look
    raw_data = pd.DataFrame(date_dict)

    return raw_data

# get date of dates and close columns only 
dates_and_close_data = include_indexcol(raw_data)[['Date', 'Close']] 

def calc_log_returns():
    """

    Calculates log of returns from previous price to next-day prie 
    F(t) = log(P(t)/P(t-1))

    """
    # fetch the stock prices; vectorize instead of a sequential for loop 
    # due to CPU memory constraints; cache invalidation 
    present_prices = dates_and_close_data['Close']

    # shift the original column ['close']  down, subtract at n and n-1 prices. 
    prev_prices = present_prices.shift(1)

    # acccount for division by NaN potentially in the future? 
    log_returns_wNaN = np.log(present_prices/prev_prices)
    # drop the NaN values 
    log_returns = log_returns_wNaN.dropna()

    # name the column, turn into a DataFrame for merging 
    log_returns.name = 'Log Returns'
    log_returns_df = log_returns.to_frame()

    return log_returns_df

# drop close column as it is not needed 
dates_onlycol = dates_and_close_data.drop(columns=['Close'])

# now join the log returns column to our data with 'dates' and group according to weeks
dates_and_log_ret = dates_onlycol.join(calc_log_returns()).dropna()

# pull out days 2 through 5 as a test and add the log returns; foreshadow to summing every 5 day periods per week 
data_test = dates_and_log_ret.iloc[1:5]
data_sum = data_test['Log Returns'].sum()

# reset index to be at 0. Ensures we are indexing correctly when grouping  
dates_and_log_ret = dates_and_log_ret.reset_index(drop=True)
# group into every 5-day summed log returns
# by exploiting additive nature of Logarithms ln(P1/P0) + ln(P2/P1) = ln(P2/P0)
grouped_data = dates_and_log_ret['Log Returns'].groupby(dates_and_log_ret.index // 5).sum()
print(dates_and_log_ret)

# Append a column that will have corresponding name of date next to the date itself 
def assign_dayname_to_datecol():
    """

    Passes a date and identifies the name of the day.  

    """
    # call the column day 
    # pull out the dates of the previous data frame; try with last date first '2025-08etc'
    days = dates_and_log_ret['Date'].dt.day_name().rename('Day')
    # iteratively pass them into this function 
    date_day_logret = pd.concat([days, dates_and_log_ret], axis=1)
    return date_day_logret
    # convert the results into a panda Series and add it to the previous data frame 
print(assign_dayname_to_datecol())

# Now use if statements to identify the specific days 



# How many months needed to end up with 5 entry week intervals? Consider NaN vals. 
# There are 4 week intervals for 22 entries
# Warning: indexing by 5 doesn't mean we are taking the specific 5 day weeks 
# How to make it recognize we need every 5 valid days?
# Its giving us 

# 22 entries 

# pull Date and Close columns


# def add_risk_free_rate():

# # plot and visualize the prices 

# # Error-handling

# def final_tree()

