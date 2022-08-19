#include <stdio.h>

struct job
{
	int jobid;
	int deadline;
	float profit;
};

int main()
{
	int n, maxdeadline = 0;
	printf("Enter total no. of jobs: ");
	scanf("%d", &n);
	struct job jobs[n];
	for (int i = 0; i < n; i++)
	{
		jobs[i].jobid = i + 1;
		printf("\nFor Job%d: \n", jobs[i].jobid);
		printf("Enter deadline: ");
		scanf("%d", &jobs[i].deadline);
		if (jobs[i].deadline > maxdeadline)
		{
			maxdeadline = jobs[i].deadline;
		}
		printf("Enter profit: ");
		scanf("%f", &jobs[i].profit);
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n - i - 1; j++)
		{
			if (jobs[j].profit < jobs[j + 1].profit)
			{
				struct job temp = jobs[j];
				jobs[j] = jobs[j + 1];
				jobs[j + 1] = temp;
			}
		}
	}

	int jobTime[maxdeadline];
	for (int i = 0; i < maxdeadline; i++)
	{
		jobTime[i] = 0;
	}
	for (int i = 0; i < n; i++)
	{
		int deadline = jobs[i].deadline - 1;
		if (jobTime[deadline] == 0)
		{
			jobTime[deadline] = jobs[i].jobid;
		}
		else
		{
			while (deadline >= 0)
			{
				if (jobTime[deadline] == 0)
				{
					jobTime[deadline] = jobs[i].jobid;
					break;
				}
				deadline--;
			}
		}
	}
	printf("\nTime \tJobID\n");
	for (int i = 0; i < maxdeadline; i++)
	{
		printf(" %d \t", i + 1);
		if (jobTime[i] != 0)
		{
			printf("job%d\n", jobTime[i]);
		}
		else
		{
			printf("No job\n");
		}
	}
	// for(int i=0 ; i<n ; i++){
	// 	printf("%d %d %f\n",jobs[i].jobid,jobs[i].deadline,jobs[i].profit);
	// }

	return 0;
}
