import numpy as np
from scipy.stats import norm
from black_scholes import BlackScholes


class Greeks:

    @staticmethod
    def delta(S, K, T, r, sigma):

        d1 = BlackScholes.d1(S, K, T, r, sigma)

        return norm.cdf(d1)

    @staticmethod
    def gamma(S, K, T, r, sigma):

        d1 = BlackScholes.d1(S, K, T, r, sigma)

        return norm.pdf(d1) / (S * sigma * np.sqrt(T))

    @staticmethod
    def vega(S, K, T, r, sigma):

        d1 = BlackScholes.d1(S, K, T, r, sigma)

        return S * norm.pdf(d1) * np.sqrt(T)

    @staticmethod
    def theta(S, K, T, r, sigma):

        d1 = BlackScholes.d1(S, K, T, r, sigma)
        d2 = BlackScholes.d2(S, K, T, r, sigma)

        term1 = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
        term2 = r * K * np.exp(-r * T) * norm.cdf(d2)

        return term1 - term2