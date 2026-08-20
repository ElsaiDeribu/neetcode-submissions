class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # TC: O(E · α(V)) ≈ O(E)
        # SC: O(V)

        n = len(edges)
        parent = {i:i for i in range(1, n + 1)}
        size = {i:1 for i in range(1, n + 1)}


        def find_parent(x):

            if parent[x] == x:
                return x

            parent[x] = find_parent(parent[x])

            return parent[x]


        def union(x, y):

            rep_x = find_parent(x)
            rep_y = find_parent(y)

            if rep_x == rep_y:
                return [x, y]

            if size[rep_x] < size[rep_y]:

                parent[rep_x] = rep_y
                size[rep_y] += size[rep_x]
            else:
                parent[rep_y] = rep_x
                size[rep_x] += size[rep_y]


        ans = []
        for n1, n2 in edges:
            res = union(n1, n2)
            if res:
                ans = res


        return ans













        