import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

class StockVisualizer:
    def __init__(self):
        self.data = None
        self.symbol = None
    
    def fetch_data(self, symbol, period='1y'):
        """
        Fetch historical stock data from Yahoo Finance
        
        Parameters:
        symbol (str): Stock symbol (e.g., 'MSFT' for Microsoft)
        period (str): Time period to fetch ('1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max')
        """
        self.symbol = symbol
        stock = yf.Ticker(symbol)
        self.data = stock.history(period=period)
        return self.data
    
    def plot_price_history(self):
        """Plot daily closing prices with volume"""
        if self.data is None:
            raise ValueError("No data available. Please fetch data first.")
        
        # Create figure with two subplots
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8), height_ratios=[3, 1])
        
        # Plot closing prices
        ax1.plot(self.data.index, self.data['Close'], color='blue')
        ax1.set_title(f'{self.symbol} Stock Price History')
        ax1.set_ylabel('Price (USD)')
        ax1.grid(True)
        
        # Plot volume
        ax2.bar(self.data.index, self.data['Volume'], color='gray', alpha=0.5)
        ax2.set_ylabel('Volume')
        ax2.grid(True)
        
        plt.tight_layout()
        return fig
    
    def calculate_moving_averages(self, short_window=20, long_window=50):
        """Calculate and plot moving averages"""
        if self.data is None:
            raise ValueError("No data available. Please fetch data first.")
        
        # Calculate moving averages
        self.data['SMA_short'] = self.data['Close'].rolling(window=short_window).mean()
        self.data['SMA_long'] = self.data['Close'].rolling(window=long_window).mean()
        
        # Create plot
        plt.figure(figsize=(12, 6))
        plt.plot(self.data.index, self.data['Close'], label='Price', alpha=0.7)
        plt.plot(self.data.index, self.data['SMA_short'], 
                label=f'{short_window}-day SMA', alpha=0.7)
        plt.plot(self.data.index, self.data['SMA_long'], 
                label=f'{long_window}-day SMA', alpha=0.7)
        
        plt.title(f'{self.symbol} Stock Price with Moving Averages')
        plt.xlabel('Date')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid(True)
        return plt.gcf()
    
    def calculate_daily_returns(self):
        """Calculate and plot daily returns distribution"""
        if self.data is None:
            raise ValueError("No data available. Please fetch data first.")
        
        # Calculate daily returns
        self.data['Daily_Return'] = self.data['Close'].pct_change() * 100
        
        # Create histogram
        plt.figure(figsize=(10, 6))
        self.data['Daily_Return'].hist(bins=50, alpha=0.7)
        plt.title(f'{self.symbol} Daily Returns Distribution')
        plt.xlabel('Daily Returns (%)')
        plt.ylabel('Frequency')
        plt.grid(True)
        return plt.gcf()

    def generate_summary_statistics(self):
        """Generate summary statistics for the stock"""
        if self.data is None:
            raise ValueError("No data available. Please fetch data first.")
        
        stats = {
            'Current Price': self.data['Close'][-1],
            'Average Price': self.data['Close'].mean(),
            'Highest Price': self.data['Close'].max(),
            'Lowest Price': self.data['Close'].min(),
            'Daily Return Std Dev': self.data['Close'].pct_change().std() * 100,
            'Average Volume': self.data['Volume'].mean()
        }
        return pd.Series(stats)
