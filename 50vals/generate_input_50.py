import numpy as np
import sys
import fileinput

def generate_in():
    f = open("50.in", "w")
    f.write("50\n")
    f.write("61.864\n")
    for i in range(50):
        for j in range(i + 1, 50):
            f.write(str(i))
            f.write(" ")
            f.write(str(j))
            f.write(" ")
            happiness = round(np.random.uniform(0, 7.5), 3)
            f.write(str(happiness))
            f.write(" ")
            stress = round(np.random.uniform(0, 2.208), 3)
            f.write(str(stress))
            f.write("\n")

def change_vals(line, listh, lists):
    # f_out = open("50.out", "r")
    # f_in = open("50.in", "r")
    # for line in f_out:
    #     vals = line.split()
    counter = 0
    for i in range(len(line)-1):
        for j in range(i + 1, len(line)):
            # f_in = open("50.in", "r")
            for l in fileinput.input("50.in", inplace=True):
                if l.startswith(str(line[i]), 0) and (str(line[i]) + " " + str(line[j])) in l:
                    # l =  str(line[i]) + " " + str(line[j]) + " " + str(listh[i*len(line) + j - 1]) + " " + str(lists[i*len(line) + j - 1])
                    l=l.replace(l, str(line[i]) + " " + str(line[j]) + " " + str(listh[counter]) + " " + str(lists[counter]) + "\n")
                    # f_out = open("50_in", "w")
                    # f_out.write(new)
                sys.stdout.write(l)
                # sys.stdout.write(str(counter))
            counter += 1
            print(counter)

change_vals([8, 11, 26, 34, 36], [17.431, 12.798, 9.079, 6.326, 3.159, 3.312, 1.336, 1.102, 1.42, 3.405], [1.799, 0.654, 0.958, 0.842, 0.071, 0.17, 0.168, 0.163, 0.384, 0.41])
change_vals([19, 22, 23, 37, 40], [13.322, 12.661, 4.53, 4.289, 1.25, 5.606, 1.623, 1.602, 3.54, 8.761], [1.003, 1.225, 1.63, 0.381, 0.298, 0.326, 0.283, 0.133, 0.139, 0.178])
change_vals([3, 9, 14, 21, 24, 46], [9.798, 4.463, 11.598, 8.242, 0.537, 4.4, 5.019, 0.571, 1.05, 1.754, 1.725, 0.332, 0.026, 0.574, 4.159], [0.359, 1.833, 0.485, 0.353, 0.716, 0.63, 0.007, 0.091, 0.532, 0.031, 0.089, 0.069, 0.028, 0.069, 0.292])
change_vals([12, 31, 48], [15.209, 6.73, 31.846], [2.534, 0.056, 2.884])
change_vals([29, 35, 38, 41], [8.558, 5.596, 8.617, 5.849, 8.786, 20.891], [2.774, 1.201, 0.776, 0.176, 0.096, 0.591])
change_vals([6, 10, 13], [16.53, 7.396, 28.036], [2.22, 0.014, 3.259])
change_vals([15, 16], [45.607], [5.493])
change_vals([0, 27, 28, 33, 42, 44, 45, 47], [15.892, 8.394, 7.027, 0.528, 2.797, 5.273, 3.401, 2.801, 0.879, 2.154, 1.148, 1.863, 1.205, 0.501, 1.173, 0.585, 0.44, 0.25, 0.404, 0.177, 0.161, 0.13, 0.119, 0.022, 0.027, 0.071, 0.048, 0.19]
, [0.2, 0.473, 1.91, 0.154, 1.061, 0.61, 0.153, 0.328, 0.094, 0.148, 0.03, 0.01, 0.037, 0.026, 0.065, 0.026, 0.018, 0.005, 0.003, 0.007, 0.001, 0.005, 0.003, 0.002, 0.001, 0.003, 0.003, 0.003])
#generate_in()
