goal_node = 12
depth_first_search_answer = [0, 1, 4, 5, 8, 12]
iterative_deepening_depth_first_search_answer = [0, 0, 1, 2, 3, 0, 1,
                                                 4, 5, 2, 5, 6, 3, 7,
                                                 0, 1, 4, 5, 8, 2, 5,
                                                 8, 6, 9, 10, 3, 7, 11,
                                                 0, 1, 4, 5, 8, 12]
a_star_search_answer = [0, 2, 6, 10, 12]

assert (depth_first_search(build_graph(), goal_node)==depth_first_search_answer)
assert (iterative_deepening_depth_first_search(build_graph(), goal_node)==iterative_deepening_depth_first_search_answer)
assert (a_star_search(build_graph(), goal_node)==a_star_search_answer)



assert (a.depth_first_search(g.build_graph(), goal_node)==depth_first_search_answer)
assert (a.iterative_deepening_depth_first_search(g.build_graph(), goal_node)==iterative_deepening_depth_first_search_answer)
