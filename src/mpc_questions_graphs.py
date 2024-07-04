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
        'Dijkstra\'s algorithm'
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


################################
lecture_graph_basics_mcq01x = {
    'question': "What is the diameter of a network?",
    'options_list': [
        'The average degree of the nodes',
        'The largest distance between any two nodes',
        'The number of edges in the network',
        'The clustering coefficient'
    ],
    'correct_answer': 'The largest distance between any two nodes',
    'explanation': "The diameter of a network is defined as the largest distance (shortest path) between any two nodes.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq02x = {
    'question': "Which algorithm is used to compute the shortest path in a weighted network?",
    'options_list': [
        'Breadth-First Search (BFS)',
        'Depth-First Search (DFS)',
        'Dijkstra\'s Algorithm',
        'Floyd-Warshall Algorithm'
    ],
    'correct_answer': 'Dijkstra\'s Algorithm',
    'explanation': "Dijkstra's Algorithm is used to compute the shortest path between nodes in a weighted network.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq03x = {
    'question': "What does a clustering coefficient measure in a network?",
    'options_list': [
        'The number of edges divided by the number of nodes',
        'The average degree of the nodes',
        'The tendency of nodes to form triangles',
        'The longest shortest path between any two nodes'
    ],
    'correct_answer': 'The tendency of nodes to form triangles',
    'explanation': "The clustering coefficient measures how likely it is for a node's neighbors to be connected, indicating the tendency of nodes to form triangles.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq04x = {
    'question': "What is modularity in the context of network analysis?",
    'options_list': [
        'The number of edges in the network',
        'The fraction of edges between nodes of the same type, normalized',
        'The largest distance between any two nodes',
        'The degree distribution of the network'
    ],
    'correct_answer': 'The fraction of edges between nodes of the same type, normalized',
    'explanation': "Modularity is a measure of the strength of division of a network into modules (clusters), comparing the fraction of edges within the same type of nodes to what is expected by chance.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq05x = {
    'question': "What is the significance of the '6 degrees of separation' concept in social networks?",
    'options_list': [
        'It indicates the clustering coefficient of the network.',
        'It suggests that any two people are connected through at most six steps.',
        'It defines the diameter of the network.',
        'It measures the density of the network.'
    ],
    'correct_answer': 'It suggests that any two people are connected through at most six steps.',
    'explanation': "The '6 degrees of separation' concept suggests that any two individuals in a social network are connected through a chain of at most six people.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq06x = {
    'question': "Which of the following is NOT a method for measuring the structure of a network?",
    'options_list': [
        'Degree distribution',
        'Clustering coefficient',
        'Average distance',
        'Modularity'
    ],
    'correct_answer': 'Modularity',
    'explanation': "Modularity is used to measure the strength of division of a network into clusters, not the overall structure of the network.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq07x = {
    'question': "What is a key characteristic of homophily in social networks?",
    'options_list': [
        'Nodes of different types are more likely to be connected.',
        'Nodes of the same type are more likely to be connected.',
        'The network has a high clustering coefficient.',
        'The network has a large diameter.'
    ],
    'correct_answer': 'Nodes of the same type are more likely to be connected.',
    'explanation': "Homophily is the tendency for nodes of the same type to be more connected than nodes of different types.",
    'chapter_information': "Lecture Graph Basics"
}

