#include <stdio.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

sem_t mutex, write_block;
int data = 0, reader_count = 0;

void* reader(void* arg) {
    int id = *((int*)arg);
    sem_wait(&mutex);
    reader_count++;
    if (reader_count == 1) {
        sem_wait(&write_block); // First reader locks the writer
    }
    sem_post(&mutex);

    printf("Reader %d: read data = %d\n", id, data);
    sleep(1);

    sem_wait(&mutex);
    reader_count--;
    if (reader_count == 0) {
        sem_post(&write_block); // Last reader unlocks the writer
    }
    sem_post(&mutex);
    
    return NULL;
}

void* writer(void* arg) {
    int id = *((int*)arg);
    sem_wait(&write_block); // Writer locks the resource
    data++;
    printf("Writer %d: wrote data = %d\n", id, data);
    sleep(1);
    sem_post(&write_block); // Unlocks the resource
    return NULL;
}

int main() {
    pthread_t readers[5], writers[2];
    sem_init(&mutex, 0, 1);
    sem_init(&write_block, 0, 1);
    
    int reader_ids[5] = {1, 2, 3, 4, 5};
    int writer_ids[2] = {1, 2};

    // Create writer threads
    for (int i = 0; i < 2; i++) {
        pthread_create(&writers[i], NULL, writer, &writer_ids[i]);
    }

    // Create reader threads
    for (int i = 0; i < 5; i++) {
        pthread_create(&readers[i], NULL, reader, &reader_ids[i]);
    }

    // Wait for writers
    for (int i = 0; i < 2; i++) {
        pthread_join(writers[i], NULL);
    }

    // Wait for readers
    for (int i = 0; i < 5; i++) {
        pthread_join(readers[i], NULL);
    }

    sem_destroy(&mutex);
    sem_destroy(&write_block);

    return 0;
}
