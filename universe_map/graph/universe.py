#from gremlin_python.process.graph_traversal import GraphTraversalSource, GraphTraversal
#from gremlin_python.process.graph_traversal import __ as AnonymousTraversal
#from gremlin_python.process.traversal import Bytecode, P
from gremlin_python.structure.graph import Graph

import sys

"""
class UniverseTraversal(GraphTraversal):
    def characters(self):
        # Finds the actors in a movie by traversing from a "movie" to an "person" over the "actor" edge.
        # return self.out("actor").hasLabel('person') # extra verification that a 'person' is obtained
        return self.characters()

class UniverseTraversalSource(GraphTraversalSource):
    def __init__(self, *args, **kwargs):
        super(UniverseTraversalSource, self).__init__(*args, **kwargs)
        self.graph_traversal = UniverseTraversal

    def characters(self, *args):
        #traversal = self.get_graph_traversal().V().hasLabel("character")
        traversal = self.get_graph_traversal().hasLabel("character")
        return traversal


class __(AnonymousTraversal):
    graph_traversal = UniverseTraversal

    @classmethod
    def characters(cls):
        return cls.graph_traversal(None, None, Bytecode()).characters()

"""
if __name__ == "__main__":
    graph = Graph()
    g = graph.traversal()
    g.addV("universe").property('name','Outlander')
    g.addV("character").property('name', 'Jamie Fraser').property("character_id", 1)
    g.addV("character").property('name', 'Claire Fraser').property("character_id", 2)
    g.V(1).addE("hosting").to(g.V(2))
    g.V(1).addE("hosting").to(g.V(3))
    g.V(2).addE("married").to(g.V(3))
    m = g.V(1).has('hosting').out().values('name').fold()
    print(m)


    #for n in g.characters().values('name').toList():
    #    print(n)

    sys.exit()