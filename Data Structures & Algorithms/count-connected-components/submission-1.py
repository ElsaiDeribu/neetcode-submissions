class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # TC: O(V + E)
        # SC: O(V)

        parent = {i:i for i in range(n)}
        size = {i:1 for i in range(n)}


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


        for n1, n2 in edges: # TC: O(E · α(V)) ≈ O(E)
            union(n1, n2)


        return len({find_parent(i) for i in range(n)}) # O(V)

        