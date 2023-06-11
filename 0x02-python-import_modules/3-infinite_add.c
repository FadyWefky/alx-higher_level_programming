#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    long sum = 0;
    int i = 0;

    if(argc == 1)
    {
        printf("%d\n", 0);
    }
    else
    {
        for(i = 1 ; argv[i] != NULL ; i++)
        {
            sum = sum + atoi(argv[i]);
        }
        printf("%ld\n", sum);
    }
    return (0);
}