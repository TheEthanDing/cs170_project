import random
import os

def generate(students = 5, stress=80):

    filename = "{}.in".format(students) 

    file = open(filename, "w") 
    file.write("{}".format(str(students)))
    file.write("\n{}".format(str(stress)))
    
    for i in range(0,students):
        for j in range(0,students):
            if i < j: 
                smelly = "\n" + str(i) + " " + str(j)
                smelly += " {}".format(random.randint(1,20))
                smelly += " {}".format(round(random.random()*stress/students, 3))
                file.write(smelly)
    file.close()

generate(20, 80)