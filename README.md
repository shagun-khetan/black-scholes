
# Black-Scholes Option Pricing

This project is a Python-based tool for pricing European call and put options using the Black-Scholes model. It is designed for anyone interested in financial engineering, quantitative finance, or simply learning about option pricing—even if you have no prior knowledge of the Black-Scholes formula.

## What is the Black-Scholes Model?

The Black-Scholes model is a mathematical formula used to determine the fair price of European-style options. Developed by Fischer Black, Myron Scholes, and Robert Merton in 1973, it revolutionized financial markets by providing a systematic way to value options. The model assumes that:

- The price of the underlying asset follows a lognormal distribution (i.e., it moves randomly but with a predictable average and volatility).
- Markets are efficient (no arbitrage opportunities).
- There are no dividends during the option's life.
- The risk-free interest rate and volatility are constant.
- Options can only be exercised at expiration (European style).

The formula takes into account the current price of the asset, the strike price, time to expiration, risk-free interest rate, and volatility to calculate the theoretical price of call and put options.

## Project Overview

This repository provides:

- A clear, modular Python implementation of the Black-Scholes pricing formula
- A command-line interface for easy interaction
- Example usage and guidance for customizing your own option pricing scenarios

### Main Features

- Calculate the price of European call and put options
- Input your own parameters (stock price, strike price, time to maturity, risk-free rate, volatility)
- Easily modify or extend the code for educational or practical use

## File Structure

- `app.py`: Main script to run the application and interact with the user
- `black_scholes.py`: Contains the core Black-Scholes pricing logic
- `requirements.txt`: Lists required Python packages

## How to Use

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the application:**
   ```bash
   python app.py
   ```

## Black-Scholes Formulas


The Black-Scholes model uses the following formulas to price European call and put options. These are written in plain text for compatibility with GitHub's markdown renderer.

### Option Pricing Equations

Let:
- S = Current price of the underlying asset
- K = Strike price of the option
- T = Time to expiration (in years)
- r = Risk-free interest rate (annualized)
- sigma = Volatility of the underlying asset (annualized standard deviation)

Define:

   d1 = [ln(S/K) + (r + sigma^2 / 2) * T] / (sigma * sqrt(T))
   d2 = d1 - sigma * sqrt(T)

The price of a European call option (C) and put option (P) are:

   C = S * N(d1) - K * exp(-r*T) * N(d2)
   P = K * exp(-r*T) * N(-d2) - S * N(-d1)

where N(x) is the cumulative distribution function (CDF) of the standard normal distribution.

## The Greeks


The Greeks are sensitivities of the option price to various parameters. This project calculates the following Greeks:

| Greek      | Meaning                                 | Formula (Call)                                                        | Formula (Put)                                                        |
|------------|-----------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------|
| Delta      | Sensitivity to underlying price (S)     | Delta_call = N(d1)                                                   | Delta_put = N(d1) - 1                                                |
| Gamma      | Sensitivity of Delta to S               | Gamma = N'(d1) / (S * sigma * sqrt(T))                               | Gamma = N'(d1) / (S * sigma * sqrt(T))                               |
| Vega       | Sensitivity to volatility (sigma)       | Vega = S * N'(d1) * sqrt(T)                                          | Vega = S * N'(d1) * sqrt(T)                                          |
| Theta      | Sensitivity to time (T)                 | Theta_call = -[S * N'(d1) * sigma / (2 * sqrt(T))] - rK * exp(-rT) * N(d2) | Theta_put = -[S * N'(d1) * sigma / (2 * sqrt(T))] + rK * exp(-rT) * N(-d2) |
| Rho        | Sensitivity to interest rate (r)        | Rho_call = K * T * exp(-rT) * N(d2)                                  | Rho_put = -K * T * exp(-rT) * N(-d2)                                 |

Where N'(d1) is the standard normal probability density function (PDF), and N(x) is the CDF.

## What the Project Does

- Computes the theoretical price of European call and put options using the Black-Scholes model
- Calculates the main Greeks (Delta, Gamma, Vega, Theta, Rho) for both calls and puts
- Provides a simple interface for users to input parameters and see results
- Designed for both educational and practical use

## Example

You can modify `app.py` to input your own parameters for option pricing, or use the provided interface to experiment with different scenarios.

## Requirements

- Python 3.7 or higher
- See `requirements.txt` for required packages


