import streamlit as st
from black_scholes import black_scholes, black_scholes_greeks
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


# Set Streamlit page layout to wide
st.set_page_config(layout="wide")
st.write("# Black-Scholes Option Pricing Calculator")

with st.sidebar:
    st.title("📊 Black-Scholes Model")

def user_input():
    st.sidebar.divider()
    # User inputs for Black-Scholes parameters
    S = st.sidebar.number_input("Current Stock Price", min_value=0.0, value=100.0)
    K = st.sidebar.number_input("Strike Price", min_value=0.0, value=100.0)
    T = st.sidebar.number_input("Time to Expiration (Years)", min_value=0.0, value=1.0)
    r = st.sidebar.number_input("Risk-Free Interest Rate (%)", min_value=0.0, value=5.0) / 100
    sigma = st.sidebar.number_input("Volatility (%)", min_value=0.0, value=20.0) / 100
    # Store user inputs in a dictionary
    dic = {
        "Current Asset Price (S)": [S],
        "Strike Price (K)": [K],
        "Time to Expiration (T)": [T],
        "Risk-Free Interest Rate (r)": [r],
        "Volatility (σ)": [sigma]
    }
    return dic

def heatmap_parameters(volatility, spot_price):
    volatility_lower_bound = volatility-volatility*0.5
    volatility_upper_bound = volatility+volatility*0.5
    spot_price_lower_bound = spot_price-spot_price*0.5
    spot_price_upper_bound = spot_price+spot_price*0.5
    st.sidebar.divider()
    # Section for heatmap parameter selection
    st.sidebar.button("### Heatmap Parameters")
    min_spot_price = st.sidebar.number_input("Min Spot Price", min_value=0.0, value=spot_price_lower_bound, key="min_spot_price")
    max_spot_price = st.sidebar.number_input("Max Spot Price", min_value=0.1, value=spot_price_upper_bound, key="max_spot_price")
    spot_prices_range = [min_spot_price, max_spot_price]
    # Slider for volatility range
    volatilities_range = np.array(st.sidebar.slider("Volatilities (%)", volatility_lower_bound*100, volatility_upper_bound*100, (volatility_lower_bound*100, volatility_upper_bound*100), step=0.01, key="volatilities_range"))/100
    return spot_prices_range, volatilities_range

# Get user input and heatmap parameters
user_input_information = user_input()
S, K, T, r, sigma = user_input_information["Current Asset Price (S)"][0], user_input_information["Strike Price (K)"][0], user_input_information["Time to Expiration (T)"][0], user_input_information["Risk-Free Interest Rate (r)"][0], user_input_information["Volatility (σ)"][0]
user_input_information_df = pd.DataFrame(user_input_information)
spot_prices_range, volatilities_range = heatmap_parameters(sigma, S)

# Display user input parameters as a dataframe
st.dataframe(user_input_information_df, use_container_width=True)

# Common configuration for info boxes
wch_colour_box1 = (144, 238, 144)  # green background for put value
wch_colour_box2 = (250, 218, 217)  # light red background for call value
wch_colour_font = (0, 0, 0)        # black font color
fontsize = 14

# Create two columns for displaying option values
col1, col2 = st.columns(2)

# Calculate
call, put = black_scholes(S, K, T, r, sigma)

# First box: Put value
with col1:
    # Display the calculated put option value
    htmlstr1 = f"""<p style="background-color:rgb({wch_colour_box1[0]},{wch_colour_box1[1]},{wch_colour_box1[2]},0.75);
                    color: rgb({wch_colour_font[0]},{wch_colour_font[1]},{wch_colour_font[2]});
                    font-size: {fontsize}px;
                    border-radius: 7px;
                    padding: 10px 12px;
                    line-height:10px;
                    margin: 0;
                    height: 60px;
                    text-align: center;">
                    <i class></i> PUT value
                    <br>
                    <br>
                    <br>
                    <span style='font-size: 22px;'> <b>${put:.2f}</b></span>
                    </p>"""
    st.markdown(htmlstr1, unsafe_allow_html=True)

# Second box: Call value
with col2:
    # Display the calculated call option value
    htmlstr2 = f"""<p style="background-color:rgb({wch_colour_box2[0]},{wch_colour_box2[1]},{wch_colour_box2[2]},0.75);
                    color: rgb({wch_colour_font[0]},{wch_colour_font[1]},{wch_colour_font[2]});
                    font-size: {fontsize}px;
                    border-radius: 7px;
                    padding: 10px 12px;
                    line-height:10px;
                    margin: 0;
                    height: 60px;
                    text-align: center;">
                    <i class></i> CALL Value
                    <br>
                    <br>
                    <br>
                    <span style='font-size: 22px; font-weight: bald'> <b>${call:.2f}</b></span>
                    </p>"""
    st.markdown(htmlstr2, unsafe_allow_html=True)

st.markdown("### ")
st.write("## Options Price - Interactive Heatmap")
st.caption("Shows how option prices vary with stock price and volatility, holding other inputs constant.")

