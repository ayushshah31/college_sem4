#include <stdio.h>

struct node
{
    char source;
    char destinaion;
    int weight;
    int isMST;
};

int main()
{
    int edgeNo, vertNo, MSTcount = 0;
    int costMST = 0;

    printf("\nEnter total no. of vertices: ");
    scanf("%d", &vertNo);
    char vertices[vertNo][2];
    printf("Enter vertices: ");
    for (int i = 0; i < vertNo; i++)
    {
        scanf(" %c", &vertices[i][0]);
        vertices[i][1] = '0';
    }

    printf("\nEnter total no. of edges: ");
    scanf("%d", &edgeNo);
    struct node graph[edgeNo];
    for (int i = 0; i < edgeNo; i++)
    {
        printf("Enter Source, Destination & weight: ");
        scanf(" %c %c %d", &graph[i].source, &graph[i].destinaion, &graph[i].weight);
        graph[i].isMST = 0;
    }

    // Sort graph according to weight
    for (int i = 0; i < edgeNo; i++)
    {
        for (int j = 0; j < edgeNo - i - 1; j++)
        {
            if (graph[j].weight > graph[j + 1].weight)
            {
                struct node temp = graph[j];
                graph[j] = graph[j + 1];
                graph[j + 1] = temp;
            }
        }
    }

    // Required Minimum Spanning Tree calc
    for (int j = 0; j < edgeNo; j++)
    {
        char source = graph[j].source;
        char destination = graph[j].destinaion;
        char verticeWithSource[vertNo];
        int vs = 0;
        char verticeWithDestination[vertNo];
        int vd = 0;
        char commonVertice[vertNo];
        int cm = 0;
        for (int i = 0; i < vertNo; i++)
        {
            verticeWithSource[i] = '-';
            verticeWithDestination[i] = '-';
            commonVertice[i] = '-';
        }
        for (int i = 0; i < vertNo && MSTcount != vertNo - 1; i++)
        {
            // Cyclic condition
            if ((vertices[i][0] == source || vertices[i][0] == destination) && vertices[i][1] == '0')
            {
                vertices[i][1] = '1';
                graph[j].isMST = 1;
                MSTcount++;
                // i++;
                printf("In if: source:%c dest:%c MSTcount:%d\n", source, destination, MSTcount);
                break;
            }
            // else if ((vertices[i][0] == source || vertices[i][0] == destination) && vertices[i][1] == '1')
            // {
            // 	for (int i = 0; i < edgeNo; i++)
            // 	{
            // 		if (graph[i].source == source)
            // 		{
            // 			verticeWithSource[vs] = graph[i].destinaion;
            // 			vs++;
            // 		}
            // 		else if (graph[i].destinaion == source)
            // 		{
            // 			verticeWithSource[vs] = graph[i].source;
            // 			vs++;
            // 		}
            // 	}
            // 	for (int i = 0; i < edgeNo; i++)
            // 	{
            // 		if (graph[i].destinaion == destination)
            // 		{
            // 			verticeWithDestination[vd] = graph[i].source;
            // 			vd++;
            // 		}
            // 		else if (graph[i].source == destination)
            // 		{
            // 			verticeWithDestination[vd] = graph[i].destinaion;
            // 			vd++;
            // 		}
            // 	}

            // 	for (int i = 0; i < vertNo; i++)
            // 	{
            // 		for (int k = 0; k < vertNo; k++)
            // 		{
            // 			if (verticeWithSource[i] == verticeWithDestination[k] && verticeWithDestination[k] != '-' && verticeWithSource[i] != '-')
            // 			{
            // 				commonVertice[cm] = verticeWithDestination[k];
            // 				cm++;
            // 			}
            // 		}
            // 	}
            // 	for (int i = 0; i < cm; i++)
            // 	{
            // 		int edge1 = 0, edge2 = 0;
            // 		for (int k = 0; k < edgeNo; k++)
            // 		{
            // 			if ((graph[k].source == source || graph[k].destinaion == source) && (graph[k].source == commonVertice[i] || graph[k].destinaion == commonVertice[i]))
            // 			{
            // 				edge1 = graph[k].isMST;
            // 			}
            // 			if ((graph[k].source == destination || graph[k].destinaion == destination) && (graph[k].source == commonVertice[i] || graph[k].destinaion == commonVertice[i]))
            // 			{
            // 				edge2 = graph[k].isMST;
            // 			}
            // 		}
            // 		if ((edge1 && !edge2) || (!edge1 && edge2) || (!edge1 && !edge2))
            // 		{
            // 			graph[j].isMST = 1;
            // 			printf("MSTcount before in else: %d\n", MSTcount);
            // 			MSTcount++;
            // 			printf("MSTcount after in else: %d\n", MSTcount);
            // 		}
            // 	}
            // }
        }
    }

    printf("\n\nMST:\n");
    for (int i = 0; i < edgeNo; i++)
    {
        if (graph[i].isMST == 1)
        {
            printf("%c -->> %c = %d \n", graph[i].source, graph[i].destinaion, graph[i].weight);
            costMST += graph[i].weight;
        }
    }
    printf("\n\nCost of MST: %d \n\n", costMST);
    return 0;
}

// Enter total no. of vertices: 5
// Enter vertices: a b c d e
// Enter total no. of edges: 7
// Enter Source, Destination & weight: 0 1 5
// Enter Source, Destination & weight: 0 2 15
// Enter Source, Destination & weight: 0 3 10
// Enter Source, Destination & weight: 1 3 25
// Enter Source, Destination & weight: 1 4 30
// Enter Source, Destination & weight: 3 2 20
// Enter Source, Destination & weight: 3 4 35

// MST:
// a -->> b = 5
// a -->> d = 10
// a -->> c = 15
// b -->> e = 30

// Cost of SMT: 60%

// Enter total no. of vertices: 5
// Enter vertices: 1 2 3 4 5

// Enter total no. of edges: 7
// Enter Source, Destination & weight: 0 1 1
// Enter Source, Destination & weight: 0 2 7
// Enter Source, Destination & weight: 0 3 10
// Enter Source, Destination & weight: 0 4 5
// Enter Source, Destination & weight: 1 2 3
// Enter Source, Destination & weight: 2 3 4
// Enter Source, Destination & weight: 3 4 2

// MST:
// 1 -->> 2 = 1
// 4 -->> 5 = 2
// 2 -->> 3 = 3

// Cost of MST: 6