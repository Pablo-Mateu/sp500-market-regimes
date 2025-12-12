# S&P 500 Market Regime Detection

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 Overview
Market behavior changes over time. Strategies that work in a "Bull Market" often fail during high-volatility crashes. This project applies **Unsupervised Machine Learning** to automatically detect latent **Market Regimes** (e.g., Low Volatility/Growth vs. High Volatility/Crash) in the S&P 500 index.

Instead of trying to predict the exact price of tomorrow, we focus on identifying the underlying **risk state** of the market to aid in asset allocation decisions.

## 🎯 Objectives
* **Data Engineering:** Transform raw price data into financial features (Log Returns, Rolling Volatility, Momentum).
* **Unsupervised Learning:** Apply **K-Means Clustering** and **Gaussian Hidden Markov Models (HMM)** to segment market history.
* **Visualization:** Create intuitive visualizations showing how market regimes have shifted during historical crises (2000 Dot-com, 2008 GFC, 2020 COVID).

## 🗂️ Project Structure
```text
sp500-market-regimes/
├── data/                       # Raw and processed datasets (CSV)
├── notebooks/                  # Jupyter Notebooks for analysis and modeling
│   ├── 01_EDA.ipynb            # Exploratory Data Analysis & Feature Engineering
│   └── 02_HMM_Modeling.ipynb   # K-Means & HMM Implementation (In Progress)
├── src/                        # Helper scripts and functions
├── images/                     # Plots and result visualizations
└── README.md                   # Project documentation