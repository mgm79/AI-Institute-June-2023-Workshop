from pysindy import SINDy

class PySINDy:
    def __init__(self):
        self.sindy = SINDy()

    def fit(self, data):
        self.sindy.fit(data.T)

    def print(self):
        self.sindy.print()
