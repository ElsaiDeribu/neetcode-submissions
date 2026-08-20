class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        # TC: O(E·α(N)) ≈ O(E)
        # SC: O(V)

        if len(edges) != n - 1:
                return False

        parent = {i:i for i in range(n)}
        size = {i:1 for i in range(n)}


        def find_parent(x):

            if parent[x] == x:
                return x

            parent[x] = find_parent(parent[x])

            return parent[x]


        def union(x, y):

            repX = find_parent(x)
            repY = find_parent(y)

            if repX == repY:
                return x, y

            if size[repX] < size[repY]:

                parent[repX] = repY
                size[repY] += size[repX]

            else:
                parent[repY] = repX
                size[repX] += size[repY]


        for n1, n2 in edges:
            if union(n1, n2):
                return False
                

        return True















        