lecture_graph_basics_mcq08x = {
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

################################
fb_social_graph_mcq01 = {
    'question': "What is a connected component in the context of a social network graph?",
    'options_list': [
        'A group of nodes where each node is directly connected to every other node.',
        'A group of nodes where there is a path between any two nodes within the group.',
        'A single node with no edges connecting it to other nodes.',
        'A pair of nodes connected by a single edge.'
    ],
    'correct_answer': 'A group of nodes where there is a path between any two nodes within the group.',
    'explanation': "In graph theory, a connected component is a subset of nodes such that there is a path between any pair of nodes within the subset.",
    'chapter_information': "The Anatomy of the Facebook Social Graph"
}

fb_social_graph_mcq02 = {
    'question': "What does the term 'degree distribution' refer to in a social network graph?",
    'options_list': [
        'The total number of nodes in the graph.',
        'The distribution of the number of connections (or friends) each node has.',
        'The arrangement of nodes in a specific pattern.',
        'The average number of connections per node.'
    ],
    'correct_answer': 'The distribution of the number of connections (or friends) each node has.',
    'explanation': "The degree distribution of a graph shows how many nodes have each possible degree (number of connections), indicating the frequency of nodes with a certain number of connections.",
    'chapter_information': "The Anatomy of the Facebook Social Graph"
}

fb_social_graph_mcq03 = {
    'question': "What is meant by the 'small-world phenomenon' in social networks?",
    'options_list': [
        'Every node is directly connected to every other node.',
        'Most nodes are not directly connected, but the average path length between any two nodes is short.',
        'The graph is divided into several disconnected components.',
        'Each node has a unique identifier.'
    ],
    'correct_answer': 'Most nodes are not directly connected, but the average path length between any two nodes is short.',
    'explanation': "The small-world phenomenon refers to the property of social networks where most nodes can be reached from any other node in a small number of steps, despite not being directly connected.",
    'chapter_information': "The Anatomy of the Facebook Social Graph"
}

fb_social_graph_mcq04 = {
    'question': "What does a high clustering coefficient indicate about a social network?",
    'options_list': [
        'The network is sparsely connected.',
        'There are many triangles in the network, indicating that friends of a person are also likely to be friends with each other.',
        'The network has many isolated nodes.',
        'The network has a hierarchical structure.'
    ],
    'correct_answer': 'There are many triangles in the network, indicating that friends of a person are also likely to be friends with each other.',
    'explanation': "A high clustering coefficient means that the network has a high tendency for nodes to cluster together, forming triangles where each node is connected to two others.",
    'chapter_information': "The Anatomy of the Facebook Social Graph"
}

fb_social_graph_mcq05 = {
    'question': "How does assortativity manifest in a social network like Facebook?",
    'options_list': [
        'Users tend to have friends from different demographic groups.',
        'Users tend to have friends with a similar number of connections (friends).',
        'Users are randomly connected regardless of their attributes.',
        'Users have the same number of connections as their friends.'
    ],
    'correct_answer': 'Users tend to have friends with a similar number of connections (friends).',
    'explanation': "Assortativity in a social network indicates that nodes (users) tend to connect with other nodes that have a similar degree (number of connections), showing a preference for similarity.",
    'chapter_information': "The Anatomy of the Facebook Social Graph"
}

fb_social_graph_mcq06 = {
    'question': "What is the significance of the 'six degrees of separation' observed in the Facebook social graph?",
    'options_list': [
        'Every user is directly connected to six other users.',
        'Most users can be reached from any other user in about six steps.',
        'There are six large connected components in the network.',
        'Each user has exactly six friends.'
    ],
    'correct_answer': 'Most users can be reached from any other user in about six steps.',
    'explanation': "The 'six degrees of separation' phenomenon implies that on average, any two users in the Facebook network are separated by about six steps or connections.",
    'chapter_information': "The Anatomy of the Facebook Social Graph"
}

fb_social_graph_mcq07 = {
    'question': "What does the study reveal about the relationship between user engagement (logins) and the number of friends?",
    'options_list': [
        'There is no correlation between user engagement and the number of friends.',
        'Users who log in more frequently tend to have more friends.',
        'Users who log in less frequently have more friends.',
        'User engagement decreases as the number of friends increases.'
    ],
    'correct_answer': 'Users who log in more frequently tend to have more friends.',
    'explanation': "The study shows a positive correlation between user engagement, measured by the number of logins, and the number of friends a user has.",
    'chapter_information': "The Anatomy of the Facebook Social Graph"
}

fb_social_graph_mcq08 = {
    'question': "What does modularity in the context of the Facebook social network refer to?",
    'options_list': [
        'The tendency for the network to be evenly distributed.',
        'The extent to which the network can be divided into clusters or communities.',
        'The presence of isolated nodes in the network.',
        'The frequency of direct connections between nodes.'
    ],
    'correct_answer': 'The extent to which the network can be divided into clusters or communities.',
    'explanation': "Modularity measures the strength of division of a network into clusters or communities, where nodes within the same community are more densely connected to each other than to nodes in other communities.",
    'chapter_information': "The Anatomy of the Facebook Social Graph"
}

fb_social_graph_mcq09 = {
    'question': "What is the significance of finding a large giant component in the Facebook social network?",
    'options_list': [
        'It indicates that most users are isolated.',
        'It shows that the majority of users are interconnected, forming a massive connected subgraph.',
        'It implies that the network has a hierarchical structure.',
        'It means that users have the same number of friends.'
    ],
    'correct_answer': 'It shows that the majority of users are interconnected, forming a massive connected subgraph.',
    'explanation': "The presence of a giant component means that the majority of users are part of a single, large interconnected subgraph, indicating high overall connectivity within the network.",
    'chapter_information': "The Anatomy of the Facebook Social Graph"
}

fb_social_graph_mcq10 = {
    'question': "What does the study conclude about gender homophily in the Facebook social network?",
    'options_list': [
        'There is a strong preference for same-gender friendships.',
        'There is no significant gender homophily.',
        'Male users tend to have more male friends.',
        'Female users tend to have more female friends.'
    ],
    'correct_answer': 'There is no significant gender homophily.',
    'explanation': "The study found no strong gender homophily, indicating that users do not show a strong preference for forming friendships with others of the same gender.",
    'chapter_information': "The Anatomy of the Facebook Social Graph"
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
        'Dijkstra\'s algorithm'
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

lecture_graph_centrality_mcq1 = {
    'question': "What does betweenness centrality measure in a network?",
    'options_list': [
        'The number of edges connected to a node',
        'The average shortest path from a node to all other nodes',
        'The extent to which a node lies on paths between other nodes',
        'The clustering coefficient of a node'
    ],
    'correct_answer': 'The extent to which a node lies on paths between other nodes',
    'explanation': "Betweenness centrality measures how often a node appears on the shortest paths between other nodes in the network.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq2 = {
    'question': "Which centrality measure considers the number of connections a node's neighbors have?",
    'options_list': [
        'Betweenness centrality',
        'Closeness centrality',
        'Degree centrality',
        'Eigenvector centrality'
    ],
    'correct_answer': 'Eigenvector centrality',
    'explanation': "Eigenvector centrality takes into account not just the number of connections a node has, but also the centrality of its neighbors.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq3 = {
    'question': "How is closeness centrality of a node defined?",
    'options_list': [
        'The number of edges connected to the node',
        'The inverse of the average shortest path distance from the node to all other nodes',
        'The number of shortest paths that pass through the node',
        'The number of triangles the node is part of'
    ],
    'correct_answer': 'The inverse of the average shortest path distance from the node to all other nodes',
    'explanation': "Closeness centrality is defined as the inverse of the average shortest path distance from a node to all other nodes in the network.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq4 = {
    'question': "In a directed graph, when is the in-degree of a node important?",
    'options_list': [
        'When analyzing social networks where following relationships matter',
        'When determining how information spreads through the network',
        'When identifying the most central node in an undirected network',
        'When measuring the clustering coefficient of the network'
    ],
    'correct_answer': 'When analyzing social networks where following relationships matter',
    'explanation': "In a social network with directed edges, the in-degree of a node (number of incoming edges) can indicate the node's popularity or influence.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq5 = {
    'question': "What is eigenvector centrality particularly useful for?",
    'options_list': [
        'Identifying nodes that are important based on their connections to highly connected nodes',
        'Measuring the direct influence of a node',
        'Finding the shortest path between two nodes',
        'Calculating the total number of edges in the network'
    ],
    'correct_answer': 'Identifying nodes that are important based on their connections to highly connected nodes',
    'explanation': "Eigenvector centrality helps identify nodes that are important not just based on their direct connections, but also on the importance of their neighbors.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq6 = {
    'question': "What is a problem with using eigenvector centrality in directed networks?",
    'options_list': [
        'It does not account for the direction of edges.',
        'Sink nodes will cause all scores to eventually become zero.',
        'It cannot be applied to weighted networks.',
        'It requires a complete graph.'
    ],
    'correct_answer': 'Sink nodes will cause all scores to eventually become zero.',
    'explanation': "In directed networks, if there are sink nodes (nodes with no outgoing edges), their scores will become zero and propagate this zero score backwards, causing all scores to eventually become zero.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq7 = {
    'question': "How can the problem of zero scores in eigenvector centrality be remedied in directed networks?",
    'options_list': [
        'By normalizing the scores based on the total number of nodes',
        'By adding a small constant score to each node at each iteration',
        'By ignoring sink nodes in the calculation',
        'By using undirected versions of the graph'
    ],
    'correct_answer': 'By adding a small constant score to each node at each iteration',
    'explanation': "To prevent scores from becoming zero, a small constant score is added to each node at each iteration. This ensures that every node maintains some level of importance.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq8 = {
    'question': "What is the main adjustment made in PageRank to account for the importance of a node?",
    'options_list': [
        'It adds a small constant score to each node.',
        'It divides the importance by the number of outgoing links of the node.',
        'It considers the clustering coefficient of the node.',
        'It only considers the shortest paths in the network.'
    ],
    'correct_answer': 'It divides the importance by the number of outgoing links of the node.',
    'explanation': "PageRank scales the importance transferred from one node to another by dividing it by the number of outgoing links, reflecting the probability of following one of the links.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq9 = {
    'question': "Why is it beneficial to add a small constant score in PageRank calculations?",
    'options_list': [
        'To ensure that the graph remains connected',
        'To avoid the problem of sink nodes causing zero scores',
        'To increase the computational complexity',
        'To improve the clustering coefficient of the graph'
    ],
    'correct_answer': 'To avoid the problem of sink nodes causing zero scores',
    'explanation': "Adding a small constant score prevents the zero score problem caused by sink nodes and ensures that every node has some level of importance.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq10 = {
    'question': "In PageRank, what does the term 'beta' refer to?",
    'options_list': [
        'The number of nodes in the network',
        'The constant score given to each node at each iteration',
        'The total number of edges in the network',
        'The sum of all node degrees'
    ],
    'correct_answer': 'The constant score given to each node at each iteration',
    'explanation': "In PageRank, 'beta' refers to the constant score assigned to each node at each iteration to ensure that all nodes maintain some importance.",
    'chapter_information': "Lecture Graph Centrality Measures"
}


lecture_graph_centrality_mcq11 = {
    'question': "What is a sink node in a directed network?",
    'options_list': [
        'A node with no incoming edges',
        'A node with no outgoing edges',
        'A node that connects two different components of the network',
        'A node with the highest degree'
    ],
    'correct_answer': 'A node with no outgoing edges',
    'explanation': "A sink node is a node that does not have any outgoing edges, meaning it does not point to any other nodes in the network.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq12 = {
    'question': "How does adding a small constant score (beta) to each node help in centrality calculations?",
    'options_list': [
        'It normalizes the scores across all nodes.',
        'It ensures that no node has a score of zero.',
        'It increases the computational complexity.',
        'It balances the in-degree and out-degree of nodes.'
    ],
    'correct_answer': 'It ensures that no node has a score of zero.',
    'explanation': "Adding a small constant score to each node prevents scores from becoming zero, ensuring that every node maintains some level of importance.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq13 = {
    'question': "What is the primary adjustment made in the PageRank algorithm compared to simple eigenvector centrality?",
    'options_list': [
        'Adding a small constant score to each node',
        'Dividing the importance score by the number of outgoing links of a node',
        'Ignoring sink nodes in the calculation',
        'Using undirected versions of the graph'
    ],
    'correct_answer': 'Dividing the importance score by the number of outgoing links of a node',
    'explanation': "The PageRank algorithm divides the importance score transferred from one node to another by the number of outgoing links, reflecting the probability of following one of the links.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq14 = {
    'question': "Why is it important to divide the importance score by the number of outgoing links in PageRank?",
    'options_list': [
        'To ensure the graph remains connected',
        'To account for the likelihood of clicking on one link among many',
        'To increase the overall importance of nodes',
        'To measure the clustering coefficient of the graph'
    ],
    'correct_answer': 'To account for the likelihood of clicking on one link among many',
    'explanation': "Dividing the importance score by the number of outgoing links accounts for the probability that a user will click on any one link among many on a webpage.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq15 = {
    'question': "In the context of PageRank, what does the term 'alpha' refer to?",
    'options_list': [
        'The number of nodes in the network',
        'The damping factor used to adjust the scores',
        'The total number of edges in the network',
        'The sum of all node degrees'
    ],
    'correct_answer': 'The damping factor used to adjust the scores',
    'explanation': "In PageRank, 'alpha' refers to the damping factor that ensures the convergence of the algorithm by adjusting the scores appropriately.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq16 = {
    'question': "In a citation network, what does an 'authority' represent?",
    'options_list': [
        'A node with no incoming edges',
        'A node that points to many other nodes',
        'A node that is pointed to by many important nodes',
        'A node with the highest out-degree'
    ],
    'correct_answer': 'A node that is pointed to by many important nodes',
    'explanation': "In a citation network, an authority is a node that contains important information itself and is pointed to by many important nodes.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq17 = {
    'question': "What does a 'hub' represent in a citation network?",
    'options_list': [
        'A node that points to many important nodes',
        'A node with no outgoing edges',
        'A node with the highest in-degree',
        'A node that is a sink'
    ],
    'correct_answer': 'A node that points to many important nodes',
    'explanation': "In a citation network, a hub is a node that is important because it points to many other important nodes, often acting as a review or summary.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq18 = {
    'question': "How do you calculate the authority score in a citation network?",
    'options_list': [
        'By summing the in-degrees of the node',
        'By considering the number of shortest paths passing through the node',
        'By summing the hub scores of nodes pointing to it',
        'By considering the out-degrees of the node'
    ],
    'correct_answer': 'By summing the hub scores of nodes pointing to it',
    'explanation': "The authority score of a node in a citation network is calculated by summing the hub scores of nodes pointing to it.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq19 = {
    'question': "What is the relationship between eigenvalues and the convergence of authority and hub scores?",
    'options_list': [
        'The scores converge to the eigenvector corresponding to the maximum eigenvalue of the adjacency matrix',
        'The scores converge to the smallest eigenvalue of the adjacency matrix',
        'The scores depend on the sum of all eigenvalues',
        'There is no relationship between eigenvalues and score convergence'
    ],
    'correct_answer': 'The scores converge to the eigenvector corresponding to the maximum eigenvalue of the adjacency matrix',
    'explanation': "The authority and hub scores converge to the eigenvector corresponding to the maximum eigenvalue of the adjacency matrix.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_graph_centrality_mcq20 = {
    'question': "How can you determine if a paper is more of a hub or an authority?",
    'options_list': [
        'By comparing its in-degree and out-degree',
        'By evaluating its betweenness centrality',
        'By calculating its scores using both hub and authority measures',
        'By checking if it has more incoming or outgoing edges'
    ],
    'correct_answer': 'By calculating its scores using both hub and authority measures',
    'explanation': "To determine if a paper is more of a hub or an authority, you calculate its scores using both hub and authority measures and compare them.",
    'chapter_information': "Lecture Graph Centrality Measures"
}

lecture_steiner_trees_mcq1 = {
    'question': "What is the primary goal of the Steiner tree problem in graphs?",
    'options_list': [
        'To find the shortest path between two nodes',
        'To identify the minimum subnetwork connecting a specific set of nodes',
        'To calculate the diameter of the network',
        'To determine the maximum flow between two nodes'
    ],
    'correct_answer': 'To identify the minimum subnetwork connecting a specific set of nodes',
    'explanation': "The Steiner tree problem aims to find the smallest subnetwork that connects a specified set of nodes, minimizing the sum of all edge weights in the subnetwork.",
    'chapter_information': "Introduction to Steiner Trees"
}

lecture_steiner_trees_mcq2 = {
    'question': "In the context of the Steiner tree problem, what are 'terminals'?",
    'options_list': [
        'Nodes with the highest degree',
        'Nodes that must be connected in the subnetwork',
        'Nodes that have no outgoing edges',
        'Nodes that are isolated in the network'
    ],
    'correct_answer': 'Nodes that must be connected in the subnetwork',
    'explanation': "Terminals are the specific nodes in a graph that must be connected in the Steiner tree.",
    'chapter_information': "Introduction to Steiner Trees"
}

lecture_steiner_trees_mcq3 = {
    'question': "Why is the Steiner tree problem considered NP-hard?",
    'options_list': [
        'It can only be solved in polynomial time',
        'It requires finding the shortest path in the network',
        'It involves deciding which additional nodes to include to minimize the subnetwork',
        'It is equivalent to finding the minimum spanning tree'
    ],
    'correct_answer': 'It involves deciding which additional nodes to include to minimize the subnetwork',
    'explanation': "The Steiner tree problem is NP-hard because it requires deciding which additional nodes should be included to create the smallest subnetwork connecting the terminals, which is computationally difficult.",
    'chapter_information': "Introduction to Steiner Trees"
}

lecture_steiner_trees_mcq4 = {
    'question': "How does the Steiner tree problem differ from the minimum spanning tree problem?",
    'options_list': [
        'The Steiner tree problem connects all nodes in the graph',
        'The minimum spanning tree problem is NP-hard',
        'The Steiner tree problem only connects a specific set of nodes',
        'The minimum spanning tree problem requires additional edge weights'
    ],
    'correct_answer': 'The Steiner tree problem only connects a specific set of nodes',
    'explanation': "The Steiner tree problem focuses on connecting a specific set of nodes (terminals) at minimum cost, whereas the minimum spanning tree problem connects all nodes in the graph.",
    'chapter_information': "Introduction to Steiner Trees"
}

lecture_steiner_trees_mcq5 = {
    'question': "What is a common approximation method for solving the Steiner tree problem?",
    'options_list': [
        'Using the shortest path algorithm',
        'Using minimum spanning tree algorithms on a distance matrix',
        'Using depth-first search',
        "Using Dijkstra's algorithm"
    ],
    'correct_answer': 'Using minimum spanning tree algorithms on a distance matrix',
    'explanation': "A common approximation method for the Steiner tree problem involves creating a distance matrix for the terminal nodes and applying minimum spanning tree algorithms to this matrix.",
    'chapter_information': "Introduction to Steiner Trees"
}

lecture_steiner_trees_mcq6 = {
    'question': "What is the significance of the approximation factor in Steiner tree algorithms?",
    'options_list': [
        'It determines the computational complexity',
        'It provides a guarantee on how close the solution is to the optimal',
        'It indicates the number of terminals',
        'It measures the diameter of the network'
    ],
    'correct_answer': 'It provides a guarantee on how close the solution is to the optimal',
    'explanation': "The approximation factor in Steiner tree algorithms indicates how close the approximate solution is to the optimal solution, providing a measure of solution quality.",
    'chapter_information': "Introduction to Steiner Trees"
}

lecture_steiner_trees_mcq7 = {
    'question': "What is the primary challenge in finding the exact Steiner tree in a graph?",
    'options_list': [
        'It requires calculating the shortest path between all pairs of nodes',
        'It involves determining which additional nodes should be included to minimize the subnetwork',
        'It can only be solved for bipartite graphs',
        'It requires knowledge of all possible spanning trees'
    ],
    'correct_answer': 'It involves determining which additional nodes should be included to minimize the subnetwork',
    'explanation': "The primary challenge in finding the exact Steiner tree is deciding which additional nodes should be included to create the smallest subnetwork connecting the terminals, which makes it an NP-hard problem.",
    'chapter_information': "Introduction to Steiner Trees"
}

lecture_steiner_trees_mcq8 = {
    'question': "How is an approximate Steiner tree typically found using the minimum spanning tree method?",
    'options_list': [
        'By finding the shortest paths between all pairs of nodes and connecting them',
        'By creating a distance matrix for the terminal nodes and applying a minimum spanning tree algorithm to this matrix',
        'By calculating the maximum flow between nodes',
        'By using depth-first search on the entire graph'
    ],
    'correct_answer': 'By creating a distance matrix for the terminal nodes and applying a minimum spanning tree algorithm to this matrix',
    'explanation': "An approximate Steiner tree can be found by creating a distance matrix for the terminal nodes and then applying a minimum spanning tree algorithm to this matrix, providing a close approximation to the exact solution.",
    'chapter_information': "Introduction to Steiner Trees"
}


lecture_community_detection_mcq1 = {
    'question': "What is the primary goal of community detection in networks?",
    'options_list': [
        'To find the shortest path between nodes',
        'To identify nodes that are more densely connected to each other than to other nodes',
        'To calculate the centrality of nodes',
        'To determine the diameter of the network'
    ],
    'correct_answer': 'To identify nodes that are more densely connected to each other than to other nodes',
    'explanation': "Community detection aims to identify groups of nodes that are more densely connected to each other than to nodes outside the group.",
    'chapter_information': "Community Detection in Networks"
}

lecture_community_detection_mcq2 = {
    'question': "How can the geodesic distance be used in community detection?",
    'options_list': [
        'To measure the degree of each node',
        'To define the similarity between nodes based on their shortest path distance',
        'To calculate the diameter of the network',
        'To determine the flow of information in the network'
    ],
    'correct_answer': 'To define the similarity between nodes based on their shortest path distance',
    'explanation': "Geodesic distance can be used to define the similarity between nodes by considering the shortest path distance between them.",
    'chapter_information': "Community Detection in Networks"
}

lecture_community_detection_mcq3 = {
    'question': "What is the betweenness centrality of an edge used for in community detection?",
    'options_list': [
        'To find the shortest path between two nodes',
        'To determine the number of shortest paths that pass through the edge',
        'To identify edges that are most central to connecting different communities',
        'To calculate the clustering coefficient of the network'
    ],
    'correct_answer': 'To identify edges that are most central to connecting different communities',
    'explanation': "Betweenness centrality of an edge is used to identify edges that are most central to connecting different communities by counting the number of shortest paths that pass through the edge.",
    'chapter_information': "Community Detection in Networks"
}

lecture_community_detection_mcq4 = {
    'question': "How does the Louvain method perform community detection?",
    'options_list': [
        'By using the shortest path algorithm',
        'By iteratively grouping nodes to maximize modularity',
        'By calculating the degree of each node',
        'By using depth-first search'
    ],
    'correct_answer': 'By iteratively grouping nodes to maximize modularity',
    'explanation': "The Louvain method performs community detection by iteratively grouping nodes in a way that maximizes the modularity of the network.",
    'chapter_information': "Community Detection in Networks"
}

lecture_community_detection_mcq5 = {
    'question': "What is modularity in the context of community detection?",
    'options_list': [
        'A measure of the average degree of nodes in a community',
        'A quality function that quantifies the strength of division of a network into communities',
        'The sum of all edge weights in the network',
        'The total number of shortest paths in the network'
    ],
    'correct_answer': 'A quality function that quantifies the strength of division of a network into communities',
    'explanation': "Modularity is a quality function that quantifies how well a network is divided into communities compared to a random model.",
    'chapter_information': "Community Detection in Networks"
}

lecture_community_detection_mcq6 = {
    'question': "Why is optimizing modularity considered an NP-complete problem?",
    'options_list': [
        'Because it can only be solved in polynomial time',
        'Because it requires finding the shortest path in the network',
        'Because it involves examining all possible partitions of the network',
        'Because it requires calculating the degree of each node'
    ],
    'correct_answer': 'Because it involves examining all possible partitions of the network',
    'explanation': "Optimizing modularity is NP-complete because it involves examining all possible partitions of the network to find the one that maximizes modularity.",
    'chapter_information': "Community Detection in Networks"
}

lecture_community_detection_mcq7 = {
    'question': "How does the divisive algorithm use betweenness centrality for community detection?",
    'options_list': [
        'By merging nodes with the highest betweenness centrality',
        'By removing edges with the highest betweenness centrality to break up the network',
        'By calculating the degree of each node',
        'By finding the shortest path between nodes'
    ],
    'correct_answer': 'By removing edges with the highest betweenness centrality to break up the network',
    'explanation': "The divisive algorithm uses betweenness centrality by removing edges with the highest betweenness centrality, which breaks up the network into communities.",
    'chapter_information': "Community Detection in Networks"
}

lecture_community_detection_mcq8 = {
    'question': "What type of community detection method is spectral clustering?",
    'options_list': [
        'A method based on edge betweenness',
        'A method based on optimizing modularity',
        'A method based on the eigenvalues and eigenvectors of matrices',
        'A method based on hierarchical clustering'
    ],
    'correct_answer': 'A method based on the eigenvalues and eigenvectors of matrices',
    'explanation': "Spectral clustering is a community detection method that uses the eigenvalues and eigenvectors of matrices to identify clusters within the network.",
    'chapter_information': "Community Detection in Networks"
}

lecture_spectral_clustering_mcq1 = {
    'question': "What is the purpose of using the second smallest eigenvalue in spectral clustering?",
    'options_list': [
        'To minimize the within-cluster distance',
        'To maximize the between-cluster distance',
        'To find the approximate solution to the ideal clustering problem',
        'To identify outliers in the dataset'
    ],
    'correct_answer': 'To find the approximate solution to the ideal clustering problem',
    'explanation': "The second smallest eigenvalue (also known as the Fiedler value) and its corresponding eigenvector help identify clusters in the graph by separating nodes into clusters based on the signs and magnitudes of the eigenvector components.",
    'chapter_information': "Spectral Clustering"
}

lecture_spectral_clustering_mcq2 = {
    'question': "How does the graph Laplacian relate to spectral clustering?",
    'options_list': [
        'It is used to compute the similarity matrix',
        'It provides the eigenvalues and eigenvectors used for clustering',
        'It normalizes the data before clustering',
        'It is only used for directed graphs'
    ],
    'correct_answer': 'It provides the eigenvalues and eigenvectors used for clustering',
    'explanation': "The graph Laplacian is a matrix representation of a graph that is used in spectral clustering to find the eigenvalues and eigenvectors. These eigenvectors are used to partition the graph into clusters.",
    'chapter_information': "Spectral Clustering"
}

lecture_spectral_clustering_mcq3 = {
    'question': "Why is the smallest eigenvalue of the graph Laplacian not useful for clustering?",
    'options_list': [
        'It does not provide any meaningful information',
        'It is always zero and corresponds to the trivial solution',
        'It represents the total number of nodes in the graph',
        'It leads to overfitting in clustering'
    ],
    'correct_answer': 'It is always zero and corresponds to the trivial solution',
    'explanation': "The smallest eigenvalue of the graph Laplacian is always zero and corresponds to a trivial solution (all components of the eigenvector are equal), which does not provide any useful information for clustering.",
    'chapter_information': "Spectral Clustering"
}

lecture_spectral_clustering_mcq4 = {
    'question': "What is the primary computational challenge in spectral clustering?",
    'options_list': [
        'Finding the eigenvalues and eigenvectors of the graph Laplacian',
        'Constructing the similarity matrix',
        'Normalizing the data points',
        'Visualizing the clusters'
    ],
    'correct_answer': 'Finding the eigenvalues and eigenvectors of the graph Laplacian',
    'explanation': "The primary computational challenge in spectral clustering is computing the eigenvalues and eigenvectors of the graph Laplacian, especially for large graphs.",
    'chapter_information': "Spectral Clustering"
}

lecture_spectral_clustering_mcq5 = {
    'question': "In spectral clustering, what does the relaxation of the integer constraints on the vector lead to?",
    'options_list': [
        'A more complex optimization problem',
        'An approximate but intuitive solution',
        'A solution with higher computational complexity',
        'A non-unique solution'
    ],
    'correct_answer': 'An approximate but intuitive solution',
    'explanation': "Relaxing the integer constraints on the vector in the optimization problem leads to an approximate but intuitive solution that is computationally feasible and provides meaningful clusters.",
    'chapter_information': "Spectral Clustering"
}

lecture_spectral_clustering_mcq6 = {
    'question': "What is the key property of the graph Laplacian that makes spectral clustering effective?",
    'options_list': [
        'It is always invertible',
        'It has non-negative eigenvalues',
        'It is a sparse matrix',
        'It can be easily decomposed'
    ],
    'correct_answer': 'It has non-negative eigenvalues',
    'explanation': "The graph Laplacian is a symmetric, positive semi-definite matrix, which means it has non-negative eigenvalues. This property is essential for the effectiveness of spectral clustering.",
    'chapter_information': "Spectral Clustering"
}

lecture_spectral_clustering_mcq7 = {
    'question': "What does the Fiedler vector (the eigenvector corresponding to the second smallest eigenvalue) represent in spectral clustering?",
    'options_list': [
        'The number of clusters in the graph',
        'The optimal partitioning of nodes into two clusters',
        'The distance between clusters',
        'The centrality of nodes in the graph'
    ],
    'correct_answer': 'The optimal partitioning of nodes into two clusters',
    'explanation': "The Fiedler vector is used to partition the graph into two clusters, with the sign and magnitude of its components indicating the cluster membership of each node.",
    'chapter_information': "Spectral Clustering"
}

lecture_spectral_clustering_mcq8 = {
    'question': "How can spectral clustering be used to find more than two clusters in a graph?",
    'options_list': [
        'By recursively applying the spectral clustering method to each cluster',
        'By using the third smallest eigenvalue instead of the second smallest',
        'By combining multiple eigenvectors to form a higher-dimensional embedding',
        'By increasing the number of iterations in the algorithm'
    ],
    'correct_answer': 'By combining multiple eigenvectors to form a higher-dimensional embedding',
    'explanation': "To find more than two clusters, spectral clustering can be extended by using the eigenvectors corresponding to the k smallest non-zero eigenvalues to form a higher-dimensional embedding of the nodes, which can then be clustered using standard techniques like k-means.",
    'chapter_information': "Spectral Clustering"
}


lecture_graphical_models_mcq1 = {
    'question': "What is one of the main reasons to study network models?",
    'options_list': [
        'To generate static representations of networks',
        'To understand the underlying generative process of networks',
        'To calculate the shortest path between nodes',
        'To increase the number of nodes in a network'
    ],
    'correct_answer': 'To understand the underlying generative process of networks',
    'explanation': "Studying network models helps to understand the generative process of networks and allows for hypothesis testing and identifying important properties in networks.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq2 = {
    'question': "In an Erdos-Rényi network model, what does the expected degree of a node depend on?",
    'options_list': [
        'The total number of edges in the network',
        'The probability of an edge between any two nodes and the number of nodes',
        'The clustering coefficient of the network',
        'The number of high-degree nodes'
    ],
    'correct_answer': 'The probability of an edge between any two nodes and the number of nodes',
    'explanation': "In an Erdos-Rényi network model, the expected degree of a node is given by (n-1) * p, where n is the number of nodes and p is the probability of an edge between any two nodes.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq3 = {
    'question': "Why does the Erdos-Rényi model not typically fit real-world network data?",
    'options_list': [
        'It generates networks with too many nodes',
        'It does not allow for varying edge probabilities',
        'It results in very small clustering coefficients and does not produce hub nodes',
        'It creates networks with a high clustering coefficient'
    ],
    'correct_answer': 'It results in very small clustering coefficients and does not produce hub nodes',
    'explanation': "The Erdos-Rényi model does not typically fit real-world network data because it results in very small clustering coefficients and does not produce hub nodes, which are common in real-world networks.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq4 = {
    'question': "What is the primary goal of the configuration model?",
    'options_list': [
        'To generate networks with a fixed number of nodes',
        'To produce networks with a specific degree distribution',
        'To create networks with high clustering coefficients',
        'To ensure all nodes are connected'
    ],
    'correct_answer': 'To produce networks with a specific degree distribution',
    'explanation': "The configuration model aims to generate networks with a specific degree distribution by fixing the degrees of nodes and connecting them randomly.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq5 = {
    'question': "How does the preferential attachment model ensure new nodes have a chance of being cited?",
    'options_list': [
        'By assigning new nodes a higher initial degree',
        'By connecting new nodes to all existing nodes',
        'By giving new nodes some initial probability of being cited',
        'By reducing the number of existing nodes'
    ],
    'correct_answer': 'By giving new nodes some initial probability of being cited',
    'explanation': "The preferential attachment model gives new nodes some initial probability of being cited, ensuring that even nodes with no citations have a chance of being linked to.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq6 = {
    'question': "What is a key property of the degree distribution in the preferential attachment model?",
    'options_list': [
        'It follows a binomial distribution',
        'It is uniform across all nodes',
        'It follows a power-law distribution',
        'It is normally distributed'
    ],
    'correct_answer': 'It follows a power-law distribution',
    'explanation': "In the preferential attachment model, the degree distribution follows a power-law distribution, meaning that some nodes become hubs with very high degrees while most nodes have relatively few connections.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq7 = {
    'question': "What is the clustering coefficient in an Erdos-Rényi graph?",
    'options_list': [
        'n',
        'p',
        '1/n',
        '1/p'
    ],
    'correct_answer': 'p',
    'explanation': "In an Erdos-Rényi graph, the clustering coefficient is equal to the probability p of an edge existing between any two nodes.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq8 = {
    'question': "What is a limitation of the configuration model?",
    'options_list': [
        'It cannot generate networks with a specific degree distribution',
        'It does not provide a generative model',
        'It requires high computational resources',
        'It only works for bipartite graphs'
    ],
    'correct_answer': 'It does not provide a generative model',
    'explanation': "The configuration model's limitation is that it does not provide a generative model, meaning it can create networks with specific degree distributions but cannot explain how the network was generated.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq1 = {
    'question': "What is one of the main reasons to study network models?",
    'options_list': [
        'To generate static representations of networks',
        'To understand the underlying generative process of networks',
        'To calculate the shortest path between nodes',
        'To increase the number of nodes in a network'
    ],
    'correct_answer': 'To understand the underlying generative process of networks',
    'explanation': "Studying network models helps to understand the generative process of networks and allows for hypothesis testing and identifying important properties in networks.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq2 = {
    'question': "In an Erdos-Rényi network model, what does the expected degree of a node depend on?",
    'options_list': [
        'The total number of edges in the network',
        'The probability of an edge between any two nodes and the number of nodes',
        'The clustering coefficient of the network',
        'The number of high-degree nodes'
    ],
    'correct_answer': 'The probability of an edge between any two nodes and the number of nodes',
    'explanation': "In an Erdos-Rényi network model, the expected degree of a node is given by (n-1) * p, where n is the number of nodes and p is the probability of an edge between any two nodes.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq3 = {
    'question': "Why does the Erdos-Rényi model not typically fit real-world network data?",
    'options_list': [
        'It generates networks with too many nodes',
        'It does not allow for varying edge probabilities',
        'It results in very small clustering coefficients and does not produce hub nodes',
        'It creates networks with a high clustering coefficient'
    ],
    'correct_answer': 'It results in very small clustering coefficients and does not produce hub nodes',
    'explanation': "The Erdos-Rényi model does not typically fit real-world network data because it results in very small clustering coefficients and does not produce hub nodes, which are common in real-world networks.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq4 = {
    'question': "What is the primary goal of the configuration model?",
    'options_list': [
        'To generate networks with a fixed number of nodes',
        'To produce networks with a specific degree distribution',
        'To create networks with high clustering coefficients',
        'To ensure all nodes are connected'
    ],
    'correct_answer': 'To produce networks with a specific degree distribution',
    'explanation': "The configuration model aims to generate networks with a specific degree distribution by fixing the degrees of nodes and connecting them randomly.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq5 = {
    'question': "How does the preferential attachment model ensure new nodes have a chance of being cited?",
    'options_list': [
        'By assigning new nodes a higher initial degree',
        'By connecting new nodes to all existing nodes',
        'By giving new nodes some initial probability of being cited',
        'By reducing the number of existing nodes'
    ],
    'correct_answer': 'By giving new nodes some initial probability of being cited',
    'explanation': "The preferential attachment model gives new nodes some initial probability of being cited, ensuring that even nodes with no citations have a chance of being linked to.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq6 = {
    'question': "What is a key property of the degree distribution in the preferential attachment model?",
    'options_list': [
        'It follows a binomial distribution',
        'It is uniform across all nodes',
        'It follows a power-law distribution',
        'It is normally distributed'
    ],
    'correct_answer': 'It follows a power-law distribution',
    'explanation': "In the preferential attachment model, the degree distribution follows a power-law distribution, meaning that some nodes become hubs with very high degrees while most nodes have relatively few connections.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq7 = {
    'question': "What is the clustering coefficient in an Erdos-Rényi graph?",
    'options_list': [
        'n',
        'p',
        '1/n',
        '1/p'
    ],
    'correct_answer': 'p',
    'explanation': "In an Erdos-Rényi graph, the clustering coefficient is equal to the probability p of an edge existing between any two nodes.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq1 = {
    'question': "What is the main limitation of the Erdos-Rényi model when applied to real-world networks?",
    'options_list': [
        'It generates networks with too many edges',
        'It does not allow for varying node degrees',
        'It results in very small clustering coefficients and lacks a power-law degree distribution',
        'It creates networks with a high clustering coefficient'
    ],
    'correct_answer': 'It results in very small clustering coefficients and lacks a power-law degree distribution',
    'explanation': "The Erdos-Rényi model does not typically fit real-world network data because it results in very small clustering coefficients and lacks a power-law degree distribution, which are common in real-world networks.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq2 = {
    'question': "How does the configuration model generate networks with a specific degree distribution?",
    'options_list': [
        'By randomly connecting nodes until a desired degree distribution is achieved',
        'By fixing the degrees of nodes and connecting them randomly',
        'By using a probabilistic method to add edges between nodes',
        'By iteratively removing and adding edges to fit the distribution'
    ],
    'correct_answer': 'By fixing the degrees of nodes and connecting them randomly',
    'explanation': "The configuration model generates networks with a specific degree distribution by fixing the degrees of nodes and then connecting them randomly.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq3 = {
    'question': "What is the purpose of the preferential attachment model in network theory?",
    'options_list': [
        'To generate networks with a high clustering coefficient',
        'To ensure that all nodes have the same degree',
        'To create networks where the probability of a node being connected is proportional to its degree',
        'To model networks with a low average path length'
    ],
    'correct_answer': 'To create networks where the probability of a node being connected is proportional to its degree',
    'explanation': "The preferential attachment model is used to create networks where the probability of a node being connected is proportional to its degree, which helps in generating networks with a power-law degree distribution.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq4 = {
    'question': "How can the small-world property be introduced into a network?",
    'options_list': [
        'By ensuring all nodes have the same degree',
        'By adding a few random long-distance edges to a regular network',
        'By increasing the clustering coefficient of the network',
        'By using a purely random connection model'
    ],
    'correct_answer': 'By adding a few random long-distance edges to a regular network',
    'explanation': "The small-world property can be introduced into a network by adding a few random long-distance edges to a regular network, which reduces the average path length while maintaining a high clustering coefficient.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq5 = {
    'question': "What is a drawback of the configuration model?",
    'options_list': [
        'It does not generate networks with a power-law degree distribution',
        'It often creates networks with self-loops and multiple edges',
        'It results in networks with too high clustering coefficients',
        'It cannot produce networks with a given degree distribution'
    ],
    'correct_answer': 'It often creates networks with self-loops and multiple edges',
    'explanation': "A drawback of the configuration model is that it can often create networks with self-loops and multiple edges, which need to be removed in larger graphs.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq6 = {
    'question': "What type of network model would be best suited for generating networks with high clustering coefficients?",
    'options_list': [
        'Erdos-Rényi model',
        'Configuration model',
        'Small-world model',
        'Preferential attachment model'
    ],
    'correct_answer': 'Small-world model',
    'explanation': "The small-world model is best suited for generating networks with high clustering coefficients and small diameters, which are common in real-world networks.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq7 = {
    'question': "What is a common feature of networks generated by the preferential attachment model?",
    'options_list': [
        'High clustering coefficient',
        'Acyclic structure',
        'Power-law degree distribution',
        'Uniform degree distribution'
    ],
    'correct_answer': 'Power-law degree distribution',
    'explanation': "Networks generated by the preferential attachment model commonly feature a power-law degree distribution, meaning that some nodes become hubs with very high degrees while most nodes have relatively few connections.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq8 = {
    'question': "What is one advantage of the configuration model over the Erdos-Rényi model?",
    'options_list': [
        'It can produce networks with a specific degree distribution',
        'It always generates networks with high clustering coefficients',
        'It is easier to implement computationally',
        'It ensures all nodes have the same degree'
    ],
    'correct_answer': 'It can produce networks with a specific degree distribution',
    'explanation': "One advantage of the configuration model over the Erdos-Rényi model is that it can produce networks with a specific degree distribution, including power-law degree distributions.",
    'chapter_information': "Introduction to Network Models"
}


lecture_graphical_models_mcq1 = {
    'question': "What is the primary characteristic of Price's model in network theory?",
    'options_list': [
        'It generates networks with high clustering coefficients',
        'It ensures uniform degree distribution among nodes',
        'It uses a preferential attachment mechanism for node connections',
        'It models networks as complete graphs'
    ],
    'correct_answer': 'It uses a preferential attachment mechanism for node connections',
    'explanation': "Price's model uses a preferential attachment mechanism, where new nodes are more likely to connect to already well-connected nodes, resulting in a 'rich get richer' effect.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq2 = {
    'question': "How does Price's model ensure that new nodes can be connected to existing nodes despite having zero in-degree?",
    'options_list': [
        'By connecting new nodes randomly to any existing nodes',
        'By assigning a minimum in-degree to each new node',
        'By using the in-degree plus a constant in the connection probability',
        'By connecting new nodes to a fixed number of existing nodes'
    ],
    'correct_answer': 'By using the in-degree plus a constant in the connection probability',
    'explanation': "In Price's model, new nodes are connected to existing nodes based on the in-degree plus a constant to ensure that even nodes with zero in-degree can be connected.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq3 = {
    'question': "What type of graph is created when each node in a circulant graph is connected to all other nodes (k = n-1)?",
    'options_list': [
        'Cycle graph',
        'Complete graph',
        'Bipartite graph',
        'Tree graph'
    ],
    'correct_answer': 'Complete graph',
    'explanation': "When each node in a circulant graph is connected to all other nodes (k = n-1), the result is a complete graph.",
    'chapter_information': "Circulant Graphs"
}

lecture_graphical_models_mcq4 = {
    'question': "How does adding 'short circuits' to a circulant graph affect its properties?",
    'options_list': [
        'It increases the clustering coefficient',
        'It reduces the diameter of the graph',
        'It ensures all nodes have the same degree',
        'It converts the graph into a bipartite graph'
    ],
    'correct_answer': 'It reduces the diameter of the graph',
    'explanation': "Adding 'short circuits' (rewiring a few edges randomly) to a circulant graph drastically reduces its diameter, making it a small-world model while largely preserving the clustering coefficient.",
    'chapter_information': "Small-World Models"
}

lecture_graphical_models_mcq5 = {
    'question': "What is the disadvantage of the small-world model with regard to its degree distribution?",
    'options_list': [
        'It does not allow for high clustering coefficients',
        'It results in a uniform degree distribution',
        'It fails to replicate a power-law degree distribution',
        'It increases the diameter of the graph'
    ],
    'correct_answer': 'It fails to replicate a power-law degree distribution',
    'explanation': "The small-world model, while achieving small diameters and high clustering coefficients, does not replicate a power-law degree distribution, which is often observed in natural networks.",
    'chapter_information': "Small-World Models"
}

lecture_graphical_models_mcq6 = {
    'question': "In Price's model, what effect does the 'rich get richer' mechanism have on the network's degree distribution?",
    'options_list': [
        'It leads to a uniform degree distribution',
        'It results in a power-law degree distribution',
        'It increases the network\'s diameter',
        'It decreases the clustering coefficient'
    ],
    'correct_answer': 'It results in a power-law degree distribution',
    'explanation': "The 'rich get richer' mechanism in Price's model results in a power-law degree distribution, where a few nodes become highly connected while most nodes have fewer connections.",
    'chapter_information': "Introduction to Network Models"
}

lecture_graphical_models_mcq7 = {
    'question': "What is a circulant graph?",
    'options_list': [
        'A graph where nodes are connected in a circular manner with a fixed number of nearest neighbors',
        'A graph where every node is connected to every other node',
        'A graph where nodes are connected randomly',
        'A bipartite graph with two disjoint sets of nodes'
    ],
    'correct_answer': 'A graph where nodes are connected in a circular manner with a fixed number of nearest neighbors',
    'explanation': "A circulant graph is one where nodes are arranged in a circle and each node is connected to a fixed number of its nearest neighbors.",
    'chapter_information': "Circulant Graphs"
}

lecture_graphical_models_mcq8 = {
    'question': "Why do small-world models with rewired edges often still have high clustering coefficients?",
    'options_list': [
        'Because the rewiring process adds more local edges',
        'Because only a few edges are rewired, preserving the original local structures',
        'Because the nodes are connected in a circular manner',
        'Because the model inherently increases the clustering coefficient with each rewire'
    ],
    'correct_answer': 'Because only a few edges are rewired, preserving the original local structures',
    'explanation': "In small-world models, only a few edges are rewired, which preserves the original local structures and high clustering coefficients while reducing the overall diameter of the graph.",
    'chapter_information': "Small-World Models"
}






COURSE_MPC_QUESTIONS = []
global_items = list(globals().items())
# print(global_items)

for name, value in global_items:
    if not name.startswith('_'):
        COURSE_MPC_QUESTIONS.append(value)

COURSE_MPC_QUESTIONS = COURSE_MPC_QUESTIONS[:-1]