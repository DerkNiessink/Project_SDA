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
        ├── AR and H0B.ipynb
        └── H0A.ipynb

## Analysis

### Hypotheses
H0A: There is no relationship between sentiment about a stock in news articles and this stock's price movements.

H0B: Future stock price predictions can not be improved by including news article sentiment about this stock as a predictor.

### Summary of Research

During this project, timeseries analysis of historical prices and news article sentiment of 15 stocks was carried out using a Vector Autoregressive Model (VAR).
A Dataset of financial newpaper articles with including content was used in conjunction with (close) stock prices from Yahoo finance, on a (business) daily basis over a period from 2014 to 2019.

15 stocks with the most articles and a top 50 market capitalization were selected.
Sentiment scores were assigned to the articles an automatic dictionary approach, manually validated, and the dictionary sentiment prediction was found to be significantly different from the manual labeling.
However, the dictionary based sentiment scores were found to be significantly correlated to the manual sentiment scores, so the analysis was proceeded with.

To obtain a sentiment timeseries, the sum of the articles sentiment (value in between the range of -1 and 1) was taken per day. 
On days where no articles were published, the value of the previous sentiment datapoint was imputed.
After (percentage) differencing most price and sentiment timeseries were confirmed to be stationairy using ADF tests, implying a constant mean and variance of the timeseries over time. 

Optimum lag order was chosen using the AIC (Aikake Information Criterion).
Using a VAR model, a significant historical relationship was established for the prices of the stocks, rejecting Hypothesis H0A and thus supporting H1A.
Subsequently, the prices of these 15 stocks were forecasted 12 days in the future with a VAR fitted on using sentiment and stock price as predictors, 
and compared with a baseline of Autoregressive Model (AR) using only the lagged values of the stock price as predictors. To optimize the predition, the timeseries was split into 19 (non-overlapping) windows 
and seperate VAR and AR models were trained on each. The mean prediction was then used to do the forecasting. AR was fitted with the same number of lags as the VAR to form a representative baseline.

Findings indicate that, against expectations, the VAR had significantly higher RMSE than the baseline AR model, indicating that no improvement in forecasting over the baseline AR model was found
using this sample, significance assumptions and forecast period. Thus we were not able to reject hypothesis H0B, and RMSE prediction does not improve, in fact it worsens, when including sentiment in the analysis. 

Residuals were plotted to look for a systematic patern in the errors, but clear patern did not emerge across stocks. 
When (V)AR assumptions were tested, the normality of residuals and constant variance over time were the assumptions failed most often and for some windows, across windows, strong stationarity held for some but was violated for others.
Limitations of this research were: failed assumptions (especially 0 autocorrelation of resisduals), only a single forcast window, possible omitted variable bias, and ofcourse the assumption that what was true in the past will hold in the future. 
Also the fact that the VAR model uses insignificant coefficients to do the forecasting could have limited prediction accuracy. 
Another limitation was that the sentiment validation indicated that the automatic labeling of the articles was significantly different (although correlated to) the manual labeling. When moving p (the lag order) steps out of sample, VAR model also predicts the next days sentiment, based on its previous predictions. Possibly the model could be improved if it was given actual sentiment as an input data instead.

Summarizing the findings, a significant historical bidirectional relationship between price and sentiment was found using the VAR model, 
however the forecasts of the VAR model including sentiment coefficients performed significantly worse than a baseline AR model using sentiment alone.
Placing the findings in context of previous research [1], an improvement could have been to use a finance domain-specific sentiment dictionary (Loughran–McDonald Financial Dictionary). 
Their outcomes were better showing that LSTM models indeed performed better using sentiment and price data, as compared to price data alone, which our results did not show. Sentiment was also found to improve stock price predition using a random forest classifier and BERT NLP model for in [2]
These results were unable to be replicated using a simple VAR model and the vader_lexicon dictionairy that we used.
This could be due to better sentiment classification using this finance domain-specific dictionairy, or using the LSTM model.
Also, as assumptions were violated, it seems that the VAR model simply was not a right fit for the data.


## Files

* `Stock Timeseries`
> Data cleaning of the stock price data, generation of a sentiment timeseries per stock and making the timeseries stationary by taking percentage differences and testing for stationarity by executing Augmented Dickey-Fuller (ADF) tests. Also, VAR forecasting for 1 stock ('AAPL') is tested.

* `Sentiment Timeseries`
> Data cleaning of the sentiment, generation of a sentiment timeseries per stock and making the timeseries stationary by taking differences and testing for stationarity by executing Augmented Dickey-Fuller (ADF) tests.

* `Sentiment Analysis`
> Here the sentiment in news articles is analysed by a dictionairy based method. Then it is manually validated.

* `VAR`
> Prediction of the stock prices using a Vector Autoregressive Model (VAR), with stock price and sentiment as variables. Including assumption VAR tests. The RMSE's of this predictions are used in `AR and H0B`

* `AR and H0B`
> Prediction of stock prices using an Autoregressive Model (AR) and comparison with the Vector Autoregressive Model (VAR) to test hypothesis H0B. Including AR assumption tests.

* `H0A`
> VAR fit on Historical data using sentiment and stock price as predictors

## References

For more information about the analysis, please take a look at the presentation slides:
https://docs.google.com/presentation/d/1Gh-xMdgrWdgvud9PWHqU0W2k2CJ1teHg/edit?usp=sharing&ouid=112006383612537603453&rtpof=true&sd=true

New papers data:
https://www.kaggle.com/gennadiyr/us-equities-news-data

Yahoo finance stock data:
https://finance.yahoo.com/
https://pypi.org/project/yfinance/

Twitter data (did not use in the end):
https://www.kaggle.com/datasets/kazanova/sentiment140
https://www.kaggle.com/datasets/utkarshxy/stock-markettweets-lexicon-data

[1]Li, X., Wu, P., & Wang, W. (2020). Incorporating stock prices and news sentiments for stock market prediction: A case of Hong Kong. Information Processing & Management, 57(5), 102212. https://www.sciencedirect.com/science/article/abs/pii/S0306457319307952

[2] Fazlija, B., & Harder, P. (2022). Using Financial News Sentiment for Stock Price Direction Prediction. Mathematics, 10(13), 2156.
https://www.mdpi.com/2227-7390/10/13/2156




