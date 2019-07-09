def depth_first_search(starting_node, goal_node):
    frontier, explored = starting_node.connected_nodes, []
    tmp = []
    for i, v in frontier:
        tmp.append(v)
    while True:
        if len(frontier) > 0:
            node = frontier.pop()
            node = node[1]
            if node == goal_node:
                print(frontier)
                return explored
            else:
                explored.append(node)
        else:
            raise Exception("Frontier is empty!!!")

        for n in reversed(node.connected_nodes):
            if n not in explored:
                frontier.append(n)
