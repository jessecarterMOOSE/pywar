from war import play
import matplotlib.pyplot as plt

num_rounds = 1000
counts = []
for i in range(0, num_rounds):
    if i % 100 == 0:
        print 'done with', i, 'rounds'
    counts.append(play())

print
print 'done!'
print 'min number of hands to win:', min(counts)
print 'max number of hands to win:', max(counts)

plt.hist(counts, bins='auto')
plt.xlabel('number of hands to win')
plt.ylabel('number of outcomes')
plt.xlim(left=0)
plt.ylim(bottom=0)
plt.tight_layout()
plt.show()