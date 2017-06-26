import matplotlib.pyplot as plt
import numpy as np

def play_dice(dice_num):
    if dice_num == 6:
        return 10
    else:
        return -1

def game():
    generate_dice = np.random.randint(low=1, high=7,size=1000)
    calc_return = np.array([play_dice(i) for i in generate_dice])
    return sum(calc_return)

should_be_normal = np.array([game() for _ in range(10000)])
plt.hist(should_be_normal)
plt.show()
