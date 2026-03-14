import numpy as np
from black_scholes import BlackScholes
from greeks import Greeks


class ImpliedVolatility:

    @staticmethod
    def newton_solver(S, K, T, r, market_price, tol=1e-5, max_iter=100):

        sigma = 0.2  # initial guess

        for i in range(max_iter):

            price = BlackScholes.call_price(S, K, T, r, sigma)
            vega = Greeks.vega(S, K, T, r, sigma)

            diff = price - market_price

            if abs(diff) < tol:
                return sigma

            sigma = sigma - diff / vega

        return sigma