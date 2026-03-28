import numpy as np
from black_scholes import BlackScholes
from greeks import Greeks
from implied_volatility import ImpliedVolatility
from monte_carlo import MonteCarlo
from volatility_smile import VolatilitySmile
from binomial_tree import BinomialTree


def main():

    print("\n=== Options Pricing Engine ===\n")

    # User Inputs
    S = float(input("Enter Stock Price (S): "))
    K = float(input("Enter Strike Price (K): "))
    T = float(input("Enter Time to Maturity in years (T): "))
    r = float(input("Enter Risk-Free Rate (r): "))
    sigma = float(input("Enter Volatility (sigma): "))

    print("\n--- Black-Scholes Pricing ---")

    call = BlackScholes.call_price(S, K, T, r, sigma)
    put = BlackScholes.put_price(S, K, T, r, sigma)

    print(f"Call Price: {call:.4f}")
    print(f"Put Price: {put:.4f}")

    print("\n--- Greeks ---")

    print(f"Delta: {Greeks.delta(S, K, T, r, sigma):.4f}")
    print(f"Gamma: {Greeks.gamma(S, K, T, r, sigma):.6f}")
    print(f"Vega: {Greeks.vega(S, K, T, r, sigma):.4f}")
    print(f"Theta: {Greeks.theta(S, K, T, r, sigma):.4f}")

    print("\n--- Implied Volatility ---")

    market_price = float(input("Enter Market Option Price: "))

    iv = ImpliedVolatility.newton_solver(S, K, T, r, market_price)

    print(f"Implied Volatility: {iv:.4f}")

    print("\n--- Monte Carlo Pricing ---")

    mc_price = MonteCarlo.call_price(S, K, T, r, sigma)

    print(f"Monte Carlo Call Price: {mc_price:.4f}")

    print("\nGenerating Volatility Smile Plot...")

    VolatilitySmile.plot()
    print("\n--- Binomial Tree Pricing ---")

    steps = int(input("Enter number of binomial steps: "))

    bt_price = BinomialTree.call_price(S, K, T, r, sigma, steps)

    print(f"Binomial Tree Call Price: {bt_price:.4f}")


if __name__ == "__main__":
    main()

