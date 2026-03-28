# pricing_model.py

from abc import ABC, abstractmethod

class PricingModel(ABC):
    """
    Abstract base class for all pricing models
    """

    @abstractmethod
    def price(self, S, K, T, r, sigma, option_type="call"):
        pass