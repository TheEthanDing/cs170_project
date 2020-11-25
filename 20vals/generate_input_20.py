import numpy as np
import sys
import fileinput

def generate_in():
    f = open("20.in", "w")
    f.write("20\n")
    f.write("83.153\n")
    for i in range(20):
        for j in range(i + 1, 20):
            f.write(str(i))
            f.write(" ")
            f.write(str(j))
            f.write(" ")
            happiness = round(np.random.uniform(0, 7.5), 3)
            f.write(str(happiness))
            f.write(" ")
            stress = round(np.random.uniform(7, 20), 3)
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
            for l in fileinput.input("20.in", inplace=True):
                if l.startswith(str(line[i]), 0) and (str(line[i]) + " " + str(line[j])) in l:
                    # l =  str(line[i]) + " " + str(line[j]) + " " + str(listh[i*len(line) + j - 1]) + " " + str(lists[i*len(line) + j - 1])
                    l=l.replace(l, str(line[i]) + " " + str(line[j]) + " " + str(listh[counter]) + " " + str(lists[counter]) + "\n")
                    # f_out = open("50_in", "w")
                    # f_out.write(new)
                sys.stdout.write(l)
                # sys.stdout.write(str(counter))
            counter += 1
            print(counter)

change_vals([1, 4, 17], [2.207, 16.202, 32.512], [5.045, 5.682, 5.821])
change_vals([2, 13], [56.549], [16.298])
change_vals([3, 9, 12, 15, 19], [14.216, 4.845, 2.768, 1.217, 9.107, 2.833, 3.522, 2.19, 1.313, 8.42], [4.255, 2.785, 4.428, 0.605, 1.588, 0.695, 0.143, 0.676, 0.242, 0.803])
change_vals([0, 5, 10, 18], [7.497, 5.854, 8.064, 5.206, 0.952, 26.314], [0.271, 6.848, 2.549, 0.559, 0.114, 5.927])
change_vals([6, 7, 8, 11, 14, 16], [13.666, 10.468, 8.408, 3.543, 1.669, 2.979, 2.187, 1.168, 1.004, 0.352, 0.741, 0.703, 1.39, 1.273, 2.674], [4.88, 2.983, 0.007, 0.084, 1.888, 3.093, 0.844, 0.451, 0.219, 0.072, 0.365, 0.105, 0.489, 0.298, 0.716])

# generate_in()
