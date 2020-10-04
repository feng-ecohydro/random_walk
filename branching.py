import numpy as np
import matplotlib.pyplot as plt

def rw_single_outcome(start, numsteps, p_forward, p_back):
    if numsteps == 0:   # with 0 steps remaining, stop
        return start
    if start <= 0:      # if already over the clip, then cannot step back 
        return start
    else:
        # randomly sample one step based on given probability
        step = np.random.choice([-1,1], p=[p_forward, p_back]) 
        # recursively take each step until the number of remaining steps go to 0
        return rw_single_outcome(start+step, numsteps-1, p_forward, p_back)
    
def simulate_rw(x0, n_steps, n_iterations, p_forward, p_back): 
    final_pos = np.zeros(n_iterations)
    for i in range(n_iterations): 
        final_pos[i] = rw_single_outcome(x0, n_steps, p_forward, p_back)
    return final_pos


pf = 1/3    # probability toward the cliff
pb = 2/3    # probability away from the cliff
x0 = 10     # how far away from the cliff we start with 

n_iterations = 10000            # number of iterations used to construct histogram
N_list = [15, 30, 50, 100]      # the total number of steps taken in each "trial"

for N in N_list:   
    print(N)
    final_pos = simulate_rw(x0, N, n_iterations, pf, pb)    
    plt.hist(final_pos,  bins=range(-10, 80))
plt.xlabel('Final positions')
plt.ylabel('# of iterations')
