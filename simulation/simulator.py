import numpy as np

def simulate_queue(arrival_rate, service_rate, time_horizon=100):
    arrivals = np.random.poisson(arrival_rate, size=time_horizon)
    queue = 0
    queue_lengths = []

    for t in range(time_horizon):
        queue += arrivals[t]
        served = min(queue, int(service_rate))
        queue -= served
        queue_lengths.append(queue)

    return queue_lengths
