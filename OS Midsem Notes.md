# OS Midsem Notes
**Booting**
---
- **Booting** is a mechanism in the system that loads the operating system from the secondary storage into the main memory, or RAM, of the system.
- Also known as starting of computer

**Types of Booting**
1. **Cold or Hard Booting:** 
- A state in which a computer is switched on from being switched off is referred to as cold booting.
- In this procedure, the system undergoes a complete power-on self-test (POST) that initializes hardwares and loads operating systems from a storage medium into random-access memory (RAM).

2. **Soft or Warm Booting**
- restarts, reboots a computer system without shutting it down entirely.
- skip some of the hardware initialization processes that are done on cold booting since the hardware components have been on power and have been initialized earlier.
- Warm Booting is required when systems give no response,hang state or behave abnormally.

- **Firmware** is a type of software that's embedded in a device's hardware to help it function. It's often called "software for hardware".Firmware is specific to a particular device, while software is more versatile and can be used across a variety of devices

- **BIOS (basic input/output system)** is the program/firmware a computer's microprocessor that uses to start the computer system after it is powered on.
- BIOS has several components:POST, Bootstrap Loader, Drivers(interfaces between OS and hardware),CMOS Setup(Configuration program that allows users to configure hardware settings )
- BIOS perform POST to check if all the necessary hardwares are connected before starting the computers system.

- **BIOS initialization** is the process that occurs when a computer is first turned on and the BIOS (Basic Input/Output System) takes control of the system.Hence,BIOS is the first software that runs in computer.
- UEFI is more preferable than BIOS nowadays(To be discussed later)

- **POST(Power on self test):** Self diagnostic test/is a set of diagnostic tests that a computer runs after it's turned on to check that all its components are working properly.

- The **bootstrap** program is the first code that runs when a computer starts, and it's responsible for loading the OS into memory. Typically stored in ROM or EPROM.
- Bootstrap program is loaded in memory by **Bootstrap Loader** in BIOS.

- Computer system can be divided into four components(Refer university notes)

