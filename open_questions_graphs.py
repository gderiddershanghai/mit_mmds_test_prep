newman_networks_c6_q1 = {
    'question': "Define a network (or graph) and list the different terminologies used for vertices and edges in various fields (e.g., computer science, physics, sociology).",
    'correct_answer': "A network (or graph) is a collection of vertices joined by edges. Vertices and edges are also called nodes and links in computer science, sites and bonds in physics, and actors and ties in sociology.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q2 = {
    'question': "What is a simple network or simple graph? How does it differ from a multigraph?",
    'correct_answer': "A simple network or simple graph is a network with no self-edges (self-loops) and no multiedges. A multigraph, on the other hand, can have multiple edges between the same pair of vertices.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q3 = {
    'question': "Explain the terms self-edges or self-loops, and multiedges.",
    'correct_answer': "Self-edges or self-loops are edges that connect a vertex to itself. Multiedges are multiple edges between the same pair of vertices.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q4 = {
    'question': "How is an adjacency matrix defined for a simple graph? What are its properties?",
    'correct_answer': "An adjacency matrix for a simple graph is a matrix with elements Aij such that Aij = 1 if there is an edge between vertices i and j, and 0 otherwise. Its properties include being symmetric for undirected graphs and having zeroes on the diagonal for graphs with no self-loops.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q5 = {
    'question': "Given a simple graph with vertices 1 through 4 and edges (1,2), (2,3), and (3,4), write down its adjacency matrix.",
    'correct_answer': "The adjacency matrix for this graph is:\n[ [0, 1, 0, 0],\n  [1, 0, 1, 0],\n  [0, 1, 0, 1],\n  [0, 0, 1, 0] ]",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q6 = {
    'question': "How would you represent multiedges and self-edges in an adjacency matrix?",
    'correct_answer': "Multiedges are represented by setting the corresponding matrix element Aij equal to the multiplicity of the edge. Self-edges are represented by setting the diagonal element Aii to 2 for a single self-edge, since each self-edge contributes two ends connected to the same vertex.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q7 = {
    'question': "What distinguishes a weighted network from a simple on/off connection network?",
    'correct_answer': "In a weighted network, edges have a strength, weight, or value associated with them, typically represented by real numbers. This contrasts with a simple on/off connection network, where edges are either present or absent without any additional value.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q8 = {
    'question': "Explain how weights are represented in the adjacency matrix of a weighted network.",
    'correct_answer': "In a weighted network, the elements of the adjacency matrix are equal to the weights of the corresponding connections. For example, if the connection between vertices 1 and 2 has a weight of 3, then A[1][2] = 3.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q9 = {
    'question': "Provide an example of a weighted network and its corresponding adjacency matrix.",
    'correct_answer': "Example: A network with vertices 1, 2, and 3, and edges (1,2) with weight 2, (1,3) with weight 1, and (2,3) with weight 4. The adjacency matrix is:\n[ [0, 2, 1],\n  [2, 0, 4],\n  [1, 4, 0] ]",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q10 = {
    'question': "What is a directed network or digraph? How is it represented visually and mathematically?",
    'correct_answer': "A directed network or digraph is a network in which each edge has a direction, pointing from one vertex to another. It is visually represented by arrows on the edges, indicating the direction. Mathematically, it is represented by an adjacency matrix where Aij = 1 if there is an edge from vertex j to vertex i.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q11 = {
    'question': "Describe the concept of cocitation and bibliographic coupling in directed networks.",
    'correct_answer': "Cocitation of two vertices is the number of vertices that have outgoing edges pointing to both of them. Bibliographic coupling is the number of vertices to which both vertices have outgoing edges. Both measures are used to analyze the structure of citation networks.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q12 = {
    'question': "How can a directed network be transformed into an undirected one for analysis purposes?",
    'correct_answer': "One way is to ignore the edge directions, effectively treating the directed edges as undirected. Another approach is to use cocitation or bibliographic coupling to create an undirected network based on the relationships indicated by the directed edges.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q13 = {
    'question': "Define cocitation and bibliographic coupling in the context of citation networks.",
    'correct_answer': "Cocitation refers to the number of other vertices that cite both of two given vertices. Bibliographic coupling refers to the number of other vertices that are cited by both of two given vertices. Both are used to measure the relatedness of papers in citation networks.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q14 = {
    'question': "How are cocitation and bibliographic coupling matrices constructed?",
    'correct_answer': "The cocitation matrix C is constructed with elements Cij = sum(Aik * Ajk) for all k, where A is the adjacency matrix of the directed network. The bibliographic coupling matrix B is constructed with elements Bij = sum(Aki * Akj) for all k.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q15 = {
    'question': "What is a hypergraph and how does it differ from a simple graph?",
    'correct_answer': "A hypergraph is a network where edges, called hyperedges, can join more than two vertices at a time. This differs from a simple graph where each edge connects exactly two vertices.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q16 = {
    'question': "Provide an example of a hypergraph and describe its hyperedges.",
    'correct_answer': "Example: A social network representing families. A hyperedge might connect all members of a family together, representing their familial relationship.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q17 = {
    'question': "What is a bipartite network and how can it be represented?",
    'correct_answer': "A bipartite network is a network with two distinct types of vertices, where edges only connect vertices of different types. It can be represented by an incidence matrix, where rows represent one type of vertex and columns represent the other type, with elements indicating edges.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q18 = {
    'question': "Describe the incidence matrix for a bipartite network.",
    'correct_answer': "The incidence matrix B of a bipartite network is a rectangular matrix where Bij = 1 if vertex i of type 1 is connected to vertex j of type 2, and 0 otherwise.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q19 = {
    'question': "Explain how a bipartite network can be projected onto a one-mode network.",
    'correct_answer': "A bipartite network can be projected onto a one-mode network by creating edges between vertices of the same type that share a common neighbor in the original bipartite network. The adjacency matrix of the one-mode projection can be calculated as B.T * B, where B is the incidence matrix.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q20 = {
    'question': "Define a tree and explain its key properties.",
    'correct_answer': "A tree is a connected, undirected network with no closed loops. Key properties include having exactly one path between any pair of vertices and having n-1 edges for n vertices.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q21 = {
    'question': "What is a rooted tree and what are leaves in this context?",
    'correct_answer': "A rooted tree is a tree in which one vertex is designated as the root. Leaves are the vertices with degree one, representing the endpoints of branches.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q22 = {
    'question': "Why are trees important in the study of networks?",
    'correct_answer': "Trees are important because they provide a simplified model of network structure, are used in various algorithms, and represent hierarchical relationships in many types of networks.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q23 = {
    'question': "What is a planar network? Provide an example.",
    'correct_answer': "A planar network is a network that can be drawn on a plane without any edges crossing. An example is a triangle or square.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q24 = {
    'question': "Explain the four-color theorem in relation to planar graphs.",
    'correct_answer': "The four-color theorem states that any planar graph can be colored with no more than four colors such that no two adjacent vertices share the same color.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q25 = {
    'question': "What is Kuratowski's theorem and how does it help in determining the planarity of a network?",
    'correct_answer': "Kuratowski's theorem states that a graph is planar if and only if it does not contain a subgraph that is a subdivision of either the complete graph K5 or the complete bipartite graph K3,3. This helps in determining whether a network can be drawn without edge crossings.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q26 = {
    'question': "Define the degree of a vertex in a graph. How is it calculated?",
    'correct_answer': "The degree of a vertex is the number of edges connected to it. It is calculated by counting the number of edges that have the vertex as an endpoint.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q27 = {
    'question': "What is the mean degree of a network?",
    'correct_answer': "The mean degree of a network is the average number of edges per vertex, calculated as the total number of edges multiplied by 2 (since each edge connects two vertices) divided by the total number of vertices.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q28 = {
    'question': "How do in-degree and out-degree differ in directed networks?",
    'correct_answer': "In directed networks, the in-degree of a vertex is the number of incoming edges, while the out-degree is the number of outgoing edges.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q29 = {
    'question': "What is a path in a network? Describe its length.",
    'correct_answer': "A path in a network is a sequence of edges that connect a sequence of vertices without repeating any edges. The length of the path is the number of edges in the sequence.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q30 = {
    'question': "Explain the concept of a geodesic path and how it differs from a general path.",
    'correct_answer': "A geodesic path is the shortest path between two vertices. It differs from a general path in that it has the minimum possible length.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q31 = {
    'question': "What are Eulerian and Hamiltonian paths? Provide an example of each.",
    'correct_answer': "An Eulerian path visits every edge of a graph exactly once. A Hamiltonian path visits every vertex exactly once. Example: For a triangle, an Eulerian path is any path that traverses all three edges once, while a Hamiltonian path is any path that visits all three vertices once.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q32 = {
    'question': "Define a component in the context of a network.",
    'correct_answer': "A component is a maximal subgraph in which any two vertices are connected by a path, and which is connected to no additional vertices in the rest of the graph.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q33 = {
    'question': "What is the difference between a strongly connected component and a weakly connected component in directed networks?",
    'correct_answer': "A strongly connected component is a subgraph in which every vertex is reachable from every other vertex via directed paths. A weakly connected component is a subgraph that becomes connected when all edges are treated as undirected.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q34 = {
    'question': "Explain the concept of edge-independent and vertex-independent paths.",
    'correct_answer': "Edge-independent paths between two vertices do not share any edges, while vertex-independent paths do not share any vertices except the start and end vertices.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q35 = {
    'question': "What is the connectivity of a pair of vertices?",
    'correct_answer': "The connectivity of a pair of vertices is the minimum number of vertices (vertex connectivity) or edges (edge connectivity) that need to be removed to disconnect the two vertices.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q36 = {
    'question': "Describe what a cut set is and the significance of Menger's theorem.",
    'correct_answer': "A cut set is a set of vertices or edges whose removal increases the number of connected components of the graph. Menger's theorem states that the minimum number of vertices/edges required to separate two non-adjacent vertices equals the maximum number of vertex-independent/edge-independent paths between them.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q37 = {
    'question': "Define the graph Laplacian and explain its role in the study of networks.",
    'correct_answer': "The graph Laplacian is defined as L = D - A, where D is the degree matrix and A is the adjacency matrix. It plays a key role in network analysis, particularly in studying network dynamics, diffusion processes, and spectral clustering.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q38 = {
    'question': "What are the eigenvalues of the graph Laplacian and what do they indicate about the network?",
    'correct_answer': "The eigenvalues of the graph Laplacian provide insights into the network's structure. The smallest eigenvalue is always zero, and the second smallest eigenvalue (algebraic connectivity) indicates the connectivity of the network. A larger gap between the smallest and the second smallest eigenvalues signifies a well-connected network.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q39 = {
    'question': "What is a random walk in the context of a network?",
    'correct_answer': "A random walk in a network is a process where a walker moves from one vertex to another, randomly choosing an edge at each step. It is used to model various processes, such as diffusion, exploration, and sampling.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q40 = {
    'question': "Explain the concept of first passage time in random walks.",
    'correct_answer': "First passage time is the expected number of steps required for a random walker to reach a specified vertex for the first time. It is an important measure in understanding the behavior of random walks in networks.",
    'chapter_information': "Newman Networks Chapter 6"
}

newman_networks_c6_q41 = {
    'question': "Describe the relationship between random walks and resistor networks.",
    'correct_answer': "Random walks and resistor networks are mathematically related. The effective resistance between two nodes in a resistor network is proportional to the expected time for a random walk starting at one node to reach the other. This relationship provides insights into network connectivity and robustness.",
    'chapter_information': "Newman Networks Chapter 6"
}

#################
newman_networks_c7_oe1 = {
    'question': "Discuss the concept of degree centrality and explain its significance in social networks. How can it be used to measure the influence of individuals within the network?",
    'correct_answer': "Degree centrality refers to the number of edges connected to a vertex. In social networks, it is often used to measure the influence of individuals, as those with higher degree centrality may have more connections, greater access to information, and higher prestige. It is particularly useful for identifying key individuals who can spread information or influence others within the network.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe2 = {
    'question': "Explain the concept of eigenvector centrality. How does it differ from degree centrality, and why might it be more informative in some network analyses?",
    'correct_answer': "Eigenvector centrality extends the concept of degree centrality by considering not just the number of connections a vertex has, but also the importance of its neighbors. A vertex's eigenvector centrality is proportional to the sum of the centralities of its neighbors, making it more informative in scenarios where connections to influential vertices are important. This measure can highlight nodes that are not only well-connected but also connected to other central and influential nodes.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe3 = {
    'question': "Describe Katz centrality and how it addresses the limitations of eigenvector centrality in directed networks. What are the key parameters involved in Katz centrality, and how do they influence the measure?",
    'correct_answer': "Katz centrality adds a small constant to the eigenvector centrality calculation, ensuring that vertices with no incoming edges still have some centrality. This addresses the issue in directed networks where vertices with no in-degrees would otherwise have zero centrality. The key parameters in Katz centrality are α and β, where α scales the contribution from the neighbors' centralities and β provides a base level of centrality to all vertices. The choice of these parameters influences the balance between network structure and intrinsic importance assigned to each vertex.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe4 = {
    'question': "What is PageRank and how does it improve upon Katz centrality? Discuss its application in web search engines and the significance of the damping factor.",
    'correct_answer': "PageRank is a variation of Katz centrality that divides the contribution from each vertex by its out-degree, preventing vertices with many outbound links from disproportionately influencing others. It is widely used in web search engines like Google to rank web pages based on their importance. The damping factor, typically set around 0.85, ensures that the calculation considers both the network structure and a probability of random surfing, balancing the contributions from direct links and the overall connectivity of the network.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe5 = {
    'question': "Discuss the concepts of hubs and authorities as proposed by the HITS algorithm. How are these centrality measures calculated, and what types of networks benefit most from this approach?",
    'correct_answer': "The HITS algorithm distinguishes between two types of centrality in directed networks: hubs and authorities. Hubs are vertices that point to many authoritative nodes, while authorities are vertices pointed to by many hubs. The algorithm calculates hub and authority centralities iteratively, with hub centrality being proportional to the sum of the authority centralities of the vertices it points to, and authority centrality being proportional to the sum of the hub centralities of the vertices pointing to it. This approach is particularly beneficial for networks like citation networks and the web, where distinguishing between sources of information and directories of information is important.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe6 = {
    'question': "Explain the concept of closeness centrality and its application in network analysis. What are its limitations and how can they be addressed?",
    'correct_answer': "Closeness centrality measures how close a vertex is to all other vertices in the network, defined as the inverse of the average shortest path distance from the vertex to all others. It is used to identify vertices that can quickly interact with all others. However, its values tend to have a small dynamic range, making it difficult to distinguish between vertices. Additionally, it becomes infinite in networks with multiple components. These limitations can be addressed by using the harmonic mean distance for better differentiation and ensuring finite values in disconnected networks.",
    'chapter_information': "Newman Networks Chapter 7"
}


newman_networks_c7_oe1x = {
    'question': "Explain the concept of betweenness centrality and how it differs from other centrality measures. Why might vertices with high betweenness centrality hold significant influence within a network?",
    'correct_answer': "Betweenness centrality measures the extent to which a vertex lies on the shortest paths between other vertices. It differs from other centrality measures such as degree, closeness, and eigenvector centrality by focusing on a vertex's role in facilitating communication within the network. Vertices with high betweenness centrality can hold significant influence because they control the flow of information between other vertices, making them critical for connectivity and communication.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe2x = {
    'question': "Given a network, how do you mathematically define the betweenness centrality of a vertex? What does the notation δst(i) represent in the context of betweenness centrality?",
    'correct_answer': "Betweenness centrality of a vertex is defined as the sum of the fraction of all-pairs shortest paths that pass through that vertex. Mathematically, it is expressed as: BC(i) = ∑(s ≠ i ≠ t) (σst(i) / σst), where σst is the total number of shortest paths from vertex s to vertex t, and σst(i) is the number of those paths that pass through vertex i. The notation δst(i) represents the fraction of shortest paths between vertices s and t that pass through vertex i.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe3x = {
    'question': "What is a geodesic path, and how does it relate to the calculation of betweenness centrality? Why do we count each geodesic path twice in an undirected network?",
    'correct_answer': "A geodesic path is the shortest path between two vertices in a network. In the calculation of betweenness centrality, geodesic paths are used to determine how often a vertex appears on these shortest paths. In an undirected network, each geodesic path is counted twice because the path from vertex u to vertex v is the same as the path from vertex v to vertex u, ensuring that each direction is accounted for in the centrality measure.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe4x = {
    'question': "Describe a scenario in which a vertex with high betweenness centrality could disrupt network communication if removed. How can high betweenness centrality impact the flow of information in a social network?",
    'correct_answer': "In a network where a vertex with high betweenness centrality is a crucial bridge between different groups, its removal can disrupt communication between these groups. For example, in a social network, if a person who connects two otherwise separate friend groups is removed, the flow of information between these groups could be significantly hindered. High betweenness centrality impacts information flow by highlighting individuals who act as critical intermediaries, facilitating the spread of information across the network.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe5x = {
    'question': "How is the calculation of betweenness centrality adjusted for directed networks? Why is it important to consider the direction of paths in directed networks when calculating betweenness centrality?",
    'correct_answer': "In directed networks, betweenness centrality is calculated by considering the direction of the shortest paths. The measure accounts for the directed nature of edges, meaning that the shortest path from vertex u to vertex v may differ from the path from v to u. It is important to consider the direction of paths because in directed networks, the influence and flow of information can be asymmetric, and paths need to be accurately represented to measure centrality correctly.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe6x = {
    'question': "Discuss potential applications of betweenness centrality in real-world networks (e.g., social networks, the Internet). How might businesses use betweenness centrality to identify key influencers in a social network?",
    'correct_answer': "Betweenness centrality can be applied to identify key nodes in various real-world networks. In social networks, it helps to pinpoint influential individuals who control information flow. On the Internet, it can identify critical routers or servers that manage data traffic. Businesses can use betweenness centrality to identify key influencers who can effectively spread marketing messages or gather valuable information from different social circles, thereby optimizing their marketing and networking strategies.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe7x = {
    'question': "Explain why it might be useful to normalize betweenness centrality values. Describe a method for normalizing betweenness centrality.",
    'correct_answer': "Normalizing betweenness centrality values is useful because it allows for comparison between vertices in different networks or of different sizes. One method for normalizing betweenness centrality is to divide the betweenness centrality of each vertex by the maximum possible betweenness centrality in the network. For an undirected network, this maximum value is (n-1)(n-2)/2 for a vertex, where n is the number of vertices in the network.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe8x = {
    'question': "Compare and contrast betweenness centrality with degree centrality, closeness centrality, and eigenvector centrality. In what types of networks might betweenness centrality provide more insightful information than other centrality measures?",
    'correct_answer': "Degree centrality measures the number of direct connections a vertex has. Closeness centrality measures how close a vertex is to all other vertices in terms of the shortest paths. Eigenvector centrality considers the influence of a vertex based on the centrality of its neighbors. Betweenness centrality, however, measures a vertex's role in facilitating communication by lying on shortest paths between other vertices. Betweenness centrality provides more insightful information in networks where intermediaries are critical for communication, such as transportation networks or social networks with distinct communities.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe9x = {
    'question': "What are some common algorithms used to calculate betweenness centrality in large networks? Discuss the computational complexity of calculating betweenness centrality and how it affects the feasibility of its use in large-scale networks.",
    'correct_answer': "Common algorithms for calculating betweenness centrality include Brandes' algorithm, which efficiently computes betweenness centrality using a combination of breadth-first search (for unweighted graphs) or Dijkstra's algorithm (for weighted graphs). The computational complexity of Brandes' algorithm is O(nm) for unweighted graphs and O(nm + n^2 log n) for weighted graphs, where n is the number of vertices and m is the number of edges. This complexity can make the calculation of betweenness centrality infeasible for extremely large-scale networks, requiring the use of approximate methods or parallel computing techniques.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe10x = {
    'question': "How does the addition or removal of edges or vertices in a network impact the betweenness centrality of other vertices? Provide an example of how a network's structure can change the betweenness centrality of specific vertices.",
    'correct_answer': "The addition or removal of edges or vertices can significantly impact the betweenness centrality of other vertices by altering the shortest paths in the network. For example, adding a new edge that provides a shorter path between two vertices can reduce the betweenness centrality of vertices that previously facilitated the shortest connection. Conversely, removing a key vertex or edge can increase the betweenness centrality of other vertices as they become new intermediaries. For instance, in a network where vertex B connects two clusters, removing B would increase the betweenness of any new intermediary vertices connecting the clusters.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe11 = {
    'question': "Consider a small network with vertices A, B, C, D, and E connected as follows: A-B, A-C, B-D, C-D, D-E. Calculate the betweenness centrality for each vertex. Interpret the results of your calculation in the context of the network's structure.",
    'correct_answer': "Calculating betweenness centrality: A = 0, B = 4, C = 4, D = 6, E = 0. Interpretation: Vertex D has the highest betweenness centrality because it lies on the shortest paths connecting most pairs of vertices, acting as a critical bridge within the network. Vertices B and C have moderate betweenness as they also serve as intermediaries but less frequently than D. Vertices A and E have the lowest betweenness centrality, indicating they are peripheral nodes with less influence over the network's communication paths.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe12 = {
    'question': "How does betweenness centrality differ when applied to directed networks compared to undirected networks? Why might betweenness centrality be less commonly used for directed networks?",
    'correct_answer': "In directed networks, betweenness centrality considers the direction of edges when calculating shortest paths, meaning the shortest path from vertex u to vertex v can differ from the path from v to u. This can make the calculation more complex and nuanced. Betweenness centrality might be less commonly used for directed networks because directed paths can introduce asymmetry and complications that make interpretation and calculation more difficult compared to undirected networks.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe13 = {
    'question': "What are some limitations and criticisms of using betweenness centrality as a measure of influence in networks? Discuss scenarios where betweenness centrality might not be a reliable indicator of a vertex's importance.",
    'correct_answer': "Limitations of betweenness centrality include its sensitivity to network size and structure changes, its computational intensity for large networks, and its assumption that shortest paths are the primary routes for information flow. Betweenness centrality might not be reliable in scenarios where information or influence spreads through multiple paths or where network dynamics are rapid and constantly changing. Additionally, in networks with many redundant paths, betweenness centrality might overestimate the importance of vertices that have alternative routes.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe14 = {
    'question': "Describe the concept of flow betweenness and how it extends the idea of betweenness centrality. How does random-walk betweenness differ from standard betweenness centrality?",
    'correct_answer': "Flow betweenness extends betweenness centrality by considering the maximum possible flow through a vertex when multiple paths can be used simultaneously, rather than only the shortest paths. It accounts for all independent paths between vertex pairs. Random-walk betweenness, on the other hand, measures the betweenness based on the number of times a random walk from one vertex to another passes through a given vertex. Unlike standard betweenness, it includes all possible paths weighted by their likelihood in a random walk, providing a more comprehensive measure of a vertex's role in the network.",
    'chapter_information': "Newman Networks Chapter 7"
}

newman_networks_c7_oe15 = {
    'question': "How can betweenness centrality be used to assess the resilience of a network? Discuss the implications of high betweenness centrality vertices in terms of network vulnerability and robustness.",
    'correct_answer': "Betweenness centrality can be used to assess network resilience by identifying critical vertices whose removal would disrupt the shortest paths between other vertices, indicating potential vulnerabilities. High betweenness centrality vertices imply that these vertices are crucial for maintaining connectivity and communication within the network. Their removal could lead to significant fragmentation, making the network less robust and more susceptible to targeted attacks or failures. Identifying such vertices helps in strengthening network resilience by adding redundancy or protection around these critical points.",
    'chapter_information': "Newman Networks Chapter 7"
}
##############################
newman_networks_c8_oe1 = {
    'question': "Discuss the significance of the 'giant component' in undirected networks. How does it typically manifest in real-world networks, and what are some examples of networks where this phenomenon is observed?",
    'correct_answer': "The 'giant component' refers to the largest connected subgraph within an undirected network, often encompassing a significant majority of the network's vertices. This phenomenon typically manifests in real-world networks where a majority of nodes are interconnected, such as the network of film actors where most actors are connected through co-appearances in films. Other examples include the Internet, where most nodes (websites) are connected through hyperlinks, and social networks, where most users are connected through friendships or acquaintances.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_oe2 = {
    'question': "Explain the concept of 'small-world effect' in networks. What implications does this effect have for the dynamics of networked systems, such as information spread or communication efficiency?",
    'correct_answer': "The 'small-world effect' refers to the observation that the average path length between nodes in many networks is surprisingly short. This effect implies that information or diseases can spread rapidly across the network, and communication is highly efficient. For example, in social networks, the 'six degrees of separation' phenomenon illustrates how individuals are connected through a short chain of acquaintances, facilitating quick dissemination of information.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_oe3 = {
    'question': "Describe the power-law degree distribution observed in many real-world networks. Why are networks with this type of distribution referred to as 'scale-free,' and what are the implications of this characteristic for the structure and behavior of the network?",
    'correct_answer': "Power-law degree distributions are characterized by a small number of nodes (hubs) with a very high degree and a large number of nodes with a low degree. Networks with this distribution are called 'scale-free' because the relative distribution remains constant regardless of the network size. This characteristic implies robustness against random failures, as most nodes have few connections, but vulnerability to targeted attacks on hubs. Examples include the World Wide Web and certain biological networks.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_oe4 = {
    'question': "Analyze the role of clustering coefficients in understanding network structure. How do clustering coefficients differ between random networks and real-world networks, and what might account for these differences?",
    'correct_answer': "Clustering coefficients measure the likelihood that two neighbors of a node are also neighbors with each other, indicating the presence of tightly knit groups. In random networks, clustering coefficients tend to be low and decrease as the network size increases. However, real-world networks often exhibit high clustering coefficients, suggesting the presence of community structures or social circles. Factors such as triadic closure, where two people with a mutual friend are likely to become friends themselves, can account for these differences.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_oe5 = {
    'question': "Evaluate the impact of assortative mixing by degree on the structure and dynamics of networks. How does assortative mixing manifest differently in social networks compared to technological or biological networks?",
    'correct_answer': "Assortative mixing by degree refers to the tendency of nodes to connect to others with similar degrees. In social networks, high-degree nodes (hubs) often connect with other high-degree nodes, leading to communities with high internal connectivity. This is less common in technological or biological networks, where disassortative mixing (high-degree nodes connecting to low-degree nodes) is more typical. This difference affects network resilience and information flow; assortative networks may be more robust and cohesive, while disassortative networks can be more efficient in certain types of flows.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_oe6 = {
    'question': "Discuss the challenges and methods involved in detecting and visualizing power-law distributions in network data. Why is it important to accurately identify these distributions, and what techniques are commonly used?",
    'correct_answer': "Detecting and visualizing power-law distributions in network data is challenging due to the noise in the tail of the distribution and the need for proper normalization. Techniques such as logarithmic binning and cumulative distribution functions help mitigate these issues. Accurately identifying power-law distributions is crucial because they indicate scale-free properties, affecting the network's resilience and behavior. Common techniques include plotting the degree distribution on log-log scales, fitting power-law models, and using statistical methods to estimate the distribution's parameters.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_oe7 = {
    'question': "Examine the importance of component sizes in directed networks. How do weakly connected and strongly connected components differ, and what significance do they hold in the analysis of network structure?",
    'correct_answer': "In directed networks, component sizes are important for understanding connectivity and reachability. Weakly connected components are subgraphs where nodes are connected ignoring the direction of edges, while strongly connected components require paths in both directions between nodes. The largest strongly connected component is critical in analyzing the core structure of the network, revealing the subset of nodes that can mutually reach each other. Weakly connected components help identify broader connectivity patterns and the potential flow of information or resources.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_oe8 = {
    'question': "Explore the concept of geodesic paths and their relevance to the study of network topology. How do the shortest paths between vertices influence the overall connectivity and efficiency of a network?",
    'correct_answer': "Geodesic paths are the shortest paths between pairs of vertices in a network. These paths are crucial in determining the network's overall connectivity and efficiency. Short geodesic paths imply high efficiency in communication and transportation networks, facilitating rapid information or resource transfer. The average geodesic path length can indicate the 'small-world' nature of a network, where most nodes can be reached in a few steps, enhancing the network's functional performance.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_oe9 = {
    'question': "Investigate the phenomenon of 'funneling' in networks as described by Stanley Milgram. How does this concept relate to the small-world effect, and what does it reveal about the structure of social networks?",
    'correct_answer': "Funneling refers to the observation that many shortest paths in a network pass through a small number of key nodes or 'hubs.' This concept, highlighted by Milgram's 'small-world' experiments, shows that in social networks, certain individuals act as critical connectors. These hubs facilitate the rapid spread of information and maintain network cohesion. The funneling effect underscores the importance of central nodes in the network's connectivity and robustness.",
    'chapter_information': "Newman Networks Chapter 8"
}

newman_networks_c8_oe10 = {
    'question': "Discuss the use of centrality measures beyond degree centrality, such as eigenvector centrality and betweenness centrality. How do these measures provide additional insights into the roles and importance of vertices within a network?",
    'correct_answer': "Eigenvector centrality considers not just the number of connections a node has, but also the importance of those connections, providing a more nuanced view of a node's influence. Betweenness centrality measures how often a node appears on the shortest paths between other nodes, indicating its role in facilitating communication. These centrality measures offer deeper insights into network dynamics by identifying influential nodes that might not be evident through degree centrality alone, such as connectors or brokers in social networks or key routers in communication networks.",
    'chapter_information': "Newman Networks Chapter 8"
}
