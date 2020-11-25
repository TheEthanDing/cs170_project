import networkx as nx
from parse import *
from utils import *
import sys

assert len(sys.argv) == 3

input = sys.argv[1]
output = sys.argv[2]
G, s = read_input_file(input)
D = read_output_file(output, G, s)

room_to_s = {}
for k, v in D.items():
    room_to_s.setdefault(v, []).append(k)

rooms = len(room_to_s)
print("Number of Breakout Rooms: " + str(rooms))

print("Total Happiness: " + str(calculate_happiness(D, G)))

print("Happiness of Each Room")
for k, v in room_to_s.items():        
    room_happiness = calculate_happiness_for_room(v, G)
    print("Happiness of Room " + str(k) + ": " + str(room_happiness))

print("Max Stress: " + str(s))
print("Stress Threshold: " + str(s/rooms))

print("Stress of Each Room")
for k, v in room_to_s.items():        
    room_stress = calculate_stress_for_room(v, G)
    print("Stress of Room " + str(k) + ": " + str(room_stress))
        