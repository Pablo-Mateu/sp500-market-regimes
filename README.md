# 📈 Dynamic Market Regime Modeling of the S&P 500 (GMMHMM)

## 🎯 Project Overview

This project implements an advanced **Hidden Markov Model with Gaussian Mixtures (GMMHMM)** to identify and characterize the **three principal market regimes** (Bull, Bear, and Transition) within the S&P 500 index. The analysis provides a robust, data-driven framework for **dynamic risk management** by explicitly recognizing the **risk asymmetry** inherent in financial markets (i.e., crashes are more volatile than rallies).

## 🛠️ Methodology and Model Architecture

The GMMHMM architecture was specifically chosen and configured to handle complex financial data characteristics:

| Parameter | Value | Financial Justification |
| :--- | :--- | :--- |
| **Core Model** | GMMHMM (Gaussian Mixture) | Necessary to model the non-normal distribution of returns and **Fat Tails** (leptokurtosis). |
| **N Components (K)** | 3 | Allows for the economic distinction between **Growth (Bull)**, **Panic (Bear)**, and **Uncertainty (Transition)**. |
| **Covariance Type** | 'full' | **CRITICAL:** Enables the model to capture the negative correlation between returns and volatility, known as the **Leverage Effect**. |
| **Features Used** | Log Return, Volatility (21d), Momentum (126d) | Captures directional change, short-term risk, and long-term trend. |
| **Reproducibility** | `np.random.seed(123)` | Ensures the regime assignments (0, 1, 2) are deterministic across all runs. |

## ✅ Key Findings and Actionable Conclusions

The model successfully separates market history into distinct states, yielding valuable insights:

### 1. Market Asymmetry and Validation

The model validates the core tenet of market risk: **"The market goes up the stairs and down the elevator."**

| Regime | Risk Profile | Volatility (Risk) | Return (Reward) |
| :--- | :--- | :--- | :--- |
| **Bull (Growth)** | **Optimal** | **LOWEST** ($\approx 9.6\%$ annualized) | HIGHEST (Positive) |
| **Bear (Panic)** | **Extreme** | **HIGHEST** ($\approx 23.7\%$ annualized) | Negative |

### 2. Regime Persistence

Analysis of the Transition Matrix (`model.transmat_`) reveals the expected duration of each state, providing a crucial timescale for strategizing:

* **Bull Regime Duration:** $\approx 66$ trading days on average.
* **Bear Regime Duration:** $\approx 57$ trading days on average.

**Conclusion for Strategy:** When the model signals a switch to the Bear regime, portfolio managers are advised to immediately reduce risk exposure and maintain a defensive posture, as the high-risk state is statistically expected to persist for nearly two months.

---

## 🚀 Repository Structure and Usage

The analysis is conducted sequentially across the following Jupyter Notebooks:

1.  **`01_EDA.ipynb`:** Data loading, cleaning, and financial feature engineering (Log Returns, Volatility, Momentum).
2.  **`02_HMM_Modeling.ipynb`:** Contains the model setup, training, Viterbi decoding (inference), regime validation, and the final visualization of the S&P 500 price colored by its inferred regime.