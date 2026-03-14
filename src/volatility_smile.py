import numpy as np
import matplotlib.pyplot as plt
from black_scholes import BlackScholes


class VolatilitySmile:

    @staticmethod
    def plot():

        S = 100
        r = 0.05
        T = 1
        sigma = 0.2

        strikes = np.linspace(70,130,50)

        prices = []

        for K in strikes:
            price = BlackScholes.call_price(S,K,T,r,sigma)
            prices.append(price)

        plt.plot(strikes, prices)

        plt.xlabel("Strike Price")
        plt.ylabel("Call Option Price")
        plt.title("Option Price vs Strike")

        plt.show()