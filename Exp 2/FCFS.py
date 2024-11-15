class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def fcfs_scheduling(processes):
    # Sort the processes first by arrival time, then by PID (or order) in case of a tie
    processes.sort(key=lambda x: (x.arrival_time, x.pid))
    
    current_time = 0
    for process in processes:
        # If the CPU is idle, jump to the arrival time of the process
        if current_time < process.arrival_time:
            current_time = process.arrival_time
        
        # Completion time = current time + burst time
        process.completion_time = current_time + process.burst_time
        process.turnaround_time = process.completion_time - process.arrival_time
        process.waiting_time = process.turnaround_time - process.burst_time
        
        # Update the current time to the completion time of the current process
        current_time = process.completion_time

def print_process_table(processes):
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

def main():
    # Define list of processes with their PID, Arrival Time, and Burst Time
    processes = [
        Process(1, 0, 5),
        Process(2, 2, 3),
        Process(3, 2, 4),
        Process(4, 0, 2),
    ]
    
    fcfs_scheduling(processes)
    print_process_table(processes)

if __name__ == "__main__":
    main()
