import networkx as nx

from parse import *
from utils import *
import glob
import sys


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
    D = {}
    k = 0
    
    students_left = G.number_of_nodes()
    student_pairs = G.edges
    student_pair_to_ratio = {}
    for pair in student_pairs:
        #print(G.edges[pair]["stress"], pair)
        ratio = 100000
        if G.edges[pair]["stress"] > 0:
            ratio = G.edges[pair]["happiness"] / G.edges[pair]["stress"]
        student_pair_to_ratio[pair] = [ratio, G.edges[pair]["happiness"]]
    student_pair_to_ratio = sorted(student_pair_to_ratio.items(), key = lambda x: (x[1][0], x[1][1]), reverse=True)

    room_to_students = {}

    while students_left > 0:
        students_left = G.number_of_nodes()
        k += 1
        D.clear()
        #students_remaining = student_pair_to_ratio.copy()
        #print("Number of breakout rooms so far: " + str(k))
        #print("Stress Threshoed: " + str(s/k))
        for r in range(k):
            #room_stress = 0
            room_to_students[r] = []
            for pair_and_ratio in student_pair_to_ratio:
                pair = pair_and_ratio[0]
                student_1 = pair[0]
                student_2 = pair[1]
                #print("First student pair: " + str(pair_and_ratio))
                # If both students are already in assigned rooms, go to next pair
                if student_1 in D.keys() and student_2 in D.keys():
                    #print("Both students in this pair are already assigned to rooms.")
                    continue
                temp = room_to_students[r].copy()
                temp.extend(pair)
                #print("Students in room " + str(r) +": " + str(room_to_students[r]))
                #print("Stress in this room: " + str(calculate_stress_for_room(room_to_students[r], G)))
                if calculate_stress_for_room(temp, G) <= s/k:
                    if student_1 not in D.keys() and student_2 not in D.keys():
                        D[student_1] = r
                        D[student_2] = r
                        room_to_students[r].extend(pair)
                        students_left -= 2
                    elif student_1 in room_to_students[r] and student_2 not in D.keys():
                        D[student_2] = r
                        room_to_students[r].append(student_2)
                        students_left -= 1
                    elif student_1 not in D.keys() and student_2 in room_to_students[r]:
                        D[student_1] = r
                        room_to_students[r].append(student_1)
                        students_left -= 1
                elif r + 1 >= k:
                    break
            #print("Number of unassigned students: " + str(students_left))

    #print(student_pair_to_ratio[0][0])
    return D, k


# Here's an example of how to run your solver.

# Usage: python3 solver.py test.in

if __name__ == '__main__':
    assert len(sys.argv) == 2
    path = sys.argv[1]
    G, s = read_input_file(path)
    solve(G, s)
    D, k = solve(G, s)
    assert is_valid_solution(D, G, s, k)
    print("Total Happiness: {}".format(calculate_happiness(D, G)))
    print("Number of Breakout Rooms: " + str(k))
    print(D)
    #write_output_file(D, 'out/test.out')


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
