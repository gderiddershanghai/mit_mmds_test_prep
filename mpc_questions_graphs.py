newman_networks_c6_mcq1 = {
    'question': "Which of the following is a key characteristic of a simple network or simple graph?",
    'options_list': [
        'It can have self-loops.',
        'It can have multiedges.',
        'It has no self-loops and no multiedges.',
        'It is always directed.'
    ],
    'correct_answer': 'It has no self-loops and no multiedges.',
    'explanation': "A simple network or simple graph is defined as having no self-loops and no multiedges, distinguishing it from more complex graph structures.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_mcq2 = {
    'question': "How is the degree of a vertex in a network defined?",
    'options_list': [
        'The number of vertices connected to it.',
        'The number of edges connected to it.',
        'The sum of weights of edges connected to it.',
        'The number of paths passing through it.'
    ],
    'correct_answer': 'The number of edges connected to it.',
    'explanation': "The degree of a vertex is defined as the number of edges connected to it, indicating its connectivity within the network.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_mcq3 = {
    'question': "In a directed network, what is the in-degree of a vertex?",
    'options_list': [
        'The number of edges it points to.',
        'The number of edges pointing to it.',
        'The total number of vertices in the network.',
        'The number of paths originating from it.'
    ],
    'correct_answer': 'The number of edges pointing to it.',
    'explanation': "In directed networks, the in-degree of a vertex is the number of incoming edges pointing to that vertex.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_mcq4 = {
    'question': "What does the adjacency matrix element Aij represent in a simple graph?",
    'options_list': [
        'The presence of a vertex i.',
        'The presence of an edge between vertex i and j.',
        'The degree of vertex i.',
        'The sum of all edges in the graph.'
    ],
    'correct_answer': 'The presence of an edge between vertex i and j.',
    'explanation': "In a simple graph, the adjacency matrix element Aij equals 1 if there is an edge between vertices i and j, and 0 otherwise.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_mcq5 = {
    'question': "Which theorem states that any planar graph can be colored with no more than four colors?",
    'options_list': [
        'Kuratowski’s Theorem',
        'Four-Color Theorem',
        'Menger’s Theorem',
        'Euler’s Theorem'
    ],
    'correct_answer': 'Four-Color Theorem',
    'explanation': "The Four-Color Theorem states that any planar graph can be colored with no more than four colors such that no two adjacent vertices share the same color.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_mcq6 = {
    'question': "What is the significance of the graph Laplacian in network analysis?",
    'options_list': [
        'It measures the total number of edges.',
        'It helps in studying network dynamics and spectral clustering.',
        'It identifies the shortest path between vertices.',
        'It represents the total degree of the network.'
    ],
    'correct_answer': 'It helps in studying network dynamics and spectral clustering.',
    'explanation': "The graph Laplacian is crucial in network analysis for studying dynamics, diffusion processes, and spectral clustering, providing insights into the network's structure.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_mcq7 = {
    'question': "What is a bipartite network?",
    'options_list': [
        'A network with edges that can have weights.',
        'A network where vertices are divided into two distinct sets with edges only connecting vertices from different sets.',
        'A network that can be colored with four colors.',
        'A network with directed edges.'
    ],
    'correct_answer': 'A network where vertices are divided into two distinct sets with edges only connecting vertices from different sets.',
    'explanation': "A bipartite network consists of two distinct types of vertices with edges only connecting vertices from different sets, often represented by an incidence matrix.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_mcq8 = {
    'question': "What is the connectivity of a pair of vertices?",
    'options_list': [
        'The total number of vertices in the network.',
        'The number of paths passing through both vertices.',
        'The minimum number of vertices or edges that need to be removed to disconnect the vertices.',
        'The total degree of both vertices.'
    ],
    'correct_answer': 'The minimum number of vertices or edges that need to be removed to disconnect the vertices.',
    'explanation': "The connectivity of a pair of vertices is the minimum number of vertices or edges that need to be removed to disconnect the vertices, indicating the network's robustness.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_mcq9 = {
    'question': "How can a bipartite network be projected onto a one-mode network?",
    'options_list': [
        'By ignoring the edge weights.',
        'By creating edges between vertices of the same type that share a common neighbor.',
        'By converting all edges to undirected edges.',
        'By combining the adjacency matrices.'
    ],
    'correct_answer': 'By creating edges between vertices of the same type that share a common neighbor.',
    'explanation': "A bipartite network can be projected onto a one-mode network by creating edges between vertices of the same type that share a common neighbor in the original bipartite network.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_mcq10 = {
    'question': "What is a geodesic path in a network?",
    'options_list': [
        'A path that visits every vertex exactly once.',
        'A path that visits every edge exactly once.',
        'The shortest path between two vertices.',
        'The longest path in the network.'
    ],
    'correct_answer': 'The shortest path between two vertices.',
    'explanation': "A geodesic path is the shortest path between two vertices, distinguishing it from other types of paths in a network.",
    'chapter_information': "Newman Networks Chapter 6"
}
###############################

