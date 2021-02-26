#include <stdio.h>
#include <netdb.h> 
#include <netinet/in.h>
#include <stdlib.h> 
#include <string.h> 
#include <sys/socket.h> 
#include <sys/types.h>
#include<pthread.h>
#include <unistd.h>
#include <arpa/inet.h>
#define MAX 80 
#define PORT 8080 
#define SA struct sockaddr 

int sockfd, connfd; 
pthread_mutex_t fill_mutex;

void dump_data(char *_data ,char ch);

void *_send() 
{ 	
	char buff[MAX]; 
	int n; 
	// infinite loop for chat 
	for (;;) 
	{ 

		//cleaning buffer before sending...
		bzero(buff, sizeof(buff)); 
		n = 0;
		//getting input from used till endline
		while ((buff[n++] = getchar()) != '\n') ; 
		dump_data(buff , 0);
		
		// send that buffer to client via socket
		write(sockfd, buff, sizeof(buff));

	}
}

void *_rec() 
{ 	
	char buff[MAX]; 
	int n; 
	// infinite loop for chat 
	for (;;) {
		/*reading data */
		
	
		read(sockfd, buff, sizeof(buff)); 
		printf("From Server :");
		printf(" %s", buff); 
		dump_data(buff , 1);
		if ((strncmp(buff, "exit", 4)) == 0) 
		{ 
			printf("Client Exit...\n"); 
			break;
			exit(0);
		} 
	}
}  


int main(void)
{ 
	
	struct sockaddr_in servaddr, cli; 

	// socket create and verification
	sockfd = socket(AF_INET, SOCK_STREAM, 0); 
	if (sockfd == -1) { 
		printf("socket creation failed...\n"); 
		exit(0); 
	} 
	else
		printf("Socket successfully created..\n"); 

	bzero(&servaddr, sizeof(servaddr)); 

	// assign IP, PORT 
	servaddr.sin_family = AF_INET; 
	servaddr.sin_addr.s_addr = inet_addr("127.0.0.1"); 
	servaddr.sin_port = htons(PORT); 

	// connect the client socket to server socket 
	if (connect(sockfd, (SA*)&servaddr, sizeof(servaddr)) != 0) { 
		printf("connection with the server failed...\n"); 
		exit(0); 
	} 
	else
		printf("connected to the server..\n"); 

	// function for chat 
	pthread_t send  ;
	pthread_create(&send, NULL,_send,NULL);
	pthread_t rec ;
	pthread_create(&rec, NULL,_rec,NULL);
	
	while(1);

	// close the socket 
	close(sockfd); 
	return 0;
} 

void dump_data(char *_data ,char ch)
{
		FILE *fptr = NULL ;
		fptr = fopen("client_d.txt" , "a+");
		if (ch == 0) {
			fprintf(fptr,"client : %s " , _data);
		}
		else if (ch ==1)
		{
			fprintf(fptr,"server : %s " , _data);
		}
		fclose(fptr);
}

