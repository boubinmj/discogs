import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dababy_path = 'data/api/dababy.csv'
huey_path = 'data/api/huey.csv'
yr_76_path = 'data/api/1976_api.csv'
yr_10_path = 'data/api/2010_api.csv'

dababy = pd.read_csv(dababy_path, delimiter=',')
huey = pd.read_csv(huey_path, delimiter=',')
yr_76 = pd.read_csv(yr_76_path, delimiter = ',')
yr_10 = pd.read_csv(yr_10_path, delimiter=',')

dababy = dababy[dababy.year != 0]
huey = huey[huey.year != 0]
yr_76 = yr_76[yr_76.year !=0]
yr_10 = yr_10[yr_10.year !=0]

dababy_s = dababy.sort_values(by=['year'])
huey_s = huey.sort_values(by=['year'])
yr_76_s = yr_76.sort_values(by=['year'])
yr_10_s = yr_10.sort_values(by=['year'])

dby_yrs = dababy_s.year.unique()
huey_yrs = huey_s.year.unique()
yr_76_yrs = yr_76_s.year.unique()
yr_10_yrs = yr_10_s.year.unique()

dby_per_year = [dababy[dababy.year == dby_yrs[i]].shape[0] for i in range(0,len(dby_yrs))]
huey_per_year = [huey[huey.year == huey_yrs[i]].shape[0] for i in range(0,len(huey_yrs))]
yr_76_per_year = [yr_76[yr_76.year == yr_76_yrs[i]].shape[0] for i in range(0,len(yr_76_yrs))]
yr_10_per_year = [yr_10[yr_10.year == yr_10_yrs[i]].shape[0] for i in range(0,len(yr_10_yrs))]


fig = plt.figure()
ax = fig.add_subplot(211)
ax.set_xlabel('year')
ax.set_ylabel('Number of Releases')
ax.bar(dby_yrs,dby_per_year)

ax2 = fig.add_subplot(212)
ax2.set_xlabel('year')
ax2.set_ylabel('Number of Releases')
ax2.bar(huey_yrs, huey_per_year)

plt.show()

fig2 = plt.figure()
ax3 = fig2.add_subplot(111)
ax3.bar(huey_yrs,huey_per_year, color = 'b', width = 0.5, label = "Huey")
ax3.bar(dby_yrs+0.5,dby_per_year, color = 'g', width=0.5, label = "Dababy")
ax3.set_xlabel('year')
ax3.set_ylabel('Number of Releases')
ax3.set_title('Releases - Dababy vs. Huey Lewis and the News')
plt.legend()
plt.show()

fig3 = plt.figure()
ax4 = fig3.add_subplot(111)
ax4.bar(yr_76_yrs,yr_76_per_year, color = 'b', width = 0.5, label = "1976")
ax4.bar(yr_10_yrs+0.5,yr_10_per_year, color = 'g', width = 0.5, label = "2010")
ax4.set_xlabel('year')
ax4.set_ylabel('Number of Releases')
ax4.set_title('Releases by Artists per Year')
plt.legend()
plt.show()
