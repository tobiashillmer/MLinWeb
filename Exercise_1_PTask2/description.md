# Comparison of Page Rank

Link to repo: https://github.com/tobiashillmer/MLinWeb

## Procedure

For the task I used the python networkx library.
First I created to equally sized graphs after the Erdösz/Renyi and the Barabasi/Albert graph models.
The number of nodes could be set to a value (here 10000) on both approaches. The expected number of edges has to be calculated from other parameters in both approaches.
The parameters of both generators were set so that both approaches generate a graph with approximately 100000 edges. For Erdösz/Renyi this means a probability of 1/500 and for Barabasi/Albert this means attachment to 10 nodes for each new node.

After the graphs were generated a pagerank-distribution for was calculated for each node in each approach. This pagerank-distribution was then visualized through a histogram and a kernel density estimator. Here the characteristic form of the poission-distribution for Erdösz/Renyi and the power-law distribution for Barabasi/Albert was visible.
Several characteristics were analyzed and are described in the following section.

## Results

In the following I will use ER short for Erdösz/Renyi and BA short for Barabasi/Albert.

The sum of all page ranks in both models  is 1.0.
Means are almost equal. This because both graphs have 10000 nodes and the page rank of 1.0 has to be distributed on these nodes.

Standard deviation of BA is significant higher. => The power law distribution is less centered to the mean.

Skewness of BA is significant higher. => The power law distribution is less symmetric.

The kurtosis of the BA distribution is multiple orders of magnitude higher. => The power law distribution is heavy tailed.

The maximum page rank of BA is significant higher. => The BA favours large hubs.
While the lower quantiles are similar in both solutions, the value of the higher quantile of BA is significant higher similar to the maximum page rank.

In BA the 10 percent nodes with the highest page_rank have 29% of the complete page rank