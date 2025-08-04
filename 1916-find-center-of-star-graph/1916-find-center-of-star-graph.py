class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        for node, values in graph.items():
            if len(values) > 1:
                return node
        