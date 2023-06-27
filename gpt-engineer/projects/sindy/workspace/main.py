from seir_model import SEIRModel
from data_generator import DataGenerator
from plotter import Plotter
from pysindy import PySINDy

# Define SEIR model parameters
beta = 0.2
gamma = 0.1
sigma = 0.1
mu = 0.01
initial_conditions = [990, 10, 0, 0]

# Create SEIR model object
seir_model = SEIRModel(beta, gamma, sigma, mu, initial_conditions)

# Generate SEIR data
data_generator = DataGenerator(seir_model)
data = data_generator.generate_data()

# Plot SEIR data
plotter = Plotter(data)
plotter.plot_data()

# Perform SINDy on SEIR data
pysindy = PySINDy()
pysindy.fit(data)
pysindy.print()
