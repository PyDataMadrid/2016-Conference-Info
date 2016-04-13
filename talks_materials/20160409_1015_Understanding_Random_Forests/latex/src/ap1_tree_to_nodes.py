from collections import namedtuple
from itertools import starmap

def tree_to_nodes(dtree):
    nodes = starmap(namedtuple('Node', 'feature,threshold,left,right'),
                    zip(map(lambda x: {0: 'age', 1: 'distance'}.get(x),
                            dtree.tree_.feature),
                        dtree.tree_.threshold,
                        dtree.tree_.children_left,
                        dtree.tree_.children_right))
    return list(nodes)