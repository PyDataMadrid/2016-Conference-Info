from collections import namedtuple, deque
from functools import partial

class NodeRanges(namedtuple('NodeRanges', 'node,max_x,min_x,max_y,min_y')):
    pass

def cart_plot(nodes):
    nodes = tree_to_nodes(dtree)

    plot = base_plot()
    add_line = partial(plot.line, line_color='black', line_width=2)

    stack = deque()
    stack.append(NodeRanges(node=nodes[0],
                            max_x=df['distance'].max(),
                            min_x=df['distance'].min(),
                            max_y=df['age'].max(),
                            min_y=df['age'].min()))

# (continues)