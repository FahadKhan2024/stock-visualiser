# Stock Visualizer

## Overview
The Stock Visualizer is a Python-based tool designed to fetch, analyze, and visualize historical stock data from Yahoo Finance. By leveraging the `yfinance` and `matplotlib` libraries, this tool provides an intuitive interface for users to gain insights into stock performance over various time periods.

## Features
- **Data Fetching**: Seamlessly fetch historical stock data for a given symbol and time period using the Yahoo Finance API.
- **Price History Visualization**: Plot daily closing prices along with trading volumes to observe trends and patterns.
- **Moving Averages Calculation**: Compute and visualize short-term and long-term moving averages to analyze stock performance.
- **Daily Returns Analysis**: Calculate and display the distribution of daily returns to understand stock volatility.
- **Summary Statistics**: Generate key summary statistics such as current price, average price, highest and lowest prices, daily return standard deviation, and average volume.

## Usage
The Stock Visualizer encapsulates its functionality within a class, providing an easy-to-use interface for fetching data, plotting, and analysis. Users can quickly integrate this tool into their workflow to perform comprehensive stock analysis.

## Installation
To use the Stock Visualizer, you need to have the following Python libraries installed:
- `yfinance`
- `pandas`
- `matplotlib`

Install the required libraries using pip:
```sh
pip install yfinance pandas matplotlib
