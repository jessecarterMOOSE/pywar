from war import play
import matplotlib.pyplot as plt

num_rounds = 1000
counts = []
for i in range(0, num_rounds):
    if i % 100 == 0:
        print 'done with', i, 'rounds'
    counts.append(play())

plt.hist(counts, bins='auto', normed=True)
plt.show()