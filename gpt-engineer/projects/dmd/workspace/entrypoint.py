import numpy as np
import matplotlib.pyplot as plt
from pydmd import DMD
from dataclasses import dataclass

@dataclass
class SEIRParams:
    beta: float
    gamma: float
    sigma: float
    N: int
    I0: int
    R0: int
    T: int

class SEIRDataGenerator:
    def __init__(self, params: SEIRParams):
        self.params = params

    def generate_data(self):
        beta, gamma, sigma, N, I0, R0, T = self.params.beta, self.params.gamma, self.params.sigma, self.params.N, self.params.I0, self.params.R0, self.params.T
        S0 = N - I0 - R0
        S, E, I, R = [S0], [0], [I0], [R0]
        for _ in range(T):
            next_S = S[-1] - (beta * S[-1] * I[-1]) / N
            next_E = E[-1] + (beta * S[-1] * I[-1]) / N - sigma * E[-1]
            next_I = I[-1] + sigma * E[-1] - gamma * I[-1]
            next_R = R[-1] + gamma * I[-1]
            S.append(next_S)
            E.append(next_E)
            I.append(next_I)
            R.append(next_R)
        return np.array([S, E, I, R]).T

class DMDExperiment:
    def __init__(self, data: np.ndarray):
        self.data = data

    def run_experiment(self):
        dmd = DMD(svd_rank=-1)
        dmd.fit(self.data.T)
        modes = dmd.modes.T
        return modes

def plot_SEIR_model(data: np.ndarray):
    plt.plot(data[:, 0], label='Susceptible')
    plt.plot(data[:, 1], label='Exposed')
    plt.plot(data[:, 2], label='Infected')
    plt.plot(data[:, 3], label='Recovered')
    plt.legend()
    plt.title('SEIR Model')
    plt.xlabel('Time')
    plt.ylabel('Number of Individuals')
    plt.savefig('SEIR_model.png')
    plt.show()

def plot_DMD_modes(modes: np.ndarray):
    for i in range(modes.shape[1]):
        plt.plot(modes[:, i], label=f'Mode {i+1}')
    plt.legend()
    plt.title('DMD Modes')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.savefig('DMD_modes.png')
    plt.show()

if __name__ == '__main__':
    params = SEIRParams(beta=0.5, gamma=0.1, sigma=0.2, N=1000, I0=1, R0=0, T=100)
    data_generator = SEIRDataGenerator(params)
    data = data_generator.generate_data()
    dmd_experiment = DMDExperiment(data)
    modes = dmd_experiment.run_experiment()
    plot_SEIR_model(data)
    plot_DMD_modes(modes)
