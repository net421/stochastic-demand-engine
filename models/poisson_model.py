import numpy as np
from scipy.stats import poisson

class PoissonDemandModel:
    def __init__(self):
        self.lambda_ = None

    def fit(self, data):
        self.lambda_ = data.mean()

    def probability(self, k):
        return poisson.pmf(k, self.lambda_)

    def sample(self, size=1):
        return np.random.poisson(self.lambda_, size=size)

    def expected(self, t=1):
        return self.lambda_ * t
