import pydot
from IPython.display import Image

def print_cart_notebook(clf, features):
    dot_data = StringIO.StringIO()
    tree.export_graphviz(clf, feature_names=features, out_file=dot_data)
    data = dot_data.getvalue().encode('utf-8')
    graph = pydot.graph_from_dot_data(data).create_png()
    return Image(graph)
