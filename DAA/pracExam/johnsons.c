#include <stdio.h>

int queueAns[100];
int front = 0;
int rear;
void pushFront(int i)
{
    queueAns[front] = i;
    front++;
}

void pushRear(int i)
{
    rear--;
    queueAns[rear] = i;
}

int main()
{

    int machines, jobs;
    printf("Enter total no. of machines: ");
    scanf("%d", &machines);
    printf("Enter total no. of jobs: ");
    scanf("%d", &jobs);

    int john[machines][jobs];
    int temp[machines][jobs];

    for (int i = 0; i < machines; i++)
    {
        printf("Enter jobs for Machine %d: ", i + 1);
        for (int j = 0; j < jobs; j++)
        {
            scanf("%d", &john[i][j]);
            temp[i][j] = john[i][j];
        }
    }

    for (int i = 0; i < machines; i++)
    {
        printf("Machine %d: ", i + 1);
        for (int j = 0; j < jobs; j++)
        {
            printf("%d \t", john[i][j]);
        }
        printf("\n");
    }

    rear = jobs;
    int i, j, minJ, machine, min;
    for (int k = 0; k < jobs; k++)
    {
        min = 99999;
        for (i = 0; i < 2; i++)
        {
            for (j = 0; j < jobs; j++)
            {
                if (min > john[i][j])
                {
                    min = john[i][j];
                    minJ = j;
                    machine = i;
                }
            }
        }

        john[0][minJ] = john[1][minJ] = 99999;
        if (machine == 0)
        {
            pushFront(minJ);
        }
        else
        {
            pushRear(minJ);
        }
    }

    printf("Solution: ");
    for (int i = 0; i < jobs; i++)
    {
        printf("Job%d \t", queueAns[i] + 1);
    }

    int timeM1 = 0;
    int m1[jobs][2];
    for (int i = 0; i < jobs; i++)
    {
        m1[queueAns[i]][0] = timeM1;
        timeM1 += temp[0][queueAns[i]];
        m1[queueAns[i]][1] = timeM1;
    }

    printf("\n\nMachine 1:\n");
    for (int i = 0; i < jobs; i++)
    {
        printf("Job%d  %d - %d\n", i + 1, m1[i][0], m1[i][1]);
    }

    int timeM2 = temp[0][queueAns[0]];
    int m2[jobs][2];
    for (int i = 0; i < jobs; i++)
    {
        m2[queueAns[i]][0] = timeM2;
        timeM2 += temp[1][queueAns[i]];
        m2[queueAns[i]][1] = timeM2;
    }

    printf("\n\nMachine 2:\n");
    for (int i = 0; i < jobs; i++)
    {
        printf("Job%d  %d - %d\n", i + 1, m2[i][0], m2[i][1]);
    }

    return 0;
}