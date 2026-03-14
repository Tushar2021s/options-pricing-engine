import numpy as np
from black_scholes import BlackScholes
from greeks import Greeks


def main():

    S = np.array([80, 90, 100, 110, 120])
    K = 100
    T = 1
    r = 0.05
    sigma = 0.2

    calls = BlackScholes.vectorized_call(S, K, T, r, sigma)

    print("Stock Prices:", S)
    print("Call Prices:", calls)


if __name__ == "__main__":
    main()

# from black_scholes import BlackScholes
# from greeks import Greeks


# def main():

#     S = 100
#     K = 100
#     T = 1
#     r = 0.05
#     sigma = 0.2

#     call = BlackScholes.call_price(S, K, T, r, sigma)
#     put = BlackScholes.put_price(S, K, T, r, sigma)

#     print("Call Price:", call)
#     print("Put Price:", put)

#     print("Delta:", Greeks.delta(S, K, T, r, sigma))
#     print("Gamma:", Greeks.gamma(S, K, T, r, sigma))
#     print("Vega:", Greeks.vega(S, K, T, r, sigma))
#     print("Theta:", Greeks.theta(S, K, T, r, sigma))


# if __name__ == "__main__":
#     main()