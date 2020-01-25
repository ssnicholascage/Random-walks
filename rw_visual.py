import matplotlib.pyplot as plt
from random_walk import RandomWalk


while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.title('Random Walks', fontsize=14)
    plt.xlabel('Random steps on x-axis', fontsize=14)
    plt.ylabel('Random steps on y-axis', fontsize=14)
    plt.show()

    keep_running = input("Do you want to make another walk, (y/n)?")
    if keep_running.lower() == 'n':
        break
