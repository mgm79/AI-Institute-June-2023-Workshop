import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, data):
        self.data = data

    def plot_data(self):
        fig, ax = plt.subplots()
        ax.plot(self.data[0], label='S')
        ax.plot(self.data[1], label='E')
        ax.plot(self.data[2], label='I')
        ax.plot(self.data[3], label='R')
        ax.set_xlabel('Time')
        ax.set_ylabel('Population')
        ax.legend()
        plt.show()
