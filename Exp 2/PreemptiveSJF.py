class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turnaround_time = 0

def srtf_scheduling(processes):
    current_time = 0
    completed = 0
    n = len(processes)
    while completed != n:
        # Find process with shortest remaining time that has arrived
        ongoing_process = None
        for process in processes:
            if process.arrival_time <= current_time and process.remaining_time > 0:
                if ongoing_process is None or process.remaining_time < ongoing_process.remaining_time:
                    ongoing_process = process
        
        if ongoing_process is None:
            # If no process has arrived yet, just increment time
            current_time += 1
            continue
        
        # Process the selected process for 1 time unit
        ongoing_process.remaining_time -= 1
        current_time += 1

        # If process is completed, calculate its completion, turnaround, and waiting time
        if ongoing_process.remaining_time == 0:
            ongoing_process.completion_time = current_time
            ongoing_process.turnaround_time = ongoing_process.completion_time - ongoing_process.arrival_time
            ongoing_process.waiting_time = ongoing_process.turnaround_time - ongoing_process.burst_time
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
    
    srtf_scheduling(processes)
    print_process_table(processes)

if __name__ == "__main__":
    main()
