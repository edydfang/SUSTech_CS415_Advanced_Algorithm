import numpy as np
from greedy_balance import greedy_balance

def sorted_blance(machine_num, job_indices, job_time):
    ascend_idx = np.argsort(job_time)
    job_indices = job_indices[ascend_idx[::-1]]
    job_time = job_time[ascend_idx[::-1]]
    return greedy_balance(machine_num, job_indices, job_time)