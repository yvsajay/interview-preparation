
# this technique will not work. Think about something else

# it will only work if the edges are given in a particular order

from collections import defaultdict

class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if not edges:
            if n == 1:
                return True
            elif n == 2:
                return False

        visited_nodes = defaultdict(list)
        count = True
        unvisited = []

        for key, value in edges:

            if key in visited_nodes and value in visited_nodes:
                return False

            if count:
                visited_nodes[key] = []
                visited_nodes[value] = []
                count = False
                continue
            if key in visited_nodes:
                visited_nodes[key].append(value)
                visited_nodes[value] = []
            elif value in visited_nodes:
                visited_nodes[value].append(key)
                visited_nodes[key] = []
            else:
                unvisited.append([key, value])

        for key, value in unvisited:

            if key in visited_nodes and value in visited_nodes:
                return False

            if key in visited_nodes:
                visited_nodes[key].append(value)
                visited_nodes[value] = []
            elif value in visited_nodes:
                visited_nodes[value].append(key)
                visited_nodes[key] = []
            else:
                return False

        return n == len(visited_nodes.keys())

print Solution().validTree(4, [[0, 1], [2, 3], [1, 2]])

