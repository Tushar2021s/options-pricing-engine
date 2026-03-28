from pricing_model import PricingModel
import numpy as np

class MonteCarlo(PricingModel):

    def __init__(self, simulations=10000):
        self.simulations = simulations

    def price(self, S, K, T, r, sigma, option_type="call"):

        Z = np.random.normal(size=self.simulations)

        ST = S * np.exp((r - 0.5 * sigma**2)*T + sigma * np.sqrt(T) * Z)

        if option_type == "call":
            payoff = np.maximum(ST - K, 0)
        else:
            payoff = np.maximum(K - ST, 0)

        return np.exp(-r*T) * np.mean(payoff)