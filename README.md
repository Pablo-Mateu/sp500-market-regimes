# 📈 Dynamic Market Regime Modeling of the S&P 500 (GMMHMM)

## 🎯 Project Overview

This project employs an advanced, unsupervised **Hidden Markov Model with Gaussian Mixtures (GMMHMM)** to identify and analyze the **three principal market regimes** (Bull, Bear, and Transition) within the S&P 500 index. The analysis provides a data-driven framework for **dynamic risk management** by explicitly modeling the **asymmetry of risk** observed in real-world finance.

## 🛠️ Methodology and Model Architecture

The GMMHMM architecture was custom-built to handle key financial data characteristics:

| Parameter | Value | Financial Rationale |
| :--- | :--- | :--- |
| **Model Type** | GMMHMM (K=3, M=2) | Used two Gaussian components (`M=2`) per regime to model **Fat Tails** in return distribution. |
| **Covariance Type** | 'full' | **CRITICAL:** Enables the model to capture the negative correlation between returns and volatility (**Leverage Effect**), crucial for defining the Bear regime. |
| **Features Used** | Log Return, Volatility (21d), Momentum (126d) | Captures directional change, short-term risk, and long-term trend. |
| **Reproducibility** | `np.random.seed(123)` | Ensures the stability and deterministic assignment of regimes across all runs. |

## ✅ Key Findings and Actionable Conclusions

The model successfully separates market history into three distinct states, validated by both statistical properties and historical events.

### 1. Regime Characterization and Asymmetry

The analysis confirms a clear distinction in the volatility-return trade-off:

| Regime | Risk Profile | Volatility (Annualized) | Expected Return |
| :--- | :--- | :--- | :--- |
| **Bull (0)** | **Optimal** | **LOWEST** (e.g., $\approx 9.6\%$ ) | HIGHEST (Positive) |
| **Bear (1)** | **Extreme Risk** | **HIGHEST** (e.g., $\approx 23.7\%$ ) | Negative |
| **Transition (2)** | Poor/Neutral | Medium | Near Zero |

### 2. Regime Persistence and Duration

Analysis of the fitted Transition Matrix provides a clear timescale for risk management decisions:

| Regime | Persistence (Pii) | Expected Duration |
| :--- | :--- | :--- |
| **Bull** | $98.48\%$ | **$\approx 66$ trading days** |
| **Bear** | $98.25\%$ | **$\approx 57$ trading days** |
| **Transition** | $97.94\%$ | $\approx 49$ trading days |

**Conclusion for Strategy:** The model shows that once the market enters the high-risk Bear regime, it is expected to persist for approximately two to three months. This dictates that risk mitigation strategies (hedging, reducing exposure) must be maintained over this timescale.

---

## 🚀 Repository Structure and Usage

The analysis is conducted sequentially across the following Jupyter Notebooks:

1.  **`01_EDA.ipynb`:** Data loading, cleaning, feature engineering, and crucial **stationarity testing** (ADF test) to prepare data for time- series modeling.
2.  **`02_HMM_Modeling.ipynb`:** Model configuration, training, Viterbi decoding (inference), regime validation, **transition matrix analysis**, and the final visualization of the S&P 500 price colored by its inferred regime.