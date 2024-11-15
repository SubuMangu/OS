#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define N 5 // Number of philosophers

sem_t forks[N];  // Semaphores for forks
pthread_t philosophers[N];  // Threads for philosophers

void* philosopher(void* num) {
    int id = *(int*)num;

    while (1) {
        // Thinking
        printf("Philosopher %d is thinking\n", id);
        sleep(1);

        // Picking up forks (left fork first, then right fork)
        printf("Philosopher %d is hungry\n", id);
        sem_wait(&forks[id]);  // Pick up left fork
        sem_wait(&forks[(id + 1) % N]);  // Pick up right fork

        // Eating
        printf("Philosopher %d is eating\n", id);
        sleep(2);

        // Putting down forks
        sem_post(&forks[id]);  // Put down left fork
        sem_post(&forks[(id + 1) % N]);  // Put down right fork
    }
    return NULL;
}

int main() {
    int ids[N];

    // Initialize semaphores for forks
    for (int i = 0; i < N; i++) {
        sem_init(&forks[i], 0, 1);
    }

    // Create philosopher threads
    for (int i = 0; i < N; i++) {
        ids[i] = i;
        pthread_create(&philosophers[i], NULL, philosopher, &ids[i]);
    }

    // Wait for philosopher threads to finish
    for (int i = 0; i < N; i++) {
        pthread_join(philosophers[i], NULL);
    }

    // Destroy semaphores
    for (int i = 0; i < N; i++) {
        sem_destroy(&forks[i]);
    }

    return 0;
}
