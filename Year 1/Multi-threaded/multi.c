/*
DUE: Feburary 3rd 2023 11:59pm
Name: Cameron Skerritt
- - - - - - - - - - - - - - - -
This is a multithreaded program which calculates values from a list of numbers.
Thread 1 determines the average number.
Thread 2 determines the minimum number.
Thread 3 determines the maximum number.

- - - - - - / additional notes \ - - - - - -
We use ATOI to convert args to a integer. 
Additionally we skip the first argument of args as its the name of the file. 
*/

#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

 
// Holds final results
int avgNum;
int minNum;
int maxNum;
 
// Functions' declaration. Definition is at the bottom.
void *avgfunc(void *param);
void *minfunc(void *param);
void *maxfunc(void *param);

/* Array that holds all values used in all functions. Set length to 10 as input is always 10 integers from tests. */
int Array[]={};
int main(int argc, char* argv[])
{
    /* Checks to see if input is less than 2 */
    if (argc < 2){
        printf("= = = = REQUIRES 2 ARGS TO RUN = = = =");
        exit(-1);
    }
   

    /* Gives each thread an ID */
    pthread_t avg, min, max;

    /* Creates a detached thread */
    pthread_attr_t tattr;

    /* initalizes thread attributes */
    pthread_attr_init(&tattr); 

    /* Creates three threads for Average, minimum and maximum functions. */
    pthread_create(&avg,&tattr,*avgfunc,(void*)argv);
    pthread_create(&min,&tattr,*minfunc,(void*)argv);
    pthread_create(&max,&tattr,*maxfunc,(void*)argv); 

    /* Threads exit */
    pthread_join(avg,NULL);
    pthread_join(min,NULL);
    pthread_join(max,NULL);

    printf("%d %d %d", avgNum, minNum, maxNum); /* Prints final results. */
}

/* Finds the average value */
void *avgfunc(void *param)
{
    char** args = (char**) param;   // args is a pointer to array of pointers to main func arguments argv
    args++;             // increment the pointer to point to the first number passed
    int count = 0; /* Used to calculate amount of numbers in args */
    int total = 0; /* Stores all numbers */
    
    while (*args != NULL){ /* loops through args until args is NULL. Reference for end of user input. */
         total = total +atoi(*args); /* converts args to in and stores it into total. */
         args++; /* Increments args by 1 */
         count++; /* Incremenets count by 1 */
    }
    
    avgNum = total / count; /* Calculates average by using total amount divided by length of args */
    pthread_exit(0);
}

 /* Finds the min value */
void *minfunc(void *param)
{
    char** args = (char**) param;   // args is a pointer to array of pointers to main func arguments argv
    args++;                        // increment the pointer to point to the first number passed

    minNum = atoi(*args);/* Uses first argument number*/
    
     while (*args != NULL){ /* loops through args until args is NULL. Reference for end of user input. */
         if ( atoi(*args) < minNum){ /* Converts args to int, compares current args number against stored number. If less than stored number: */
            minNum = atoi(*args);/* Sets new result to minNum*/
         }
    *args++; /* Increments args by 1. */
    }
    pthread_exit(0); 
}

/* Finds the max value */
void *maxfunc(void *param)
{
    char** args = (char**) param;   // args is a pointer to array of pointers to main func arguments argv
    args++;                        // increment the pointer to point to the first number passed

    maxNum = atoi(*args);/* Uses first argument number*/

     while (*args != NULL){ /* loops through args until args is NULL. Reference for end of user input. */
         if (atoi(*args) > maxNum) { /* Converts to int, checks if current args number is greater than stored number */
         /* Sets new result to maxNum */
         maxNum = atoi(*args);
         }
    args++;/* Increments args by 1 */
    }
    pthread_exit(0);
}
