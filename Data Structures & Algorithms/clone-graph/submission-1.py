class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        clones = {}

        def clone(nodo):
            if nodo is None:
                return None

            if nodo in clones:
                return clones[nodo]

            copia = Node(nodo.val)
            clones[nodo] = copia

            for neighbor in nodo.neighbors:
                copia.neighbors.append(clone(neighbor))

            return copia

        return clone(node)