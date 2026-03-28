from pricing_model import PricingModel
import numpy as np


class BinomialTree(PricingModel):

    def __init__(self, steps=100):
        self.steps = steps

    def price(self, S, K, T, r, sigma, option_type="call"):

        dt = T / self.steps

        u = np.exp(sigma * np.sqrt(dt))
        d = 1 / u

        p = (np.exp(r * dt) - d) / (u - d)

        # Stock prices at maturity
        prices = np.zeros(self.steps + 1)

        for i in range(self.steps + 1):
            prices[i] = S * (u ** (self.steps - i)) * (d ** i)

        # Option payoff
        if option_type == "call":
            values = np.maximum(prices - K, 0)
        else:
            values = np.maximum(K - prices, 0)

        # Backward induction
        for step in range(self.steps - 1, -1, -1):
            for i in range(step + 1):
                values[i] = np.exp(-r * dt) * (
                    p * values[i] + (1 - p) * values[i + 1]
                )

        return values[0]