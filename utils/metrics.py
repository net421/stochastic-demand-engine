import numpy as np

def summarize_queue(queue_lengths):
    return {
        "avg_queue": np.mean(queue_lengths),
        "max_queue": np.max(queue_lengths),
        "std_queue": np.std(queue_lengths)
    }
