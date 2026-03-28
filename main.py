from data.generate_data import generate_store_data
from models.demand_model import DemandForecaster
from models.queue_model import MM1Queue
from simulation.simulator import simulate_queue
from utils.metrics import summarize_queue

def main():
    df = generate_store_data()

    forecaster = DemandForecaster()
    forecaster.fit(df)

    predictions = forecaster.predict(days=14)
    print("Demand forecast:", predictions)

    lambda_est = df["customers"].mean()
    mu_est = df["service_rate"].mean()

    queue = MM1Queue(lambda_est, mu_est)
    print("Queue metrics:", queue.summary())

    queue_sim = simulate_queue(lambda_est, mu_est)
    metrics = summarize_queue(queue_sim)

    print("Simulation metrics:", metrics)

if __name__ == "__main__":
    main()
