
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
        open_nodes = set([starting_node])
        g = {}
        f = {starting_node:0}
        came_from = {}
        
        g[starting_node] = 0
        # f[starting_node] = starting_node.heuristic_cost
        
        while len(open_nodes) > 0:
            current_node, current_f = None, None
            # find nadj node with lowwst cost...
            print(open_nodes)
            for node in open_nodes:
                if current_node is None or f[node] < current_f:
                    print("Node is ====> %s", node)
                    if node is starting_node:
                        current_f = f[node]
                        current_node = node
                    else:
                        current_f = f[node[1]]
                        current_node = node[1]
            
            if current_node.ID == goal_node:
                    print("top")
                    taken_path = [current_node.ID]
                    
                    while current_node in came_from:
                        current_node = came_from[current_node]
                        taken_path.append(current_node.ID)
                    taken_path.reverse()
                    print(taken_path)
                    return taken_path
                
            closed_nodes.append(current_node)
            open_nodes.remove(current_node)
            
            for n in current_node.connected_nodes[::-1]:
                if n in closed_nodes:
                    continue
                candidate = g[current_node] + n[0]
                if n not in open_nodes:
                    open_nodes.add(n)
                elif candidate >= g[n]:
                    continue
                    
                came_from[n] = current_node
                g[n] = candidate
                print(candidate)#, f[n[1]])
                print(current_node)
#                 f[n[1]] = candidate + f[current_node[1]]
                
        return []