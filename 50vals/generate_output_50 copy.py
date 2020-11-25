import numpy as np
def generate_stress(num):
    nums = []
    total = round(np.random.uniform(5.343, 5.624), 3)
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

generate_stress(4)
generate_stress(6)
generate_stress(4)
generate_stress(5)
generate_stress(5)
generate_stress(6)
generate_stress(3)
generate_stress(4)
generate_stress(3)
generate_stress(2)
generate_stress(8)

generate_h(4)
generate_h(6)
generate_h(4)
generate_h(5)
generate_h(5)
generate_h(6)
generate_h(3)
generate_h(4)
generate_h(3)
generate_h(2)
generate_h(8)