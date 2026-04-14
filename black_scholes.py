import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2 / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    call = S * norm.cdf(d1) - K * np.exp(-r*T) * norm.cdf(d2)
    put = K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return call, put

def black_scholes_greeks(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2 / 2)*T) / (sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)

    # Delta
    delta_call = norm.cdf(d1)
    delta_put = norm.cdf(d1) - 1

    # Gamma (same for call & put)
    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))

    # Vega (same for call & put)
    vega = S * norm.pdf(d1) * np.sqrt(T)

    # Theta (per year)
    theta_call = (-S * norm.pdf(d1) * sigma / (2*np.sqrt(T))
                  - r * K * np.exp(-r*T) * norm.cdf(d2))

    theta_put = (-S * norm.pdf(d1) * sigma / (2*np.sqrt(T))
                 + r * K * np.exp(-r*T) * norm.cdf(-d2))

    # Rho
    rho_call = K * T * np.exp(-r*T) * norm.cdf(d2)
    rho_put = -K * T * np.exp(-r*T) * norm.cdf(-d2)

    return {
        "delta_call": delta_call,
        "delta_put": delta_put,
        "gamma": gamma,
        "vega": vega,
        "theta_call": theta_call,
        "theta_put": theta_put,
        "rho_call": rho_call,
        "rho_put": rho_put
    }  