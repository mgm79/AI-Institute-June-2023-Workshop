from dataclasses import dataclass
from typing import List
from scipy.integrate import solve_ivp

@dataclass
class SEIRModel:
    beta: float
    gamma: float
    sigma: float
    mu: float
    initial_conditions: List[float]

    def _seir_ode(self, t, y):
        S, E, I, R = y
        N = S + E + I + R
        dSdt = self.mu * (N - S) - (self.beta * S * I) / N
        dEdt = (self.beta * S * I) / N - (self.sigma * E)
        dIdt = (self.sigma * E) - (self.gamma * I)
        dRdt = (self.gamma * I) - (self.mu * R)
        return [dSdt, dEdt, dIdt, dRdt]

    def simulate(self, t_span, t_eval):
        sol = solve_ivp(self._seir_ode, t_span, self.initial_conditions, t_eval=t_eval)
        return sol.y
