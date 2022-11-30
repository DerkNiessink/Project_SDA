import yfinance as yf
import sys


def download(tickers: str):

    df = yf.download(tickers, start="2011-01-01", end="2019-12-31", group_by="ticker")
    df.to_csv("stock_data.csv")


if __name__ == "__main__":

    ticker_string = ""
    for i in range(1, len(sys.argv)):
        ticker_string += f" {sys.argv[i]}"

    download(ticker_string)
