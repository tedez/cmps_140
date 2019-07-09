def dls(start, depth, goal, vn):
    vn.append(start.ID)
#     print(vn)

    if start.ID == goal:
        return True, vn
    elif depth <= 0:
        return False, vn

    for node in start.connected_nodes:
        r, vn = dls(node[1], depth - 1, goal, vn)
        if r is True:
            return True, vn

    return False, vn


def iterative_deepening_depth_first_search(starting_node, goal_node):
    visited_nodes_in_order = [starting_node.ID]
    MAX_DEPTH = 2^30
    for i in range(1, MAX_DEPTH):
#         print("Depth ====> %s", i)
        result, visited_nodes_in_order = dls(starting_node, i, goal_node, visited_nodes_in_order)
        if result is True:
#             print(visited_nodes_in_order)
            return visited_nodes_in_order


   
def depth_first_search(starting_node, goal_node):
    frontier, explored = starting_node.connected_nodes[::-1], [starting_node.ID]
    
    if frontier is None:
        return -1
    if starting_node.ID is goal_node:
        return explored
    
    while True:
        if len(frontier) > 0:
            node = frontier.pop()
            node = node[1]
            explored.append(node.ID)
              
            if node.ID == goal_node:
                return explored

            for n in (node.connected_nodes[::-1]):
                if n not in explored:
                    frontier.append(n)
        else:
            raise Exception("Empty frontier")
      

    
def a_star_search(starting_node, goal_node):
    closed_nodes = []
    open_nodes = set([(0,starting_node)])
    g = {}
    f = {(0,starting_node):0}
    came_from = {}
    g[(0,starting_node)] = 0

    while len(open_nodes) > 0:
        current_f, current_node = None, None
        # find adj node with lowest cost...
        for node in open_nodes:
            if current_node is None or f[node] < current_f:
                current_f = f[node]
                current_node = node

        if current_node[1].ID == goal_node:
            taken_path = [current_node[1].ID]

            while current_node in came_from:
                current_node = came_from[current_node]
                taken_path.append(current_node[1].ID)
            taken_path.reverse()
#             print(taken_path)
            return taken_path

#         print(current_node)
        closed_nodes.append(current_node)
#         print(open_nodes)
#         print("\n\n\n\n\n")

        open_nodes.remove(current_node)

        for n in current_node[1].connected_nodes:
            if n[1] in closed_nodes:
                continue
            candidate = g[current_node] + n[0]
            if n not in open_nodes:
                open_nodes.add(n)
            elif candidate >= g[n]:
                continue

            came_from[n] = current_node
            g[n] = candidate
#                 print(candidate)#, f[n[1]])
#                 print(current_node)
            f[n] = candidate + f[current_node]

    return []