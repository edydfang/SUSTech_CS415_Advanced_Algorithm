#! /usr/bin/python3

from sorted_balance import sorted_blance
import numpy as np

def test():
    '''
    %   >> [makespan, assigns, accumulators] = greedy_balance(3, 7, 1 : 7, 1 : 7); % 12
%   >> [makespan, assigns, accumulators] = greedy_balance(3, 6, 1 : 6, [2 3 4 6 2 2]); % 8
%   >> [makespan, assigns, accumulators] = greedy_balance(4, 13, [2 : 13 1], [ones(1, 12) 4]); % 7 <= 2 * 4 (4 = opt)
%   >> [makespan, assigns, accumulators] = greedy_balance(3, 5, 1 : 5, [7 6 5 4 2]); % 9
%       vs. [makespan, assigns, accumulators] = greedy_balance(3, 5, 1 : 5, [2 7 6 5 4]); % 10
%   >> job_time = randi(RandStream('mt19937ar', 'Seed', 0), 1e3, 1, 1e3); % job_time(1 , [1 end]) == [815   867]
%   >> [makespan, assigns, accumulators] = greedy_balance(100, 1e3, 1 : 1e3, job_time); % 5481
    '''
    print(sorted_blance(3,np.arange(1,8), np.arange(1,8)))
    print(sorted_blance(3,np.arange(1,7), np.array([2,3,4,6,2,2])))
    print(sorted_blance(4,np.concatenate((np.arange(2,14),np.array([1])),axis=0), np.concatenate((np.ones(12,dtype=np.int8),np.array([4])),axis=0)))
    print(sorted_blance(3,np.arange(1,6), np.array([7,6,5,4,2])))

if __name__ == '__main__':
    test()