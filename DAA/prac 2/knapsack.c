#include <stdio.h>

struct data{
    int id;
    int weight;
    float profit;
    float pbw;
    float used;
};

int main()
{
    int n,capacity;
    float profit=0;
    printf("Enter total no. of entries: ");
    scanf("%d",&n);
    struct data arr[n];
    struct data temp;
    for(int i=0 ; i<n ; i++){
        printf("Entry %d:\n",i+1);
        arr[i].id=i+1;
        printf("Enter weight: ");
        scanf("%d",&arr[i].weight);
        printf("Enter profit: ");
        scanf("%f",&arr[i].profit);
        arr[i].pbw = arr[i].profit/arr[i].weight ;
    }
    printf("\nEnter total capacity: ");
    scanf("%d",&capacity);
    
    
    for(int i=0 ; i<n ; i++){
        for(int j=0 ; j<n-i-1 ; j++){
            if(arr[j].pbw < arr[j+1].pbw){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1]= temp;
            }
        }
    }
    
    for(int i=0 ; i<n && capacity>=0 ; i++){
        for(int j=1 ; j<=arr[i].weight && capacity>0 ; j++){
            profit +=arr[i].pbw;
            capacity--;
            arr[i].used = (float)j/arr[i].weight ;
            // printf("capacity: %d\n",capacity);
            // printf("profit: %0.2f\n",profit);
        }
    }
    
    for(int i=0 ; i<n ; i++){
        for(int j=0 ; j<n-i-1 ; j++){
            if(arr[j].id >  arr[j+1].id){
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1]= temp;
            }
        }
    }
    printf("\nProfit: %0.2f\n\n",profit);
    printf("ID\tWeight\tProfitt\t\tProfit/Weight\tUsed\n");
    for(int i=0 ; i<n ; i++){
        printf("%d\t%d\t%f\t%f\t%0.2f\n",arr[i].id,arr[i].weight,arr[i].profit,arr[i].pbw,arr[i].used);
    }

    return 0;
}
