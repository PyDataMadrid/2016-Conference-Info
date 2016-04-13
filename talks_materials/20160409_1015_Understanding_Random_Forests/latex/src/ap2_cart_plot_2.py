    while len(stack):
        node, max_x, min_x, max_y, min_y = stack.pop()
        feature, threshold, left, right = node

        if feature == 'distance':
            add_line(x=[threshold, threshold], y=[min_y, max_y])
        elif feature == 'age':
            add_line(x=[min_x, max_x], y=[threshold, threshold])
        else:
            continue

        stack.append(NodeRanges(node=nodes[left],
                                max_x=threshold if feature == 'distance' else max_x,
                                min_x=min_x,
                                max_y=threshold if feature == 'age' else max_y,
                                min_y=min_y))

        stack.append(NodeRanges(node=nodes[right],
                                max_x=max_x,
                                min_x=threshold if feature == 'distance' else min_x,
                                max_y=max_y,
                                min_y=threshold if feature == 'age' else min_y))

    show(plot)