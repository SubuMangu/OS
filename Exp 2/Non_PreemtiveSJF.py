class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def sjf_scheduling(processes):
    # Sort processes by arrival time first, and then by burst time
    processes.sort(key=lambda x: (x.arrival_time, x.burst_time))
    current_time = 0
    completed = 0
    n = len(processes)
    
    while completed != n:
        # Find the process with the shortest burst time that has arrived and is not yet completed
        shortest_job = None
        for process in processes:
            if process.arrival_time <= current_time and process.completion_time == 0:
                if shortest_job is None or process.burst_time < shortest_job.burst_time:
                    shortest_job = process

        if shortest_job is None:
            # If no process has arrived yet, increment time
            current_time += 1
            continue

        # Complete the shortest job
        current_time += shortest_job.burst_time
        shortest_job.completion_time = current_time
        shortest_job.turnaround_time = shortest_job.completion_time - shortest_job.arrival_time
        shortest_job.waiting_time = shortest_job.turnaround_time - shortest_job.burst_time
        completed += 1

def print_process_table(processes):
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

def main():
    # Define list of processes with their PID, Arrival Time, and Burst Time
    processes = [
        Process(1, 0, 8),
        Process(2, 1, 4),
        Process(3, 2, 9),
        Process(4, 3, 5),
    ]
    
    sjf_scheduling(processes)
    print_process_table(processes)

if __name__ == "__main__":
    main()
