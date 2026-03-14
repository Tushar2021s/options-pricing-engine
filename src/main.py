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

# import numpy as np
# from black_scholes import BlackScholes
# from greeks import Greeks
# from implied_volatility import ImpliedVolatility
# from monte_carlo import MonteCarlo
# from volatility_smile import VolatilitySmile


# def main():

#     S = np.array([80, 90, 100, 110, 120])
#     K = 100
#     T = 1
#     r = 0.05
#     sigma = 0.2

#     # Vectorized Black-Scholes pricing
#     calls = BlackScholes.vectorized_call(S, K, T, r, sigma)

#     # print("Stock Prices:", S)
#     # print("Call Prices:", calls)
#     for s, c in zip(S, calls):
#         print(f"Stock: {s} -> Call Price: {c:.2f}")

#     # Implied Volatility calculation
#     market_price = 10.45

#     iv = ImpliedVolatility.newton_solver(
#         S=100,
#         K=100,
#         T=1,
#         r=0.05,
#         market_price=market_price
#     )

#     print("Implied Volatility:", iv)

#     # Monte Carlo pricing
#     mc_price = MonteCarlo.call_price(100, 100, 1, 0.05, 0.2)

#     print("Monte Carlo Call Price:", mc_price)

#     # Volatility Smile Plot
#     VolatilitySmile.plot()


# if __name__ == "__main__":
#     main()
# # import numpy as np
# # from black_scholes import BlackScholes
# # from greeks import Greeks
# # from implied_volatility import ImpliedVolatility

# # def main():

# #     S = np.array([80, 90, 100, 110, 120])
# #     K = 100
# #     T = 1
# #     r = 0.05
# #     sigma = 0.2

# #     calls = BlackScholes.vectorized_call(S, K, T, r, sigma)

# #     print("Stock Prices:", S)
# #     print("Call Prices:", calls)
# #     market_price = 10.45

# #     iv = ImpliedVolatility.newton_solver(S=100, K=100, T=1, r=0.05, market_price=market_price)

# # print("Implied Volatility:", iv)


# # if __name__ == "__main__":
# #     main()

# # # from black_scholes import BlackScholes
# # # from greeks import Greeks


# # # def main():

# # #     S = 100
# # #     K = 100
# # #     T = 1
# # #     r = 0.05
# # #     sigma = 0.2

# # #     call = BlackScholes.call_price(S, K, T, r, sigma)
# # #     put = BlackScholes.put_price(S, K, T, r, sigma)

# # #     print("Call Price:", call)
# # #     print("Put Price:", put)

# # #     print("Delta:", Greeks.delta(S, K, T, r, sigma))
# # #     print("Gamma:", Greeks.gamma(S, K, T, r, sigma))
# # #     print("Vega:", Greeks.vega(S, K, T, r, sigma))
# # #     print("Theta:", Greeks.theta(S, K, T, r, sigma))


# # # if __name__ == "__main__":
# # #     main()