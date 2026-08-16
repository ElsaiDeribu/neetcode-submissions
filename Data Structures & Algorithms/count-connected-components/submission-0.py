class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # TC: O(V + E)
        # SC: O(V + E)
        
        count = 0
        adj_list = defaultdict(list)
        visited = set()

        for n1, n2 in edges:
            adj_list[n1].append(n2)
            adj_list[n2].append(n1)
        

        def dfs(node):
            visited.add(node)

            for neibr in adj_list[node]:
                if neibr not in visited:
                    dfs(neibr)


        for node in range(n):
            if node not in visited:
                count += 1
                dfs(node)


        return count

