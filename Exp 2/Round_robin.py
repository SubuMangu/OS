class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def round_robin_scheduling(processes, quantum):
    current_time = 0
    completed = 0
    n = len(processes)
    queue = []
    
    # Add processes to the queue in order of arrival time
    for process in processes:
        queue.append(process)
    
    while completed != n:
        for process in list(queue):  # Iterate over a copy of the queue
            if process.remaining_time > 0:
                if process.remaining_time > quantum:
                    current_time += quantum
                    process.remaining_time -= quantum
                else:
                    current_time += process.remaining_time
                    process.remaining_time = 0
                    process.completion_time = current_time
                    process.turnaround_time = process.completion_time - process.arrival_time
                    process.waiting_time = process.turnaround_time - process.burst_time
                    completed += 1
                
                # If process is still not done, rotate it back to the queue
                if process.remaining_time > 0:
                    queue.append(process)
            
            # Remove the processed item from the queue
            queue.remove(process)

def print_process_table(processes):
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t{process.burst_time}\t{process.completion_time}\t{process.turnaround_time}\t{process.waiting_time}")

def main():
    # Define list of processes with their PID, Arrival Time, and Burst Time
    processes = [
        Process(1, 0, 10),
        Process(2, 1, 5),
        Process(3, 2, 8),
    ]
    
    # Define time quantum
    quantum = 3
    
    round_robin_scheduling(processes, quantum)
    print_process_table(processes)

if __name__ == "__main__":
    main()
