#####################################################################################
# PRE-PROCESSING RAW FINANCIAL DATA OF A TICKER TO PASS INTO XGBOOST FOR LEARNING  #
####################################################################################

import yfinance as yf
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import sys

# initiate ompany name as user input
ticker_symbol = str(input(" Enter TICKER: "))

# create Ticker object
ticker = yf.Ticker(ticker_symbol)

# raw financial data of last 30 days
historical_data = ticker.history(period="1mo")

# turn data into dataFrame for a cleaner look
raw_data = pd.DataFrame(historical_data)

# include Date as a column 
def include_indexcol(data):
    """

    'Date' is originally an index in yfinance. 
    
    
    Return:'Date' as a column for uses down the line.

    Alternatively use build-in one-liner
    # raw_data = raw_data_without_datecol.reset_index()
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

def calc_log_returns(prev_price, present_price, log_return):
    """
    Calculates log of returns from previous price to next-day prie 
    F(t) = log(P(t)/P(t-1))
    """



    return log_return

# pull Date and Close columns

# def get_dates_with_log_returns(ticker_symbol):
#     """
#     Takes large matrix of raw data and cuts following features: 
    
#     High, Low, Volume, Dividends, Stock Plits

#     Returns Date, Adj. Close grouped by week 1 through 5 and respective weekly log returns
#     """ 
#     dates_and_close_by_week = pd.groupby
#     return 
#     # here we will convert raw into adj close and dates
#     # calc log returns and group dates by week 1 through week 5 

# def add_risk_free_rate():

# # plot and visualize the prices 

# # Error-handling

# def final_tree()

# def main():
#     args = sys.argv[1:]

#     if len(args) == 1:
#         #some function (args[0])
#     else:
#         print('example usage: data/original_small.json')


# if __name__ == "__main__":
#     main()