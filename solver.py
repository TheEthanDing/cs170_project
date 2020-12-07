import networkx as nx

from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_happiness
import sys

def sort_ratios(G, room_list):
    ratio_list = []
    g_iter = G.__iter__()
    for node in g_iter:
        total_h = 0
        total_s = 0
        for room_node in room_list:
            total_h += G[node][room_node]["happiness"]
            total_s += G[node][room_node]["stress"]
        total_ratio = total_h/total_s
        ratio_list.append(total_ratio)
    return ratio_list.sort(reverse=True)

def solve(G, s):
    """
    Args:
        G: networkx.Graph
        s: stress_budget
    Returns:
        D: Dictionary mapping for student to breakout room r e.g. {0:2, 1:0, 2:1, 3:2}
        k: Number of breakout rooms
    """

    # TODO: your code here!
    #for one k
    keys = [i for i in range(G.number_of_nodes())]
    dict = {key: [] for key in keys}
    curr_room = 0
    G_copy = G
    g_iter = G_copy.__iter__()
    n = G_copy.number_of_nodes()
    max_ratio = 0
    best_node_one = 1
    best_node_two = 2
    for node in g_iter:
        for node_two in g_iter:
            h = G_copy[node_one][node_two]["happiness"]
            s = G_copy[node_one][node_two]["stress"]
            if (s == 0) {
                s = 0.0001
            }
            hs_ratio = h/s
            if (hs_ratio > max_ratio) {
                max_ratio = hs_ratio
                best_node_one = node_one
                best_node_two = node_two
            }
    dict[0].append(best_node_one)
    dict[0].append(best_node_two)

    #add check for is_valid_solution
    G_copy.remove_node(best_node_one)
    G_copy.remove_node(best_node_two)
    # while sum(dict.values()) < n*(n+1)/2 or (0 not in dict.values()):
    #for one room
    while G_copy:
        while dict[curr_room] <= s/k:
            sorted_list = sort_ratios(G, dict[curr_room])
            if sorted_list[0]


    pass



# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

# if __name__ == '__main__':
#     assert len(sys.argv) == 2
#     path = sys.argv[1]
#     G, s = read_input_file(path)
#     D, k = solve(G, s)
#     assert is_valid_solution(D, G, s, k)
#     print("Total Happiness: {}".format(calculate_happiness(D, G)))
#     write_output_file(D, 'out/test.out')


# For testing a folder of inputs to create a folder of outputs, you can use glob (need to import it)
# if __name__ == '__main__':
#     inputs = glob.glob('file_path/inputs/*')
#     for input_path in inputs:
#         output_path = 'file_path/outputs/' + basename(normpath(input_path))[:-3] + '.out'
#         G, s = read_input_file(input_path, 100)
#         D, k = solve(G, s)
#         assert is_valid_solution(D, G, s, k)
#         cost_t = calculate_happiness(T)
#         write_output_file(D, output_path)
