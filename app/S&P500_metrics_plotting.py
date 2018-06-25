#imports
import quandl
import os
import matplotlib.pyplot as plt

#Define API key variable from environment variable

api_key = os.environ.get("QUANDL_API_KEY")

#main section of the app

def run():

#Menu adapted from inventory management app
    print('''
    -----------------------------------
    WELCOME TO S&P500 METRICS PLOTTING
    -----------------------------------
    User Name: user_name
    This app plots metrics on the S&P 500 stock index.
    Here is a list of metrics that can be plotted:
        Metric                    | Description
        ----------------------    | ---------------------------------------
        'SP500_BVPS_YEAR'         | Yearly book value per share.
        'SP500_BVPS_QUARTER'      | Quarterly book value per share.
        'SP500_DIV_YIELD_YEAR'    | Yearly dividend yield.
        'SP500_DIV_YIELD_MONTH'   | Monthly dividend yield.
        'SP500_EARNINGS_YEAR'     | Yearly earnings.
        'SP500_EARNINGS_MONTH'    | Monthly earnings.
        'SP500_PE_RATIO_YEAR'     | Yearly price to earnings ratio.
        'SP500_PE_RATIO_MONTH'    | Monthly price to earnings ratio.
        'SHILLER_PE_RATIO_YEAR'   | Yearly Shiller price to earnings ratio.
        'SHILLER_PE_RATIO_MONTH'  | Monthly Shiller price to earnings ratio.''')
