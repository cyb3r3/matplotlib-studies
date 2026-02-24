#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np


data = {'a': np.arange(100),
        'c': np.random.randint(0, 100, 100),
        'd': np.random.randn(100)}
data['b'] = data['a'] + 10 * np.random.randn(100)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
