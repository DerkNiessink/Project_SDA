"""
Download stock prices data from 2011-01-01 to 2019-12-31 for specific stocks
and save it to file: "stock_data.csv".

Example usage:
python download.py AMZN AAPL BAC

-> Downloads the stock data of the tickers AMZN, AAPL and BAC.
"""


import yfinance as yf
import sys


def download(tickers: str):

    df = yf.download(tickers, start="2011-01-01", end="2019-12-31", group_by="ticker")
    df.to_csv("Data/stock_data.csv")


if __name__ == "__main__":

    ticker_string = ""
    for i in range(1, len(sys.argv)):
        ticker_string += f" {sys.argv[i]}"

    download(ticker_string)
