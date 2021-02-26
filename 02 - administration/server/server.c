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
#include <stdio.h> 
#include <sys/types.h> 
#include <unistd.h> 
#include <stdlib.h> 
#include <errno.h> 
#include <sys/wait.h> 


#define MAX 80 
#define PORT 8080  //shall be non-used port
#define NUM_CONNECTIONS_REQ 5
#define SA struct sockaddr 
//run this to view ports: sudo lsof -i -P -n | grep 192.168.1.3
// Function designed for chat between client and server. 

pthread_mutex_t fill_mutex;
int sockfd, connfd, len; 
struct sockaddr_in servaddr, cli; 
pthread_t mythread;

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
		dump_data(buff , 1);
		// send that buffer to client via socket
		write(connfd, buff, sizeof(buff));
	}
}

void *_rec() 
{ 	
	char buff[MAX]; 
	int n; 
	// infinite loop for chat 
	for (;;) {
		/*reading data */
		read(connfd, buff, sizeof(buff)); 
			printf("From client  ");
		printf("  : %s", buff); 
		dump_data(buff , 0);
	}
}  

void *thread2 ()
{
	sleep(3);
		// Now server is ready to listen and verification 
	//check that ethernet accepted binding
	// NUM_CONNECTIONS_REQ N connection requests
	if ((listen(sockfd, NUM_CONNECTIONS_REQ)) != 0) {
		printf("Listen failed...\n"); 
		exit(0); 
	}
	else
		printf("Server listening..\n"); 
	
	// Accept the data packet from client and verification 
	//waiting till client opens socket and connect to server
	/* In the call to accept(), the server is put to sleep and when for an incoming
	 * client request, the three way TCP handshake* is complete, the function accept()
	 * wakes up and returns the socket descriptor representing the client socket.
	 */
	connfd = accept(sockfd,NULL, NULL);
	if (connfd < 0) { 
		printf("server acccept failed...\n"); 
		exit(0); 
	} 
	else
		printf("server acccept the client...\n"); 
	
	// Function for chatting between client and server 
	//func(connfd); 
	pthread_cancel(mythread);
	pthread_t send  ;
	pthread_create(&send, NULL,_send,NULL);
	pthread_t rec ;
	pthread_create(&rec, NULL,_rec,NULL);
	// After chatting close the socket 
	close(sockfd);
}

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


// Driver function 
int main(void)
{ 

	//pthread_t mythread , time_st;
	
	
	pthread_create(&mythread, NULL,thread,NULL);
	
	pthread_t mythread2;
	pthread_create(&mythread2, NULL,thread2,NULL);
	
	// socket create and verification, socket is a channel between client and server
	//socket = IP+PORT
	//AF_INET For Internet family of IPv4 addresses
	//SOCK_STREAM for full duplex
	// 0 for TCP
	sockfd = socket(AF_INET, SOCK_STREAM, 0); //socketfd is a socket descriptor with int value, to bind with a port
	if (sockfd == -1) { 
		printf("socket creation failed...\n");
		exit(0); 
	} 
	else
		printf("Socket successfully created..\n");
	//Initializing serveraddr with zeros
	bzero(&servaddr, sizeof(servaddr)); 

	// assign IP, PORT 
	servaddr.sin_family = AF_INET; //For Internet family of IPv4 addresses
	servaddr.sin_addr.s_addr = inet_addr("192.168.1.15"); //define server IP statically
	servaddr.sin_port = htons(PORT); //define connection port that will be used for client and server

	//Binding newly created socket
	//binding is to attach socket to ethernet port
	if ((bind(sockfd, (SA*)&servaddr, sizeof(servaddr))) != 0) { 
		printf("socket bind failed...\n"); 
		exit(0); 
	} 
	else
		printf("Socket successfully binded..\n"); 
	



	while(1);

	

	
	return 0;
} 


void dump_data(char *_data ,char ch)
{
		FILE *fptr = NULL ;
		fptr = fopen("server_d.txt" , "a+");
		if (ch == 0) {
			fprintf(fptr,"client : %s" , _data);
		}
		else if (ch ==1)
		{
			fprintf(fptr,"server : %s" , _data);
		}
		fclose(fptr);
}

