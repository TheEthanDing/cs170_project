import numpy as np
import sys
import fileinput

def generate_in():
    f = open("10.in", "w")
    f.write("10\n")
    f.write("75.343\n")
    for i in range(10):
        for j in range(i + 1, 10):
            f.write(str(i))
            f.write(" ")
            f.write(str(j))
            f.write(" ")
            happiness = round(np.random.uniform(0, 7.5), 3)
            f.write(str(happiness))
            f.write(" ")
            stress = round(np.random.uniform(6, 13), 3)
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
            for l in fileinput.input("10.in", inplace=True):
                if l.startswith(str(line[i]), 0) and (str(line[i]) + " " + str(line[j])) in l:
                    # l =  str(line[i]) + " " + str(line[j]) + " " + str(listh[i*len(line) + j - 1]) + " " + str(lists[i*len(line) + j - 1])
                    l=l.replace(l, str(line[i]) + " " + str(line[j]) + " " + str(listh[counter]) + " " + str(lists[counter]) + "\n")
                    # f_out = open("50_in", "w")
                    # f_out.write(new)
                sys.stdout.write(l)
                # sys.stdout.write(str(counter))
            counter += 1
            print(counter)

change_vals([1, 3, 7], [17.968, 12.889, 27.768], [8.552, 5.285, 11.192])
change_vals([0, 2, 4, 9], [1.667, 1.513, 7.747, 11.748, 2.353, 27.046], [6.196, 3.44, 2.705, 5.35, 3.43, 3.944])
change_vals([5, 6, 8], [12.224, 9.047, 28.959], [3.738, 4.902, 16.46])
# generate_in()
