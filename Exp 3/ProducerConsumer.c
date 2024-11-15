#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5

int buffer[BUFFER_SIZE];  // Shared buffer
int in = 0, out = 0;      // Buffer index for producer and consumer

sem_t empty;  // Semaphore to track empty slots
sem_t full;   // Semaphore to track full slots
pthread_mutex_t mutex;  // Mutex to ensure mutual exclusion

void *producer(void *arg) {
    int item;
    for (int i = 0; i < 10; i++) {
        item = i;  // Produce an item
        sem_wait(&empty);  // Wait for empty slot
        pthread_mutex_lock(&mutex);  // Lock the buffer
        
        // Critical section
        buffer[in] = item;
        printf("Producer produced: %d\n", item);
        in = (in + 1) % BUFFER_SIZE;
        
        pthread_mutex_unlock(&mutex);  // Unlock the buffer
        sem_post(&full);  // Signal that buffer has a full slot
        
        sleep(1);  // Simulate production time
    }
    return NULL;
}

void *consumer(void *arg) {
    int item;
    for (int i = 0; i < 10; i++) {
        sem_wait(&full);  // Wait for full slot
        pthread_mutex_lock(&mutex);  // Lock the buffer
        
        // Critical section
        item = buffer[out];
        printf("Consumer consumed: %d\n", item);
        out = (out + 1) % BUFFER_SIZE;
        
        pthread_mutex_unlock(&mutex);  // Unlock the buffer
        sem_post(&empty);  // Signal that buffer has an empty slot
        
        sleep(1);  // Simulate consumption time
    }
    return NULL;
}

int main() {
    pthread_t prod_thread, cons_thread;

    // Initialize the semaphores
    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);
    pthread_mutex_init(&mutex, NULL);

    // Create producer and consumer threads
    pthread_create(&prod_thread, NULL, producer, NULL);
    pthread_create(&cons_thread, NULL, consumer, NULL);

    // Wait for both threads to complete
    pthread_join(prod_thread, NULL);
    pthread_join(cons_thread, NULL);

    // Cleanup
    sem_destroy(&empty);
    sem_destroy(&full);
    pthread_mutex_destroy(&mutex);

    return 0;
}
