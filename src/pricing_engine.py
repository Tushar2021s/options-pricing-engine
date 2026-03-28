# pricing_engine.py

class PricingEngine:
    """
    Central engine to price options using any model
    """

    def __init__(self, model):
        self.model = model

    def set_model(self, model):
        """
        Switch pricing model dynamically
        """
        self.model = model

    def price(self, S, K, T, r, sigma, option_type="call"):
        self._validate_inputs(S, K, T, sigma)
        return self.model.price(S, K, T, r, sigma, option_type)
    def batch_price(self, options):
        """
        options: list of dicts
        [
            {"S":100, "K":100, "T":1, "r":0.05, "sigma":0.2, "type":"call"},
            ...
        ]
        """
        results = []

        for opt in options:
            price = self.model.price(
                opt["S"],
                opt["K"],
                opt["T"],
                opt["r"],
                opt["sigma"],
                opt.get("type", "call")
            )
            results.append(price)

        return results
    
    def _validate_inputs(self, S, K, T, sigma):
        if S <= 0 or K <= 0:
            raise ValueError("S and K must be positive")
        if T <= 0:
            raise ValueError("Time to maturity must be > 0")
        if sigma <= 0:
            raise ValueError("Volatility must be > 0")
        
    def model_name(self):
        return self.model.__class__.__name__