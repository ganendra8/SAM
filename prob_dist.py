import numpy as np
import random
from collections import Counter
import matplotlib.pyplot as plt


die_faces = [1,2,3,4,5,6]

prob = [1/6,1/6,1/6,1/6,1/6,1/6,]

rolls = np.random.choice(die_faces, size=100, p=prob)

frequency = Counter(rolls)

print('Face | Frequency')
print()
for face in sorted(frequency):
    print(f'{face:4} | {frequency[face]:9}')

plt.bar(frequency.keys(), frequency.values(), color='skyblue')

plt.xlabel('Face')
plt.ylabel('Frequency')
plt.title('Frequency Distribution of Dice Roll')

plt.show()