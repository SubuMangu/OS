class Process:
    def __init__(self, pid, arrival_time, burst_time, priority):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def priority_scheduling(processes):
    current_time = 0
    completed = 0
    n = len(processes)
    
    while completed != n:
        # Find the highest priority process that has arrived and is not yet completed
        highest_priority_process = None
        for process in processes:
            if process.arrival_time <= current_time and process.completion_time == 0:
                if highest_priority_process is None or process.priority < highest_priority_process.priority:
                    highest_priority_process = process

        if highest_priority_process is None:
            current_time += 1
            continue

        # Complete the selected process
        current_time += highest_priority_process.burst_time
        highest_priority_process.completion_time = current_time
        highest_priority_process.turnaround_time = highest_priority_process.completion_time - highest_priority_process.arrival_time
        highest_priority_process.waiting_time = highest_priority_process.turnaround_time - highest_priority_process.burst_time
        completed += 1

def print_process_table(processes):
    print("PID\tAT\tBT\tPriority\tCT\tTAT\tWT")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.priority}\t\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

def main():
    # Define list of processes with their PID, Arrival Time, Burst Time, and Priority
    processes = [
        Process(1, 0, 7, 2),
        Process(2, 2, 4, 1),
        Process(3, 4, 1, 3),
        Process(4, 5, 4, 2),
    ]
    
    priority_scheduling(processes)
    print_process_table(processes)

if __name__ == "__main__":
    main()
