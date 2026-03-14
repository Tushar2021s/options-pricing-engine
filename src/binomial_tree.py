import numpy as np


class BinomialTree:

    @staticmethod
    def call_price(S, K, T, r, sigma, steps=100):

        dt = T / steps

        u = np.exp(sigma * np.sqrt(dt))
        d = 1 / u

        p = (np.exp(r * dt) - d) / (u - d)

        # Stock prices at maturity
        prices = np.zeros(steps + 1)

        for i in range(steps + 1):
            prices[i] = S * (u ** (steps - i)) * (d ** i)

        # Option payoffs at maturity
        option_values = np.maximum(prices - K, 0)

        # Backward induction
        for step in range(steps - 1, -1, -1):
            for i in range(step + 1):
                option_values[i] = np.exp(-r * dt) * (
                    p * option_values[i] + (1 - p) * option_values[i + 1]
                )

        return option_values[0]