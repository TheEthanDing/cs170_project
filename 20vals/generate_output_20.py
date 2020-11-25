import numpy as np

def generate_s(num):
    nums = []
    total = round(np.random.uniform(16.2, 16.631), 3)
    print(total)
    for i in range(int(num*(num-1)/2)):
        val = 0
        if i == int(num*(num-1)/2) - 1:
            val = round(total, 3)
        else:
            val = round(np.random.uniform(0, total/2), 3)
        nums.append(val)
        total -= val
    print(nums)

def generate_h(num):
    nums = []
    total = round(np.random.uniform(50, 60), 3)
    print(total)
    for i in range(int(num*(num-1)/2)):
        val = 0
        if i == int(num*(num-1)/2) - 1:
            val = round(total, 3)
        else:
            val = round(np.random.uniform(0, total/3), 3)
        nums.append(val)
        total -= val
    print(nums)

print("Stresses are")
generate_s(3) # room 1
generate_s(2) # room 2
generate_s(5) # room 3
generate_s(4) # room 4
generate_s(6) # room 5


print("Happinesses are")
generate_h(3) # room 1
generate_h(2) # room 2
generate_h(5) # room 3
generate_h(4) # room 4
generate_h(6) # room 5