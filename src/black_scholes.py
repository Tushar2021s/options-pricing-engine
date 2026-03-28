from pricing_model import PricingModel
import numpy as np
from scipy.stats import norm


class BlackScholes(PricingModel):

    @staticmethod
    def d1(S, K, T, r, sigma):
        return (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

    @staticmethod
    def d2(S, K, T, r, sigma):
        return BlackScholes.d1(S, K, T, r, sigma) - sigma * np.sqrt(T)

    @staticmethod
    def call_price(S, K, T, r, sigma):
        d1 = BlackScholes.d1(S, K, T, r, sigma)
        d2 = BlackScholes.d2(S, K, T, r, sigma)

        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

    @staticmethod
    def put_price(S, K, T, r, sigma):
        d1 = BlackScholes.d1(S, K, T, r, sigma)
        d2 = BlackScholes.d2(S, K, T, r, sigma)

        return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    @staticmethod
    def vectorized_call(S, K, T, r, sigma):
        S = np.array(S)

        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)

        return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)

    # 🔥 NEW METHOD (this is the upgrade)
    def price(self, S, K, T, r, sigma, option_type="call"):
        if option_type == "call":
            return self.call_price(S, K, T, r, sigma)
        else:
            return self.put_price(S, K, T, r, sigma)