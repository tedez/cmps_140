class Node:
    """
    This class describes a single node contained within a graph. 
    It has the following instance level attributes:
    
    ID: An integer id for the node i.e. 1
    heuristic_cost: A float value representing the estimated 
                    cost to the goal node
    """    
    def __init__(self, ID, heuristic_cost):
        self.ID = ID
        self.connected_nodes = []
        self.heuristic_cost = heuristic_cost
        
    def __repr__(self):
        ID = self.ID
        hx = self.heuristic_cost
        if len(self.connected_nodes)==0:
            nodes = 'None'
        else:
            nodes = ','.join(str(cn[1].ID) for cn in self.connected_nodes)
        return 'Node:{}\nh(n):{}\nConnected Nodes:{}'.format(ID, hx, nodes)
        
    def set_connected_nodes(self,connected_nodes):
        """
        Adds edges that lead from this node to other nodes:
        
        Parameters:
        - connected_nodes: A list of tuples consisting of (cost, Node), 
                           where 'cost' is a floating point value 
                           indicating the cost to get from this node 
                           to 'Node' and 'Node' is a Node object
        """
        self.connected_nodes = connected_nodes
    
def build_graph():
    """
    Builds the graph to be parsed by the search algorithms.
    Returns: The starting node, which is the entry point into the graph
    """
    ids = range(13)
    coords = [(0,0), (1,1), (1,0), (1,1), (5,2), (3,1), (3,0), 
              (3,-1), (5,1), (4,1), (4,0), (4,-2), (7,0)]
    
    #https://en.wikipedia.org/wiki/Euclidean_distance
    euclidean_distance = lambda x1y1, x2y2: ((x1y1[0]-x2y2[0])**2 +  (x1y1[1]-x2y2[1])**2)**(0.5)
    
    def build_connected_node_list(from_id, to_ids):
        starting_coords = coords[from_id]
        
        connected_nodes = []
        for to_id in to_ids:
            connected_nodes.append((euclidean_distance(starting_coords, coords[to_id]), all_nodes[to_id]))
            
        return connected_nodes
    
    goal_coords = (7,0)
    all_nodes = [Node(_id, euclidean_distance(coord, goal_coords)) for _id, coord in zip(ids, coords)]
    
    all_nodes[8].set_connected_nodes(build_connected_node_list(8, [12]))
    all_nodes[10].set_connected_nodes(build_connected_node_list(10,[12]))
    all_nodes[5].set_connected_nodes(build_connected_node_list(5, [8]))
    all_nodes[6].set_connected_nodes(build_connected_node_list(6, [9, 10]))
    all_nodes[7].set_connected_nodes(build_connected_node_list(7, [11]))
    all_nodes[1].set_connected_nodes(build_connected_node_list(1, [4,5]))
    all_nodes[2].set_connected_nodes(build_connected_node_list(2, [5,6]))
    all_nodes[3].set_connected_nodes(build_connected_node_list(3, [7]))
    all_nodes[0].set_connected_nodes(build_connected_node_list(0, [1,2,3]))
    
    return all_nodes[0]

#
# ####################################################################################################################
# ###                                     IDDFS
# ####################################################################################################################
#
# def dls(start, depth, goal, vn):
#     vn.append(start.ID)
#
#     if start.ID == goal:
#         return True, vn
#     elif depth <= 0:
#         return False, vn
#
#     for node in start.connected_nodes:
#         r, vn = dls(node[1], depth-1, goal, vn)
#         if r is True:
#             return True, vn
#     return False, vn
#
#
# def iterative_deepening_depth_first_search(starting_node, goal_node):
#     visited_nodes_in_order = [starting_node.ID]
#     MAX_DEPTH =  2**31-1
#     for i in range(1, MAX_DEPTH):
#         result, visited_nodes_in_order = dls(starting_node, i, goal_node, visited_nodes_in_order)
#         print(visited_nodes_in_order)
#
#         if result is True:
#             return visited_nodes_in_order
#
#
# ####################################################################################################################
# ###                                     a_star
# ####################################################################################################################
# def a_star_search(starting_node, goal_node):
#         print("a star search\n")
#         closed_nodes = {}
#         open_nodes = set([starting_node])
#         g = {}
#         f = {}
#         came_from = {}
#
#         g[starting_node] = 0
#         f[starting_node] = starting_node.heuristic_cost
#
#         while len(open_nodes) > 0:
#             current_node, current_f = None, None
#
#             for node in open_nodes:
#                 if current_node is None or f[node[1]] < current_f:
#                     current_f = f[node[1]]
#                     current_node = node
#
#             if current_node[1].ID == goal_node:
#                     print("top")
#                     taken_path = [current_node[1].ID]
#
#                     while current_node in came_from:
#                         current_node = came_from[current_node]
#                         taken_path.append(current_node[1].ID)
#                     taken_path.reverse()
#                     print(taken_path)
#                     return taken_path
#
#             closed_nodes.add(current_node)
#             open_nodes.remove(current_node)
#
#             for n in current_node.connected_nodes[::-1]:
#                 if n in closed_nodes:
#                     continue
#                 candidate = g[current_node[1] + n[0]]
#                 if n not in open_nodes:
#                     open_nodes.Add(n)
#                 elif candidate >= g[n[1]]:
#                     continue
#
#                 came_from[n] = current_node
#                 g[n[1]] = candidate
#                 f[n[1]] = candidate + n.heuristic_cost
#
#         return []
# #     return [0, 2, 6, 10, 12]
#
# ####################################################################################################################
# ###                                     DFS
# ####################################################################################################################
#
#
# def depth_first_search(starting_node, goal_node):
#     print("derp")
#     frontier, explored = starting_node.connected_nodes[::-1], [starting_node.ID]
#
#     if frontier is None:
#         return -1
#     if starting_node.ID is goal_node:
#         return explored
#
#     while True:
#         if len(frontier) > 0:
#             node = frontier.pop()
#             node = node[1]
#             explored.append(node.ID)
#
#             if node.ID == goal_node:
#                 print(explored)
#                 return explored
#
#             for n in (node.connected_nodes[::-1]):
#                 if n not in explored:
#                     frontier.append(n)
#         else:
#             raise Exception("Empty frontier")