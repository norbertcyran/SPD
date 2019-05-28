import os
import random
import time
from copy import deepcopy

import numpy as np
import matplotlib.pyplot as plt

from lab4.job import Job

from lab4.scheduler import solve_rpq


def generate_jobs(count):
    for i in range(count):
        yield Job(i + 1, *(random.randint(0, 2000) for _ in range(3)))


def plot_schrage():
    schrage_times = []
    schrage_heap_times = []
    sizes = [10, 100, 250, 500, 1000, 2500, 5000, 10000]
    for i in sizes:
        jobs = list(generate_jobs(i))
        start_time = time.time()
        schrage_algorithm(jobs)
        schrage_times.append(time.time() - start_time)
        start_time = time.time()
        schrage_heaps(jobs)
        schrage_heap_times.append(time.time() - start_time)
    plt.plot(sizes, schrage_times, 'r-', label='Normal Schrage')
    plt.plot(sizes, schrage_heap_times, 'b-', label='Schrage on heaps')
    plt.xlabel('Dataset size')
    plt.ylabel('Execution time')
    plt.legend(loc='upper left')
    plt.show()


def plot_schrage_pmtn():
    schrage_times = []
    schrage_heap_times = []
    sizes = [10, 100, 250, 500, 1000]
    for i in sizes:
        jobs = list(generate_jobs(i))
        jobs_copy = deepcopy(jobs)
        start_time = time.time()
        schrage_pmtn(jobs_copy)
        schrage_times.append(time.time() - start_time)
        jobs_copy = deepcopy(jobs)
        start_time = time.time()
        schrage_pmtn_heaps(jobs_copy)
        schrage_heap_times.append(time.time() - start_time)
    plt.plot(sizes, schrage_times, 'r-', label='Normal Schrage pmtn')
    plt.plot(sizes, schrage_heap_times, 'b-', label='Schrage pmtn on heaps')
    plt.xlabel('Dataset size')
    plt.ylabel('Execution time')
    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    for path in os.listdir('data'):
        job_data = np.loadtxt(f'data/{path}', dtype=int, skiprows=1)
        jobs = [Job(job_id, *times) for job_id, times in enumerate(job_data)]
        makespan = solve_rpq(jobs)
        print(makespan)
        # if path == 'in002.txt' or path == 'in007.txt':
        #     continue
        # print(f'Perm for {path} (using heaps): {[job.id for job in perm]}')
        # print(f'Makespan for {path} (using heaps): {makespan}')
        # carlier_sched = Carlier(jobs)
        # perm = carlier_sched.schedule()
        # makespan = compute_makespan(perm)
        # print(f'Perm for {path} (carlier): {[job.id for job in perm]}')
        # print(f'Makespan for {path} (carlier): {makespan}')
        # print(f'Tree extensions: {carlier_sched.nodes}')
