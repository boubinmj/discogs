import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dababy_path = 'data/dababy.csv'

dababy = pd.read_csv(dababy_path, delimiter=',')
print(dababy)
dababy_s = dababy.sort_values(by=['year'])


dby_yrs = dababy_s.year.unique()
print(dby_yrs.shape)
print(type(dby_yrs))
# dby_yrs_s = dby_yrs.sort(axis=0)
# print(dby_yrs_s)

dby_per_year = [dababy[dababy.year == dby_yrs[i]].shape[0] for i in range(0,len(dby_yrs))]

print(dby_yrs)
print(dby_per_year)

# plt.xlabel('year')
# plt.ylabel('number of releases')
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlabel('year')
ax.set_ylabel('Number of Releases')
ax.bar(dby_yrs,dby_per_year)
plt.show()