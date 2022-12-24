# Project_SDA

## Installation

1. Clone the repository.
2. Install the requirements: `pip install -r requirements.txt`.
3. Download the data by running `download.py` in the `Project_SDA` folder as working directory.


May `download.py` malfunction for some reason, the data can be downloaded and extracted to this folder from the drive directly: https://drive.google.com/file/d/1FgmJXkv6Xo0JWJtslu1ZNL3urH6SlodU/view?usp=sharing.

## Structure

The src folder contains all the code of the analysis. All py/ipynb files can be run separately.

    .
    ├── requirements.txt
    ├── README.md
    ├── data               # Constructed after running `download.py`
    ├── download.py
    └── src
        ├── Stock Timeseries.ipynb
        ├── Sentiment Timeseries.ipynb
        ├── Sentiment Analysis.ipynb
        ├── VAR.ipynb
        ├── AR and H0A.ipynb
        └── H0B.ipynb

## Analysis

# Hypotheses
H0A:
> There is no relationship between sentiment about a stock in news articles and this stock's price movements.
H0B:
> Future stock price predictions can not be improved by including news article sentiment about this stock as a predictor

# Files

* `Stock Timeseries`
>

* `Sentiment Timeseries`
> Data cleaning of the sentiment, generation of a sentiment timeseries per stock and making the timeseries stationary by taking differences
and executing Augmented Dickey-Fuller (ADF) tests.

* `Sentiment Analysis`
>

* `VAR`
> Prediction of the stock prices using a Vector Autoregressive Model (VAR), with stock price and sentiment as variables.

* `AR and H0A`
> Prediction of stock prices using an Autoregressive Model (AR) and comparison with the VAR to test hypothesis H0A.

* `H0B`
>

For more information about the analysis, please take a look at the presentation slides:
https://docs.google.com/presentation/d/1Gh-xMdgrWdgvud9PWHqU0W2k2CJ1teHg/edit?usp=sharing&ouid=112006383612537603453&rtpof=true&sd=true