**Kernel**
- The **kernel** is a core component/heart of an operating system and serves as the main interface between the computer's physical hardware and the processes running on it.
- The OS is sometimes known as kernel.
- It acts as a bridge between software applications and the hardware of a computer.
-  It basically manages operations of memory and CPU time.
- [Types of kernel](https://www.geeksforgeeks.org/kernel-in-operating-system/)
    - **Monolithic kernel:** The entire operating system runs as a single program in Kernel mode.The user services and kernel services are implemented in the same address space
    - **Micro kernel:** Here user services are kept inside the user address space and kernel services are kept under the kernel address space.
- [Monolithic kernel versus micro kernel](https://www.geeksforgeeks.org/difference-between-microkernel-and-monolithic-kernel/)
- **Modularity** is the concept of breaking down a system into separate components or modules, each with a specific function that operates independently.

- A **lightweight** application is an application consuming less process cycle, to achieve the same results as a conventional application. Lightweight applications are designed to be small, portable, self-contained, and easy to fix. 

**Types of operating system, according to architecture**
- Single processor
- Multiprocessor

**Use of multiprocessor over single processor**
- **Modularity:** Uses modules for each category of task. Tasks belonging to same category are parallel processed.
- **Computation speed up:** Multiprocessor has higher throughput and speed than uniprocessor, since it distributes tasks among multiple processors.
- **Reliability/Fault Tolerant:** In multiprocessor systems, if one processor fails, others can take over its tasks, improving system reliability and reducing the risk of complete system failure.
- **Safety:** Multiprocessor systems enhance safety by allowing critical tasks to be run redundantly on different processors, ensuring consistent and accurate operation even in the event of a fault.
- **Information Sharing:** Multiple processors can share memory and resources, allowing them to easily exchange information and collaborate on complex tasks, improving efficiency and coordination in workloads.

**Types of multiprocessing**
1. **Asymmetric multiprocessing**
- Asymmetric Multiprocessing (AMP) is a multiprocessing structure where in one processor called the master processor controls the other subordinate processors also known as the slave processors.
- tasks scheduling is done by the master processor of the system.
2. **Symmetric multiprocessing**
- Symmetric multiprocessing (SMP) is a multiprocessors system where multiple processors are installed and have an equal access to the system and memory resources of the system.
- Every processor works individually, while doing its work and communicating with the operating system.
- [Difference between assymetric and symmetric multiprocessing](https://www.geeksforgeeks.org/difference-between-asymmetric-and-symmetric-multiprocessing/)
    - Definition
    - Easiness to design
    - Cost
    - Scheduling done
    - Communication
    - Example
- In computer architecture, and especially in Multiprocessors systems, memory access models play a critical role that determines performance, scalability, and generally, efficiency of the system.
- **Shared memory architecture** is a system where multiple process communicate by reading from and writing to a shared memory pool.
- The two shared-memory models most frequently used are UMA and NUMA:

**UMA(Uniform memory access)**
-  Here all the processes have equal access time.
- All processors have equal access to memory, with no portion of memory being closer to any one processor.
- bandwidth is restricted or limited rather than non-uniform memory access. Hence slower than NUMA.
- Bandwidth refers to maximum capacity of data that can be transferred.

**NUMA(Non Uniform memory access)**
- Here all the processes have different access time.
- Processors can have access local memory faster than remote memory.

**UMA vs NUMA**
- Definition
- Bandwidth
- Speed
- Example

**Loosely coupled vs tightly coupled system**
|Loosely coupled|Tightly coupled system|
|--|--|
|1.Here we have individual bus, cabinet and peripheral devices for different processors|1.Here we have single bus,cabinet and set of peripheral devices for different processors|
|2.There is distributed memory in loosely coupled multiprocessor system.|2.There is shared memory, in tightly coupled multiprocessor system.|
|3.Loosely Coupled Multiprocessor System has low data rate.|3.Tightly coupled multiprocessor system has high data rate.|
|4.The cost of loosely coupled multiprocessor system is less.|4.Tightly coupled multiprocessor system is more costly.|
|5.Applications of loosely coupled multiprocessor are in distributed computing systems.|5.Applications of tightly coupled multiprocessor are in parallel processing systems.|
|6.In loosely coupled multiprocessor, Memory conflicts don’t take place.|6.While tightly coupled multiprocessor system have memory conflicts.|
- In loosely coupled multiprocessor system, modules are connected through MTS (Message transfer system) network.

**Other types of operating system**
---
1. **Batch Operating System**
- This type of operating system does not interact with the computer directly.
- There is an operator which takes similar jobs having the same requirements and groups them into batches.

<img src="Images/Screenshot 2024-09-30 113014.png" width="" height="">

**Pros:**
- The idle time for the batch system is very less.
- Multiple users can share the batch systems.
- It is easy to manage large work repeatedly in batch systems.

**Cons:**
- hard to debug.
- It is sometimes costly.
- The other jobs will have to wait for an unknown time if any job fails.
- In batch operating system the processing time for jobs is commonly difficult to accurately predict while they are in the queue.

**Examples of Batch Operating Systems:** Payroll Systems, Bank Statements, etc.

2. **Multi-Programming Operating System**
- Multiprogramming Operating Systems can be simply illustrated as more than one program/jobs is present in the main memory and any one of them can be kept in execution.
- Since, in general, main memory is too small to
accommodate all jobs, the jobs are kept initially on the disk in the **job pool**.
This pool consists of all processes residing on disk awaiting allocation of main
memory
- The set of jobs in memory can be a subset of the jobs kept in the job
pool.
- The OS picks a job from main memory and executes it till completion.Other jobs in the have to wait for one job to complete.
- Hence, though multiprogramming ensures no cpu idleness but lacks responsivenes. 
- These are tightly coupled

<img src="Images/Screenshot 2024-09-30 114441.png" width="" height="">

**Pros:**
- Increases throughput
- focus on reducing idleness

**Cons:**
- Not concerned about responsiveness

3. **Multitasking / Timesharing system**
- In Multitasking Operating System is the cpu executes multiple jobs/tasks by switching among them.
- It switches so frequently that the users
can interact with each program while it is running.Hence improves reponsiveness along reducing cpu idleness.
- It generally uses round robin algorithm to switch between tasks.

<img src="Images/Screenshot 2024-09-30 115613.png" width="" height="">

- [Multiprogramming vs multitasking systems](https://www.geeksforgeeks.org/difference-between-multiprogramming-and-multitasking/)
    - Definition
    - Concepts used
    - Focus
    - Time consumption
    - Scheduling Algorithms

4. **Distributed systems**
- These are loosely coupled systems.
- Various autonomous interconnected computers communicate with each other using a shared communication network.
- Independent systems possess their own memory unit and CPU. 

<img src="Images/Screenshot 2024-09-30 120457.png" width="" height="">

5. **Embedded systems**
- It is a system with a specific set of hardware, and it is designed to perform a specific functionality.
- All real time systems are embedded but vice versa is not true.

6. **Real time systems**
- These are operating system which are used to perform real time tasks.
- **Real time task:** A task, which is associated with time.
- It is of three types:
    1. **Hard real time:**
    - Here deadline is mandatory otherwise disastrous event will happen.
    - if a deadline is missed, the system will fail.

    Eg;Flight controller systems

    2. **Soft real time:**
    - Here deadline is desirable.
    - Missing the deadline doesn't cause disastrous event but it decreases the usefulness of output.
    - the system continues to function even if a deadline is missed, but with lower quality output.

    Eg, Live screening, Video calling
    
    3. **Firm real time:**
    - A firm is stricter than soft realtime, where a small number of missed deadlines can be tolerated.

    Eg,Online trading system,Online auction system,Online reservation system
- **Physical Time:** It refers to the quantitative time that is being measured by clock.
- **Logical Time:** It refers to the qualitative time with respect to sequence of events occurred before.

- [User mode vs kernel mode](https://www.geeksforgeeks.org/difference-between-user-mode-and-kernel-mode/)
    - Access to Resources
    - Level of privilege

**System Calls**
---
- It basically changes from user mode to kernel mode.
- It provides an interface to the services made available by operating system/kernel.
- These calls are available as routines, mostly written in C/C++
- In Unix Systems there are many system call functions which can be directly used in code whereas in other operating systems we need APIs.

<img src="Images/Screenshot 2024-09-30 124455.png" width="" height="">
-  For most programming languages, the run-time support system (a set of
 functions built into libraries included with a compiler) provides a system
call interface that serves as the link to system calls made available by the
 operating system. 
 -  The system-call interface intercepts function calls in the API
 and invokes the necessary system calls within the operating system. 
 - Typically,
 a number is associated with each system call, and the system-call interface
 maintains a table indexed according to these numbers.
 - The system call interface  then invokes the intended system call in the operating-system kernel and
 returns the status of the system call and any return values.
 - 


- There are five types of system call based on the services they provide:
1. **Process control**
- It is responsible for creating,managing and terminating processes.
- fork(): Creates a child process
- exit():Normal termination
- abort() and kill:Forceful termination
- wait():Blocks the calling/parent process until child process terminates
2. **File manipulation**
- It is responsible for manipulating files such as opening, reading and writing.
- open(): Initialises access to a file in system
- read():Read data from a file into a buffer
- write():Write data from a buffer declared by the user to a given device.
- close():Closes a file descriptor by the kernel
3. **Device manipulation**
- It is responsible for managing devices such as requesting releasing, attaching and detaching devices.
- ioctl():Controls a device by setting device dependent request code
- read(): used to read data from a file, device, socket, or pipe into a buffer.
- write()
4. **Information maintenance**
- It is responsible for managing and transferring information between Operating system and computer programmes.
- getpid():getting process id of current process
- getppid():getting process id of parent process
- alarm():used to send a SIGALRM signal to a process after a specified number of seconds have elapsed
- sleep():sets the process to wait until the specified amount of time proceeds
- wait() is used for inter-thread communication and synchronization, often in scenarios where one thread needs to wait for a specific condition before proceeding. sleep() is used to introduce a pause or delay in the execution of the current thread, regardless of other threads
5. **Communication**
- It is responsible for communicating between processes such as sending or receiving messages and creating and deleting communication connections.
- pipe():Creates a pipe that allows communication between a process and its child process
- shm open()
- mmap()
6. **Protection**
- Used to access privileged operations that are not available to normal user programmes.
- Operating system uses this privilege to protect the system from malicious and unauthorised users.
- chmod():Changes the permissions and modes of files and directories.
- chown():Change the ownership of a file or directory
- umask()

<img src="Images/Screenshot 2024-09-30 140906.png" width="" height="">

**Process**
---
- program in its execution stage is called a **process**

**Process States**
1. **New:** The process is being created
2. **Running:** Instructions are being executed.
3. **Waiting:** The process is waiting for some event to occur (such as an I/O
completion or reception of a signal).
4. **Ready:** The process is waiting to be assigned to a processor.
5. **Terminated:** The process has finished execution.

**Process control block (PCB)**

- **Process state:** Contains information about a state of a process.The state may be new, ready, running, waiting, halted, and
so on
- **Program counter:** The counter indicates the address of the next instruction
to be executed for this process.
- **CPU registers:** They include accumulators, index registers,
stack pointers, and general-purpose registers. Along with the program counter, this state information must
be saved when an interrupt occurs, to allow the process to be continued
correctly afterward .
- **CPU-scheduling information:** This information includes a process priority,
CPU scheuelling algorithm used and any other scheduling parameters.
- **Accounting information:** This information includes the amount of CPU
and real time used, time limits, account numbers, job or process numbers,
and so on.
- **I/O status information:** This information includes the list of I/O devices
allocated to the process, a list of open files, and so on

<img src="Images/Screenshot 2024-09-30 145659.png" width="" height="">

**Transition diagram**

<img src="Images/Screenshot 2024-09-30 145908.png" width="" height="">

1. **New**:  
   - A process is just created and is waiting to be admitted into the system.

2. **Admitted → Ready**:  
   - The process is now ready to be executed by the CPU, but it is waiting for the CPU to be free.

3. **Scheduler Dispatch → Running**:  
   - When the CPU is available, the process is dispatched (assigned) to run on the CPU.

4. **Running → Interrupt → Ready**:  
   - If the process is interrupted (for example, by an urgent task or another process), it stops running and goes back to the ready state, waiting for its next turn.

5. **Running → I/O or Event Wait → Waiting**:  
   - If the process needs input/output (I/O) operations or is waiting for an event (like user input), it moves to the waiting state.

6. **Waiting → I/O or Event Completion → Ready**:  
   - Once the I/O operation or the event completes, the process goes back to the ready state to wait for the CPU again.

7. **Running → Exit → Terminated**:  
   - After the process finishes its execution, it moves to the terminated state, meaning it is completed and done.

- **Schedulers:** Select a process from the ready queue.
- **Dispatchers:** Assigns a process to the operating system.

**Waiting vs Interrupt**
|Waiting|Interrupt|
|--|--|
|Puts the CPU in an idle state until a specific event occurs.|Temporarily halts the CPU's current process to handle an urgent task.|
|It is I/O bound and required for the process|It is not required for the process, but it is forced|

**Context switching**
- It is a situation where the current process has to stay idle when more important task is assigned is called **context switching**.
- It involves the following steps:
1. Saving the state of current task
2. Loading the state of new task to execute

<img src="Images/Screenshot 2024-09-30 152220.png" width="" height="">

**Process Scheduling Queues**
- These are data structures in an operating system that store processes at different stages of execution, such as ready, waiting, or blocked, allowing the system to manage and prioritize process execution efficiently.
- They are of different types:
1. **Job queue :** set of all processes in the system 
2. **Ready queue:** set of all processes residing in main memory, ready and waiting 
to execute
3. **Device queues:** set of processes waiting for an I/O device
- Processes migrate among the various queues as you can see in the diagram below.

<img src="Images/Screenshot 2024-09-30 153019.png" width="" height="">

**Schedulers**
- **Schedulers:** Select a process from the ready queue.
- Refer your notebook

- Operation on a process are of two types:**Process creation** and **process termination**

**Process creation**
- Parent process create children processes, which, in turn create other processes, forming a tree of processes
- Generally, process identified and managed via a **process identifier (pid)**.
- The **init** process (which always
has a pid of 1) serves as the root parent process for all user processes.
- Once the
system has booted, the init process can also create various user processes, such
as a web or print server, an ssh server, and the like.
- **Resource sharing:** child process will
need certain resources (CPU time, memory, files, I/O devices) to accomplish
its task. A child process may be able to obtain its resources directly from
the operating system, or it may be constrained to a subset of the resources
of the parent process.
- Restricting a child process to a subset of
the parent’s resources prevents any process from overloading the system by
creating too many child processes. 
-  **Execution:** 
    - Parent and children execute concurrently
    - Parent waits until children terminate
- exec() system call is used to replace the program that a process is executing with a new program. 
- There are also two address-space possibilities for the new process:
1. The child process is a duplicate of the parent process (it has the same
program and data as the parent).
2. The child process has a new program loaded into it.

<img src="Images/Screenshot 2024-09-30 155011.png" width="" height="">

**Process Termination**
- A process terminates when it finishes executing its final statement and asks the
operating system to delete it by using the exit() system call.
- At that point, the
process may return a status value (typically an integer) to its parent process
- All the resources of the process — including
physical and virtual memory, open files, and I/O buffers — are deallocated
by the operating system.
- **Cascading termination:** It is a phenomenon where termination of parent process leads to termination of all its child processes.It is a forceful termination.

**Inter process communication**
--- 
- Processes executing concurrently in the operating system may be either
independent processes or cooperating processes.
- **Cooperating processes:** A process which can affect or get affected by other processes are known as cooperating processes
- **Independent processes** a process which cannot affect or affected by other processes is called independent processes.

<img src="Images/Screenshot 2024-09-30 160603.png" width="" height="">

- IPC is a mechanism through which cooperating processes can communicate with each other.

- There are two
fundamental models of interprocess communication: **shared memory** and **message passing**.

**Shared-Memory Model**
- Communication in shared memory model has the following components:
1. **Producer process:** produces information
2. **Consumer process** consumes information
3. **Buffer:** Temporary memory space where information is stored temporarily
- Bufferng is of 3 types: Zero,bounded,unbounded(Refer notebook)
- In case of zero buffering both producer and consumer are dependent on each other at each instance of time.
- The code for accessing and manipulating the shared
memory be written explicitly by the application programmer.

**Message-Passing Systems**
- Message passing provides a mechanism to allow processes to communicate
and to synchronize their actions without sharing the same address space.
- It is
particularly useful in a distributed environment, where the communicating
processes may reside on different computers connected by a network.
- For
example, an Internet chat program could be designed so that chat participants
communicate with one another by exchanging messages.

**Naming**
- Processes that want to communicate must have a way to refer to each other.
They can use either direct or indirect communication.

**Buffering**
- Whether communication is direct or indirect, messages exchanged by communicating processes reside in a temporary queue. 

**Thread**
---
- a thread is a basic unit of execution that's a sequence of programmed instructions that can be managed independently. 

**Process vs Thread**
|Process|Thread|
|-|-|
|Process means any program is in execution.|Thread means a segment of a process.|
|Heavyweight task|Lightweight task|
|If one process is blocked, then it will not affect the execution of other processes.|If a user-level thread is blocked, then all other user-level threads are blocked.|
|A system call is involved in it.|No system call is involved, it is created using APIs.|
|The process does not share data with each other.|Threads share data with each other.|

**User thread vs kernel thread**
|User thread|kernel thread|
|-|-|
|User threads are managed by user-level thread libraries like POSIX threads (Pthreads) and not directly by the OS kernel.|Kernel threads are created, managed, and scheduled directly by the operating system’s kernel.|
|Faster Context Switching,since user threads do not require kernel mode switching|Slower Context Switching,Switching between kernel threads involves the kernel|
|If one user thread makes a blocking system call (like I/O), the entire process is blocked because the kernel doesn't distinguish between user threads.|A blocking system call made by one kernel thread does not block the entire process, as other threads can continue execution.|

**Multi threading models**
- Refer to assignment





















- Users of os
    - OS is a resource allocator
    - OS is a control program
- bootstrap program is loaded at power-up or reboot
    - Typically stored in ROM or EPROM, generally known as firmware
    - Initializes all aspects of system
    - Loads operating system kernel and starts execution
- An **interrupt** is a signal that temporarily stops a computer's processor from running its current program, allowing other devices or processes to access the processor.
- A trap is a software-generated interrupt caused either by an error or a user 
request
- **Types of interrupt**
    - **polling:** A polled interrupt is a type of software interrupt that involves a computer regularly checking if its connected devices need attention. In a polled interrupt, the computer does not wait for devices to signal that they need help, but instead asks them directly. 
    - **vectored interrupt system:** A vectored interrupt is an interrupt that uses an interrupt vector, which is a predefined address in memory where the specific interrupt service routine (ISR) for that interrupt is located.
- An operating system is **interrupt driven** 
- The operating system preserves the state of the CPU by storing registers and the 
program counter 
- Determines which type of interrupt has occurred