newman_networks_c7_mcq1 = {
    'question': "What does betweenness centrality measure in a network?",
    'options_list': [
        'The number of edges connected to a vertex.',
        'The shortest path between two vertices.',
        'The extent to which a vertex lies on paths between other vertices.',
        'The average distance from a vertex to all other vertices.'
    ],
    'correct_answer': 'The extent to which a vertex lies on paths between other vertices.',
    'explanation': "Betweenness centrality measures the extent to which a vertex lies on the shortest paths between other vertices, indicating its role in facilitating communication within the network.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq2 = {
    'question': "Why is betweenness centrality important in social networks?",
    'options_list': [
        'It identifies vertices with the most direct connections.',
        'It highlights vertices that control the flow of information.',
        'It measures the total number of vertices in the network.',
        'It calculates the average path length between all pairs of vertices.'
    ],
    'correct_answer': 'It highlights vertices that control the flow of information.',
    'explanation': "Betweenness centrality is important because it highlights vertices that act as bridges in the network, controlling the flow of information between different parts of the network.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq3 = {
    'question': "In a directed network, how does the calculation of betweenness centrality differ from an undirected network?",
    'options_list': [
        'It does not consider the direction of edges.',
        'It only considers paths in one direction.',
        'It considers the direction of edges when calculating shortest paths.',
        'It ignores vertices with out-degree zero.'
    ],
    'correct_answer': 'It considers the direction of edges when calculating shortest paths.',
    'explanation': "In directed networks, betweenness centrality takes into account the direction of edges, meaning the shortest path from vertex u to vertex v can differ from the path from v to u.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq4 = {
    'question': "Which centrality measure is described as the number of edges connected to a vertex?",
    'options_list': [
        'Betweenness centrality',
        'Closeness centrality',
        'Degree centrality',
        'Eigenvector centrality'
    ],
    'correct_answer': 'Degree centrality',
    'explanation': "Degree centrality measures the number of edges directly connected to a vertex, indicating its immediate connections within the network.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq5 = {
    'question': "What is a potential drawback of using betweenness centrality in large networks?",
    'options_list': [
        'It only identifies the vertex with the highest degree.',
        'It requires significant computational resources.',
        'It does not account for edge direction.',
        'It assumes that all paths are of equal length.'
    ],
    'correct_answer': 'It requires significant computational resources.',
    'explanation': "Betweenness centrality can be computationally intensive to calculate, especially in large networks, because it requires consideration of all shortest paths between vertex pairs.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq6 = {
    'question': "How can the removal of a vertex with high betweenness centrality affect a network?",
    'options_list': [
        'It can reduce the total number of edges in the network.',
        'It can significantly disrupt communication between other vertices.',
        'It can increase the degree centrality of other vertices.',
        'It can reduce the network\'s average degree.'
    ],
    'correct_answer': 'It can significantly disrupt communication between other vertices.',
    'explanation': "Removing a vertex with high betweenness centrality can disrupt the shortest paths and communication between other vertices, potentially fragmenting the network.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq7 = {
    'question': "What is the relationship between betweenness centrality and information flow in a network?",
    'options_list': [
        'Vertices with high betweenness centrality block information flow.',
        'Vertices with high betweenness centrality facilitate information flow.',
        'Betweenness centrality does not affect information flow.',
        'Vertices with high betweenness centrality only influence their immediate neighbors.'
    ],
    'correct_answer': 'Vertices with high betweenness centrality facilitate information flow.',
    'explanation': "Vertices with high betweenness centrality facilitate information flow by acting as intermediaries on the shortest paths between other vertices.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq8 = {
    'question': "What is an advantage of normalizing betweenness centrality values?",
    'options_list': [
        'It makes all centrality measures equal.',
        'It allows comparison between vertices in different networks.',
        'It simplifies the calculation process.',
        'It increases the betweenness centrality value.'
    ],
    'correct_answer': 'It allows comparison between vertices in different networks.',
    'explanation': "Normalizing betweenness centrality values allows for comparison between vertices in different networks or of different sizes, providing a standardized measure.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq9 = {
    'question': "Which algorithm is commonly used for efficiently calculating betweenness centrality in large networks?",
    'options_list': [
        'Dijkstra\'s algorithm',
        'Brandes\' algorithm',
        'Kruskal\'s algorithm',
        'Prim\'s algorithm'
    ],
    'correct_answer': 'Brandes\' algorithm',
    'explanation': "Brandes' algorithm is commonly used for efficiently calculating betweenness centrality in large networks by combining breadth-first search (for unweighted graphs) or Dijkstra's algorithm (for weighted graphs).",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq10 = {
    'question': "In the context of betweenness centrality, what does the notation σst(i) represent?",
    'options_list': [
        'The total number of shortest paths in the network.',
        'The number of shortest paths from vertex s to vertex t.',
        'The number of shortest paths from vertex s to vertex t that pass through vertex i.',
        'The total number of vertices in the network.'
    ],
    'correct_answer': 'The number of shortest paths from vertex s to vertex t that pass through vertex i.',
    'explanation': "The notation σst(i) represents the number of shortest paths from vertex s to vertex t that pass through vertex i, used in the calculation of betweenness centrality.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq11 = {
    'question': "Which centrality measure calculates the average distance from a vertex to all other vertices in the network?",
    'options_list': [
        'Degree centrality',
        'Betweenness centrality',
        'Closeness centrality',
        'Eigenvector centrality'
    ],
    'correct_answer': 'Closeness centrality',
    'explanation': "Closeness centrality measures the average distance from a vertex to all other vertices in the network, indicating how quickly information can spread from that vertex to others.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq12 = {
    'question': "Which of the following statements about eigenvector centrality is true?",
    'options_list': [
        'It is proportional to the number of shortest paths passing through a vertex.',
        'It considers the centrality of a vertex’s neighbors.',
        'It measures the number of direct connections a vertex has.',
        'It is unaffected by the connections of neighboring vertices.'
    ],
    'correct_answer': 'It considers the centrality of a vertex’s neighbors.',
    'explanation': "Eigenvector centrality measures the influence of a vertex by considering the centrality of its neighbors, meaning a vertex connected to high-centrality neighbors will also have high eigenvector centrality.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq13 = {
    'question': "What is the significance of a vertex with high closeness centrality in a network?",
    'options_list': [
        'It lies on many shortest paths between other vertices.',
        'It has the highest number of direct connections.',
        'It can spread information quickly to the entire network.',
        'It has a low degree centrality.'
    ],
    'correct_answer': 'It can spread information quickly to the entire network.',
    'explanation': "A vertex with high closeness centrality can spread information quickly to the entire network due to its short average distance to all other vertices.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq14 = {
    'question': "How does eigenvector centrality differ from degree centrality?",
    'options_list': [
        'Eigenvector centrality considers the quality of connections, while degree centrality only counts the number of connections.',
        'Eigenvector centrality measures the total number of vertices in the network.',
        'Degree centrality accounts for the influence of neighboring vertices, while eigenvector centrality does not.',
        'Degree centrality considers edge weights, while eigenvector centrality does not.'
    ],
    'correct_answer': 'Eigenvector centrality considers the quality of connections, while degree centrality only counts the number of connections.',
    'explanation': "Eigenvector centrality considers the centrality of a vertex’s neighbors, thus measuring the quality of connections, while degree centrality only counts the number of direct connections.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq15 = {
    'question': "In the context of network analysis, what is meant by 'assortative mixing'?",
    'options_list': [
        'The tendency of vertices to connect with others that have a similar degree.',
        'The process of removing vertices with low centrality.',
        'The calculation of shortest paths between all pairs of vertices.',
        'The measurement of betweenness centrality.'
    ],
    'correct_answer': 'The tendency of vertices to connect with others that have a similar degree.',
    'explanation': "Assortative mixing refers to the tendency of vertices to connect with others that have similar characteristics, such as degree or other attributes.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq16 = {
    'question': "What is a key characteristic of a k-core in network analysis?",
    'options_list': [
        'Every vertex has at least k connections.',
        'It contains only the shortest paths between vertices.',
        'It measures the average degree of vertices.',
        'It includes all possible edges between vertices.'
    ],
    'correct_answer': 'Every vertex has at least k connections.',
    'explanation': "A k-core is a subgraph in which every vertex has at least k connections to other vertices within the subgraph.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq17 = {
    'question': "What does the clustering coefficient measure in a network?",
    'options_list': [
        'The number of direct connections a vertex has.',
        'The extent to which vertices cluster together.',
        'The total number of vertices in the network.',
        'The average path length between all pairs of vertices.'
    ],
    'correct_answer': 'The extent to which vertices cluster together.',
    'explanation': "The clustering coefficient measures the extent to which vertices tend to cluster together, forming tightly knit groups within the network.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq18 = {
    'question': "How is flow betweenness centrality different from standard betweenness centrality?",
    'options_list': [
        'Flow betweenness considers only geodesic paths.',
        'Flow betweenness measures the maximum possible flow between vertices.',
        'Flow betweenness is based on the degree of vertices.',
        'Flow betweenness ignores the direction of edges.'
    ],
    'correct_answer': 'Flow betweenness measures the maximum possible flow between vertices.',
    'explanation': "Flow betweenness centrality measures the maximum possible flow between vertices, considering all possible paths and not just the shortest ones.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq19 = {
    'question': "What is one of the benefits of using the Katz centrality measure?",
    'options_list': [
        'It ignores low-degree vertices.',
        'It can measure the influence of distant vertices.',
        'It is computationally simpler than degree centrality.',
        'It only considers immediate neighbors.'
    ],
    'correct_answer': 'It can measure the influence of distant vertices.',
    'explanation': "Katz centrality can measure the influence of distant vertices by considering the total number of walks between vertices and applying a decay factor to longer walks.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_mcq20 = {
    'question': "Which of the following is true about the harmonic mean closeness centrality?",
    'options_list': [
        'It excludes paths through all vertices with infinite distance.',
        'It is used more frequently than standard closeness centrality.',
        'It measures the longest path between two vertices.',
        'It is the average of all shortest path lengths in the network.'
    ],
    'correct_answer': 'It excludes paths through all vertices with infinite distance.',
    'explanation': "Harmonic mean closeness centrality automatically excludes paths through vertices for which the distance is infinite, making it a useful alternative in disconnected networks.",
    'chapter_information': "Newman Networks Chapter 7"
}
##########
newman_networks_c8_mcq1 = {
    'question': "What is the 'giant component' in a network?",
    'options_list': [
        'The component with the highest degree centrality.',
        'A component that contains all the vertices in the network.',
        'The largest connected component that includes a significant fraction of the entire network.',
        'A component with the smallest average path length.'
    ],
    'correct_answer': 'The largest connected component that includes a significant fraction of the entire network.',
    'explanation': "The 'giant component' is the largest connected subgraph within a network, often encompassing most of the network's vertices.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_mcq2 = {
    'question': "Which of the following best describes the small-world effect in networks?",
    'options_list': [
        'Most vertices are directly connected to each other.',
        'There are few connections between vertices, leading to a sparse network.',
        'Typical path lengths between vertices are surprisingly short, even in large networks.',
        'Vertices form tight clusters with few inter-cluster connections.'
    ],
    'correct_answer': 'Typical path lengths between vertices are surprisingly short, even in large networks.',
    'explanation': "The small-world effect indicates that most nodes in a network can be reached from any other in a small number of steps.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_mcq3 = {
    'question': "What characterizes a power-law degree distribution in networks?",
    'options_list': [
        'Most nodes have the same degree.',
        'A large number of nodes have a high degree.',
        'A small number of nodes (hubs) have a very high degree, while most nodes have a low degree.',
        'Degree distribution follows a normal distribution.'
    ],
    'correct_answer': 'A small number of nodes (hubs) have a very high degree, while most nodes have a low degree.',
    'explanation': "Power-law degree distributions are right-skewed, with a few nodes having many connections and many nodes having few connections.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_mcq4 = {
    'question': "In network analysis, what does a high clustering coefficient indicate?",
    'options_list': [
        'A network with very few connections.',
        'A network with many interconnected triangles.',
        'A network where most nodes have a high degree.',
        'A network with long average path lengths.'
    ],
    'correct_answer': 'A network with many interconnected triangles.',
    'explanation': "A high clustering coefficient indicates that nodes tend to form tightly knit groups with many triangles, or interconnected nodes.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_mcq5 = {
    'question': "What is assortative mixing by degree in a network?",
    'options_list': [
        'Nodes connect to others randomly.',
        'High-degree nodes tend to connect to other high-degree nodes.',
        'Low-degree nodes tend to avoid connecting to high-degree nodes.',
        'Nodes with similar attributes tend to connect to each other.'
    ],
    'correct_answer': 'High-degree nodes tend to connect to other high-degree nodes.',
    'explanation': "Assortative mixing by degree means that nodes with similar degrees (e.g., high-degree nodes) are more likely to connect to each other.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_mcq6 = {
    'question': "Which centrality measure considers both the number of connections a node has and the importance of those connections?",
    'options_list': [
        'Degree centrality',
        'Closeness centrality',
        'Betweenness centrality',
        'Eigenvector centrality'
    ],
    'correct_answer': 'Eigenvector centrality',
    'explanation': "Eigenvector centrality measures the influence of a node based on the influence of its neighbors, considering both the number and importance of connections.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_mcq7 = {
    'question': "What is a weakly connected component in a directed network?",
    'options_list': [
        'A subgraph where each node can reach every other node via directed paths.',
        'A subgraph where connections are ignored to form a single connected component.',
        'A subgraph with no cycles.',
        'A subgraph with the highest clustering coefficient.'
    ],
    'correct_answer': 'A subgraph where connections are ignored to form a single connected component.',
    'explanation': "In a weakly connected component, the direction of edges is ignored, forming a connected component based solely on the presence of edges.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_mcq8 = {
    'question': "Why is the degree distribution important in network analysis?",
    'options_list': [
        'It determines the exact structure of the network.',
        'It helps identify the most important nodes in the network.',
        'It indicates the level of clustering in the network.',
        'It reveals the average path length between nodes.'
    ],
    'correct_answer': 'It helps identify the most important nodes in the network.',
    'explanation': "The degree distribution provides insights into which nodes are highly connected (hubs) and play crucial roles in the network's structure and dynamics.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_mcq9 = {
    'question': "What is the significance of the bow tie structure in directed networks?",
    'options_list': [
        'It shows the most direct paths between all nodes.',
        'It represents the division of the network into one large strongly connected component and smaller components.',
        'It illustrates the hierarchy of nodes based on degree.',
        'It indicates the presence of multiple hubs in the network.'
    ],
    'correct_answer': 'It represents the division of the network into one large strongly connected component and smaller components.',
    'explanation': "The bow tie structure in directed networks depicts a large strongly connected component with in-components and out-components, highlighting the network's connectivity and structure.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_mcq10 = {
    'question': "How does the small-world effect impact the efficiency of networked systems?",
    'options_list': [
        'It increases the average path length between nodes.',
        'It decreases the clustering coefficient.',
        'It enhances the speed of information or resource transfer across the network.',
        'It reduces the overall number of connections in the network.'
    ],
    'correct_answer': 'It enhances the speed of information or resource transfer across the network.',
    'explanation': "The small-world effect, with its short path lengths, allows for rapid dissemination of information or resources, improving the network's efficiency.",
    'chapter_information': "Newman Networks Chapter 8"
}

lecture_graph_basics_mcq1 = {
    'question': "What is a network in the context of graph theory?",
    'options_list': [
        'A system of interconnected highways.',
        'A graph consisting of nodes and edges.',
        'A collection of unrelated data points.',
        'A series of interconnected equations.'
    ],
    'correct_answer': 'A graph consisting of nodes and edges.',
    'explanation': "A network in graph theory is a graph consisting of nodes (vertices) and edges (connections) between them.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq2 = {
    'question': "In a social network like Facebook, what do the nodes and edges represent?",
    'options_list': [
        'Nodes are users, and edges are friendships.',
        'Nodes are posts, and edges are comments.',
        'Nodes are groups, and edges are group memberships.',
        'Nodes are photos, and edges are tags.'
    ],
    'correct_answer': 'Nodes are users, and edges are friendships.',
    'explanation': "In a social network like Facebook, the nodes represent users and the edges represent friendships between users.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq3 = {
    'question': "Which of the following is an example of an undirected network?",
    'options_list': [
        'Road networks.',
        'Citation networks.',
        'Ancestral trees.',
        'Email communication networks.'
    ],
    'correct_answer': 'Road networks.',
    'explanation': "Road networks are an example of undirected networks where the edges (roads) have no direction.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq4 = {
    'question': "What type of network is represented by cities connected by railroads?",
    'options_list': [
        'Social network',
        'Transportation network',
        'Biological network',
        'Computer network'
    ],
    'correct_answer': 'Transportation network',
    'explanation': "A network of cities connected by railroads is a transportation network.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq5 = {
    'question': "What does it mean for a graph to be bipartite?",
    'options_list': [
        'The graph has two nodes connected by an edge.',
        'The graph can be divided into two sets of nodes with edges only between sets, not within sets.',
        'The graph has at least two cycles.',
        'The graph has a hierarchical structure.'
    ],
    'correct_answer': 'The graph can be divided into two sets of nodes with edges only between sets, not within sets.',
    'explanation': "A bipartite graph can be divided into two distinct sets of nodes, with edges only between nodes of different sets.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq6 = {
    'question': "How can a large, sparse network be efficiently stored?",
    'options_list': [
        'Using a full adjacency matrix.',
        'As a list of nodes.',
        'As an edge list.',
        'In a complete graph format.'
    ],
    'correct_answer': 'As an edge list.',
    'explanation': "A large, sparse network can be efficiently stored as an edge list, which saves space by only recording the edges that exist.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq7 = {
    'question': "What is an adjacency matrix?",
    'options_list': [
        'A matrix showing the shortest paths between nodes.',
        'A matrix representing the connections between nodes in a graph.',
        'A list of nodes in the network.',
        'A hierarchical representation of a graph.'
    ],
    'correct_answer': 'A matrix representing the connections between nodes in a graph.',
    'explanation': "An adjacency matrix is a square matrix used to represent a finite graph, where the elements indicate whether pairs of vertices are adjacent or not.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq8 = {
    'question': "What property distinguishes a directed graph from an undirected graph?",
    'options_list': [
        'The presence of weighted edges.',
        'The direction of edges.',
        'The number of nodes.',
        'The absence of cycles.'
    ],
    'correct_answer': 'The direction of edges.',
    'explanation': "A directed graph has edges with a direction, indicating a one-way relationship between nodes.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq9 = {
    'question': "In which type of graph can you find both a source and a sink node?",
    'options_list': [
        'Undirected graph',
        'Bipartite graph',
        'Directed acyclic graph (DAG)',
        'Complete graph'
    ],
    'correct_answer': 'Directed acyclic graph (DAG)',
    'explanation': "In a directed acyclic graph (DAG), you can have source and sink nodes, which have only outgoing and incoming edges respectively.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq10 = {
    'question': "What is a hypergraph?",
    'options_list': [
        'A graph with multiple edges between nodes.',
        'A graph where edges can connect more than two nodes.',
        'A complete graph with weighted edges.',
        'A hierarchical graph with cycles.'
    ],
    'correct_answer': 'A graph where edges can connect more than two nodes.',
    'explanation': "A hypergraph is a generalization of a graph where edges (called hyperedges) can connect more than two nodes.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq11 = {
    'question': "What is a common characteristic of degree distribution in social networks?",
    'options_list': [
        'Uniform distribution',
        'Bell-shaped curve',
        'Long-tailed distribution',
        'Normal distribution'
    ],
    'correct_answer': 'Long-tailed distribution',
    'explanation': "In social networks, the degree distribution typically has a long tail, meaning there are a few nodes with very high degree (hubs) and many nodes with a low degree.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq12 = {
    'question': "Which plot is often used to represent a power-law degree distribution?",
    'options_list': [
        'Linear plot',
        'Logarithmic plot',
        'Log-log plot',
        'Histogram'
    ],
    'correct_answer': 'Log-log plot',
    'explanation': "A power-law degree distribution is often represented using a log-log plot where both axes are on a logarithmic scale, making the distribution appear linear.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq13 = {
    'question': "What is the clustering coefficient of a network?",
    'options_list': [
        'The ratio of actual triangles to all possible triangles in the network.',
        'The total number of triangles in the network.',
        'The average degree of the nodes in the network.',
        'The density of edges in the network.'
    ],
    'correct_answer': 'The ratio of actual triangles to all possible triangles in the network.',
    'explanation': "The clustering coefficient measures how clustered a network is by comparing the number of actual triangles to the number of possible triangles in the network.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq14 = {
    'question': "How do you find connected components in a graph?",
    'options_list': [
        'Using a shortest path algorithm',
        'Using breadth-first search (BFS) or depth-first search (DFS)',
        'Using a maximum flow algorithm',
        'Using Dijkstra\'s algorithm'
    ],
    'correct_answer': 'Using breadth-first search (BFS) or depth-first search (DFS)',
    'explanation': "Connected components can be found using BFS or DFS by exploring all nodes reachable from each starting node and marking them as part of the same component.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq15 = {
    'question': "What does it mean for a network to be sparse?",
    'options_list': [
        'It has a high edge density.',
        'The number of edges grows quadratically with the number of nodes.',
        'The edge density goes to zero as the network size increases.',
        'It is fully connected.'
    ],
    'correct_answer': 'The edge density goes to zero as the network size increases.',
    'explanation': "A network is considered sparse if its edge density decreases towards zero as the number of nodes increases, meaning the number of edges grows slower than quadratically with the number of nodes.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq16 = {
    'question': "What is a characteristic of a dense network?",
    'options_list': [
        'It has few edges compared to the number of nodes.',
        'The number of edges grows quadratically with the number of nodes.',
        'It has a constant number of edges as the number of nodes increases.',
        'It has no cycles.'
    ],
    'correct_answer': 'The number of edges grows quadratically with the number of nodes.',
    'explanation': "A dense network is characterized by a number of edges that grows quadratically with the number of nodes, resulting in a high edge density.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq17 = {
    'question': "Which algorithm can be used to suggest new friends in a social network?",
    'options_list': [
        'Breadth-first search',
        'Matrix multiplication of the adjacency matrix',
        'Shortest path algorithm',
        'Dijkstra's algorithm'
    ],
    'correct_answer': 'Matrix multiplication of the adjacency matrix',
    'explanation': "New friends can be suggested in a social network by multiplying the adjacency matrix with itself to find common neighbors, indicating potential new friendships.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq18 = {
    'question': "What is the purpose of using a sparse matrix representation for large networks?",
    'options_list': [
        'To simplify the network',
        'To reduce computational complexity and memory usage',
        'To make the network more connected',
        'To increase the number of edges'
    ],
    'correct_answer': 'To reduce computational complexity and memory usage',
    'explanation': "A sparse matrix representation is used to reduce computational complexity and memory usage by only storing non-zero entries, which is efficient for large networks with many zero entries.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq19 = {
    'question': "Which of the following is a measure of how quickly information spreads in a network?",
    'options_list': [
        'Clustering coefficient',
        'Degree distribution',
        'Diameter of the network',
        'Number of connected components'
    ],
    'correct_answer': 'Diameter of the network',
    'explanation': "The diameter of a network, which is the longest shortest path between any two nodes, indicates how quickly information or diseases can spread across the network.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq20 = {
    'question': "What is a bipartite network?",
    'options_list': [
        'A network with two connected components.',
        'A network with edges that only connect nodes from two different sets.',
        'A network where every node is connected to every other node.',
        'A network with directed and undirected edges.'
    ],
    'correct_answer': 'A network with edges that only connect nodes from two different sets.',
    'explanation': "In a bipartite network, nodes are divided into two disjoint sets, and edges only connect nodes from different sets, not within the same set.",
    'chapter_information': "Lecture Graph Basics"
}
