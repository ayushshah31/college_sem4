#include <stdio.h>

typedef struct Data
{
    int id;
    int profit;
    int weight;
    float pbw;
    float sol;
} Sack;

void sort(Sack item[], int no, int order)
{
    for (int i = 0; i < no; i++)
    {
        for (int j = 0; j < no - i - 1; j++)
        {
            if (order == 1)
            {
                if (item[j].pbw < item[j + 1].pbw)
                {
                    Sack temp = item[j + 1];
                    item[j + 1] = item[j];
                    item[j] = temp;
                }
            }
            else
            {
                if (item[j].id < item[j + 1].id)
                {
                    Sack temp = item[j + 1];
                    item[j + 1] = item[j];
                    item[j] = temp;
                }
            }
        }
    }
}

// here we received the sorted array. Now we fill sack one by one
int fillSack(Sack item[], int capacity, int n)
{
    float profit = 0;
    for (int i = 0; i < n && capacity >= 0; i++)
    {
        for (int j = 1; j <= item[i].weight && capacity > 0; j++)
        {
            profit += item[i].pbw;
            capacity--;
            item[i].sol = (float)j / item[i].weight;
        }
    }
    return profit;
}

int main()
{
    int n, capacity;
    float profit = 0;
    printf("Enter total no. of items: ");
    scanf("%d", &n);
    printf("Enter capacity of Sack: ");
    scanf("%d", &capacity);

    Sack item[n];

    for (int i = 0; i < n; i++)
    {
        printf("\nItem %d", i + 1);
        item[i].id = i;
        item[i].sol = 0;
        printf("\nEnter Profit: ");
        scanf("%d", &item[i].profit);
        printf("Enter Weight: ");
        scanf("%d", &item[i].weight);
        item[i].pbw = (float)item[i].profit / item[i].weight;
    }

    // 1 is when sorting according to pbw
    sort(item, n, 1);
    profit = fillSack(item, capacity, n);
    printf("\nTotal profit: %d", profit);

    // 0 is when sorting acc to id
    sort(item, n, 0);
    printf("\nSolution Vector: ");
    for (int i = 0; i < n; i++)
    {
        printf(" %f ", item[i].sol);
    }

    // printf("\nID Pro Wgt Pbw Sol");
    // for (int i = 0; i < n; i++)
    // {
    //     printf("\n%d %d %d %f %d", item[i].id, item[i].profit, item[i].weight, item[i].pbw, item[i].sol);
    // }

    return 0;
}