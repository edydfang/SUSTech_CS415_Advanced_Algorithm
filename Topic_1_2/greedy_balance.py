import numpy as np

def greedy_balance(machine_num, job_indices, job_time):
    assigns = [list() for i in range(machine_num)]
    accumulators = np.zeros(machine_num)
    for job_ind in range(len(job_indices)):
        min_ind = np.argmin(accumulators)
        
        assigns[min_ind].append(job_indices[job_ind])
        #print(assigns)
        accumulators[min_ind] += job_time[job_ind]
    makespan = max(accumulators)
    return (makespan,assigns,accumulators)