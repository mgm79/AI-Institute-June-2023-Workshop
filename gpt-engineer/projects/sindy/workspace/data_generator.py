class DataGenerator:
    def __init__(self, seir_model):
        self.seir_model = seir_model

    def generate_data(self):
        t_span = [0, 100]
        t_eval = range(100)
        data = self.seir_model.simulate(t_span, t_eval)
        return data
