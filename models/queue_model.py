class MM1Queue:
    def __init__(self, arrival_rate, service_rate):
        self.lambda_ = arrival_rate
        self.mu = service_rate

        if self.lambda_ >= self.mu:
            raise ValueError("System unstable: λ >= μ")

    def utilization(self):
        return self.lambda_ / self.mu

    def expected_customers(self):
        rho = self.utilization()
        return rho / (1 - rho)

    def expected_time(self):
        return 1 / (self.mu - self.lambda_)

    def summary(self):
        return {
            "rho": self.utilization(),
            "L": self.expected_customers(),
            "W": self.expected_time()
        }
