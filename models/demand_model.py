from models.poisson_model import PoissonDemandModel

class DemandForecaster:
    def __init__(self):
        self.models = {}

    def fit(self, df):
        grouped = df.groupby("day_of_week")["customers"]

        for day, values in grouped:
            model = PoissonDemandModel()
            model.fit(values)
            self.models[day] = model

    def predict(self, days=7):
        predictions = []

        for i in range(days):
            day = i % 7
            pred = self.models[day].sample()[0]
            predictions.append(pred)

        return predictions
