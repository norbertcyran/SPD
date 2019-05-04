import os

import numpy as np

from lab4.scheduler import (Job, schrage_algorithm, compute_makespan,
                            schrage_pmtn)

if __name__ == '__main__':
    for path in os.listdir('data'):
        job_data = np.loadtxt(f'data/{path}', dtype=int, skiprows=1)
        jobs = [Job(job_id, *times) for job_id, times in enumerate(job_data, 1)]
        perm = schrage_algorithm(jobs)
        makespan = compute_makespan(perm)
        print(f'Perm for {path}: {[job.id for job in perm]}')
        print(f'Makespan for {path}: {makespan}')
        print(f'Makespan for pmtn: {schrage_pmtn(jobs)}')