col4, col5 = st.columns(2)
# Generate spot price and volatility ranges for the heatmap
spot_prices = np.linspace(spot_prices_range[0], spot_prices_range[1], 10)
volatilities = np.linspace(volatilities_range[0], volatilities_range[1], 10)
# Create meshgrid for spot prices and volatilities
S_grid, sigma_grid = np.meshgrid(spot_prices, volatilities)
call_price, put_price = black_scholes(S_grid, K, T, r, sigma_grid)

# Call option price heatmap
with col4:
    st.write("### Call Option Price Heatmap")
    plt.figure(figsize=(10, 8))
    # Plot heatmap for call option prices
    sns.heatmap(np.round(call_price, 2), xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities*100, 2), cmap='magma', annot=True, cbar_kws={'label': 'Call Price'})
    plt.xlabel("Spot Price")
    plt.ylabel("Volatility(%)")
    st.pyplot(plt)

# Put option price heatmap
with col5:
    st.write("### Put Option Price Heatmap")
    plt.figure(figsize=(10, 8))
    # Plot heatmap for put option prices
    sns.heatmap(np.round(put_price, 2), xticklabels=np.round(spot_prices, 2), yticklabels=np.round(volatilities*100, 2), cmap='magma', annot=True, cbar_kws={'label': 'Put Price'})
    plt.xlabel("Spot Price")
    plt.ylabel("Volatility(%)")
    st.pyplot(plt)

st.write("## Option Greeks")
st.markdown("### ")
greeks = black_scholes_greeks(S, K, T, r, sigma)

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.subheader("Calls")
    st.subheader("Puts")
    
with col2:
    st.metric("Delta", f"{greeks['delta_call']:.3f}")
    st.metric("Delta", f"{greeks['delta_put']:.3f}")

with col3:
    st.metric("Gamma", f"{greeks['gamma']:.5f}")
    st.metric("Gamma", f"{greeks['gamma']:.5f}")

with col4:
    st.metric("Vega", f"{greeks['vega']:.3f}")
    st.metric("Vega", f"{greeks['vega']:.3f}")

with col5:
    st.metric("Call Theta", f"{greeks['theta_call']:.3f}")
    st.metric("Put Theta", f"{greeks['theta_put']:.3f}")

with col6:
    st.metric("Call Rho", f"{greeks['rho_call']:.3f}")
    st.metric("Put Rho", f"{greeks['rho_put']:.3f}")

st.markdown("### ")
st.write("## Greeks vs Stock Price")
st.markdown("### ")

S_range = np.linspace(0.5*S, 1.5*S, 100)

delta_call_vals = []
delta_put_vals = []
gamma_vals = []
vega_vals = []
theta_call_vals = []
theta_put_vals = []
rho_call_vals = []
rho_put_vals = []

for s in S_range:
    g = black_scholes_greeks(s, K, T, r, sigma)

    delta_call_vals.append(g["delta_call"])
    delta_put_vals.append(g["delta_put"])
    gamma_vals.append(g["gamma"])
    vega_vals.append(g["vega"])
    theta_call_vals.append(g["theta_call"])
    theta_put_vals.append(g["theta_put"])
    rho_call_vals.append(g["rho_call"])
    rho_put_vals.append(g["rho_put"])

col1, col2 = st.columns(2)

with col1:
    fig1, ax = plt.subplots()
    ax.plot(S_range, delta_call_vals, label="Call Delta")
    ax.plot(S_range, delta_put_vals, label="Put Delta")
    ax.set_title("Delta vs Stock Price")
    ax.set_xlabel("Stock Price")
    ax.set_ylabel("Delta")
    ax.legend()

    st.pyplot(fig1)

with col2:
    fig2, ax = plt.subplots()
    ax.plot(S_range, gamma_vals)
    ax.set_title("Gamma vs Stock Price")
    ax.set_xlabel("Stock Price")
    ax.set_ylabel("Gamma")

    st.pyplot(fig2)

col3, col4 = st.columns(2)

with col3:
    fig3, ax = plt.subplots()
    ax.plot(S_range, vega_vals)
    ax.set_title("Vega vs Stock Price")
    ax.set_xlabel("Stock Price")
    ax.set_ylabel("Vega")

    st.pyplot(fig3)

with col4:

    fig4, ax = plt.subplots()
    ax.plot(S_range, theta_call_vals, label="Call Theta")
    ax.plot(S_range, theta_put_vals, label="Put Theta")
    ax.set_title("Theta vs Stock Price")
    ax.set_xlabel("Stock Price")
    ax.set_ylabel("Theta")
    ax.legend()

    st.pyplot(fig4)

col_left, col_center, col_right = st.columns([1, 2, 1])

with col_center:
    fig, ax = plt.subplots()
    ax.plot(S_range, rho_call_vals, label="Call Rho")
    ax.plot(S_range, rho_put_vals, label="Put Rho")
    ax.set_title("Rho vs Stock Price")
    ax.set_xlabel("Stock Price")
    ax.set_ylabel("Rho")
    ax.legend()

    st.pyplot(fig)
