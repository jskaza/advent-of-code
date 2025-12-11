import re
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

def solve(target, buttons):
    """
    Solve as Integer Linear Programming problem.
    Minimize: sum of button presses
    Subject to: A @ x = target, x >= 0, x integer
    """
    n_counters = len(target)
    n_buttons = len(buttons)
    
    # Build coefficient matrix A where A[i][j] = 1 if button j increments counter i
    A = np.zeros((n_counters, n_buttons), dtype=float)
    for j, button in enumerate(buttons):
        for counter_idx in button:
            A[counter_idx][j] = 1.0
    
    # Objective: minimize sum of button presses (all coefficients are 1)
    c = np.ones(n_buttons)
    
    # Constraints: A @ x = target
    constraints = LinearConstraint(A, lb=target, ub=target)
    
    # Bounds: x >= 0
    bounds = Bounds(lb=0, ub=np.inf)
    
    # Solve integer linear program
    result = milp(c=c, constraints=constraints, bounds=bounds, integrality=np.ones(n_buttons))
    
    if result.success:
        return int(round(result.fun))
    else:
        return -1

# Main
with open("input.txt", "r") as f:
    lines = f.read().splitlines()

total = 0
for i, line in enumerate(lines, 1):
    buttons_str = line.split("]")[1].split("{")[0]
    buttons = [tuple(int(x) for x in re.findall(r'\d+', button)) 
               for button in re.findall(r'\([^)]+\)', buttons_str)]
    joltage = [int(x) for x in line.split("{")[1].split("}")[0].split(",")]
    
    total += solve(joltage, buttons)


print(total)