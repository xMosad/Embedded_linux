#include <stdio.h> 
#include <sys/types.h> 
#include <unistd.h> 
#include <stdlib.h> 
#include <errno.h> 
#include <sys/wait.h> 
#include<pthread.h>

//run gcc example20.c -lpthread -o ex20
void *thread (void *data)
{
	int i = 0;
	while(1)
	{
		printf("%i \n" , i);
		sleep(10);
		i++;
	}
}

int main(int argc, int **argv)
{		
	pthread_t mythread;
	pthread_create(&mythread, NULL,thread,NULL);
	while(1)
	{
		
	}
}