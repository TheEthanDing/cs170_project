import networkx as nx

from parse import read_input_file, write_output_file
from utils import is_valid_solution, calculate_happiness
import sys

#def generate(students, stress_sum, stress_range):
    
def subsetSum(gr, students, num_students, stress_sum, stress_range, k):
    if stress_sum <= stress_range:
        return []
    if (num_students  == 0 and stress_sum > stress_range):
        return None
    last_student_stress = 0
    g_iter = gr.__iter__()
    # for node in g_iter:
    #     print(node)
    # for s in students:
    #     print(s)
    # print(num_students)
    # print(stress_sum)
    # print(stress_range)
    # print(k)
    gr_copy = gr.copy()
    for s in students[:-1]:
        pair = (s, students[num_students-1])
        last_student_stress += gr_copy.edges[pair]["stress"]
        # gr_copy.add_edge(s, students[num_students-1])
        # return []
    sub1 = subsetSum(gr_copy, students, num_students - 1, stress_sum, stress_range, k)
    
    if (last_student_stress > stress_sum):
        return sub1
    
    if sub1 is None:
        sub2 = subsetSum(gr_copy, students, num_students - 1, stress_sum - last_student_stress, stress_range, k)
        if sub2 is None:
            return None
        else:
            return sub2 + [students[num_students-1]]
    
    else:
        return sub1

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
    dict_lists = []
    for k in range(1, G.number_of_nodes()):
        s_room = s/k
        g_copy = G.copy()
        threshold = 0
        keys = [i for i in range(k)]
        dict = {key: [] for key in keys}
        currkey = 0
        best_node_one = 0
        best_node_two = 0
        while g_copy.number_of_nodes() >= 1:
            if currkey >= k:
                dict = None
                break

            if g_copy.number_of_nodes == 1:
                dict[currkey].append(g_copy.__iter__().__next__())
                break

            g_iter = G.__iter__()
            # for node in g_iter:
            #     print(node)
            max_h = 0
            local_best_one = 0
            local_best_two = 0
            for node_one in g_iter:
                for node_two in g_iter:
                    h = G[node_one][node_two]["happiness"]
                    if (h > max_h):
                        max_h = h
                        local_best_one = node_one
                        local_best_two = node_two
            if max_h == 0:
                dict = None
                break
            
            if local_best_one == best_node_one and local_best_two== local_best_two:
                threshold += 0.05
            
            best_node_one = local_best_one 
            best_node_two = local_best_two
            # print(best_node_one)
            # print(best_node_two)

            if g_copy[best_node_one][best_node_two]["stress"] <= s_room:
                dict[currkey].append(best_node_one)
                dict[currkey].append(best_node_two)
                g_copy.remove_node(best_node_one)
                g_copy.remove_node(best_node_two)
                if (s_room - threshold*s_room) <= G[best_node_one][best_node_two]["stress"]:
                    break

            
            students = list(g_copy.nodes)
            num_students = g_copy.number_of_nodes()
            stress_sum = s_room - G[best_node_one][best_node_two]["stress"]
            # stress_sum = 0
            stress_range = threshold*s_room
            room_list = generate(students, stress_sum, stress_range)
            # room_list = subsetSum(G, students, num_students, stress_sum, stress_range, k)
            for student in room_list:
                dict[currkey].append(student)
            currkey += 1
        if  dict != None and is_valid_solution(dict, G, s, k):      
            dict_lists.append(dict)
    max_dict_happiness = 0
    max_dict = None
    for dict in dict_lists:
        h = calculate_happiness(dict, G)
        if h > max_dict_happiness:
            max_dict_happiness = h
            max_dict = dict
    return convert_dictionary(max_dict), len(max_dict)
    #maybe check if valid in the last for loop
    #pass


# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G, s = read_input_file(path)
    D, k = solve(G, s)
    assert is_valid_solution(D, G, s, k)
    print("Total Happiness: {}".format(calculate_happiness(D, G)))
    write_output_file(D, 'out/test.out')


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