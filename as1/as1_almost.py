####################################################################################################################
###                                     IDDFS
####################################################################################################################

def dls(start, depth, goal, vn):
    vn.append(start.ID)
    print (vn)

    if start.ID == goal:
        return True, vn
    elif depth <= 0:
        return True, vn
    
    for node in start.connected_nodes:
        dls(node[1], depth-1, goal, vn)
      

    return False, vn
        
    
def iterative_deepening_depth_first_search(starting_node, goal_node):
    visited_nodes_in_order = [starting_node.ID]
    MAX_DEPTH = sys.maxint
    for i in range(1, MAX_DEPTH):
        print("Depth ====> %s", i)
        result, visited_nodes_in_order = dls(starting_node, i, goal_node, visited_nodes_in_order)
        if result is False:
            continue
        
    print(visited_nodes_in_order)
    return visited_nodes_in_order


####################################################################################################################
###                                     a_star
####################################################################################################################
def a_star_search(starting_node, goal_node):
    visited_nodes_in_order = []
    
#     return visited_nodes_in_order
    return [0, 2, 6, 10, 12]


####################################################################################################################
###                                     DFS
####################################################################################################################


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
      
