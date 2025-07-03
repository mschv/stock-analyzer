import pandas as pd
import numpy as np

def calculate_daily_returns(df:pd.DataFrame)->pd.Series:
    return df['Close'].pct_change()

def calculate_cumulative_return(df:pd.DataFrame)->float:
    return(df['Close'].iloc[-1]/df['Close'].iloc[0])-1

def calculate_volatility(daily_return:pd.Series)->float:
    return daily_return.std()*np.sqrt(252) #annualized

def calculate_sharpe_ratio(daily_returns:pd.Series,risk_free_rate=0.01)->float:
    excess_return=daily_returns.mean()*252-risk_free_rate
    volatility=daily_returns.std()*np.sqrt(252)
    if volatility==0:
        return 0
    return excess_return/volatility