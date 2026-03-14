import numpy as np


class MonteCarlo:

    @staticmethod
    def call_price(S, K, T, r, sigma, simulations=100000):

        Z = np.random.standard_normal(simulations)

        ST = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

        payoff = np.maximum(ST - K, 0)

        price = np.exp(-r * T) * np.mean(payoff)

        return price