import pandas as pd
import matplotlib.pyplot as plt

# read the data from the csv file
df = pd.read_csv('data.csv', usecols=['Player', 'PSxG+/-'])

# sort the data by PSxG+/-
df_sorted = df.sort_values('PSxG+/-')

# create a bar chart
fig, ax = plt.subplots(figsize=(12, 8))

# plot the data
bars = ax.barh(df_sorted['Player'], df_sorted['PSxG+/-'])

# add title and labels
ax.set_title('La Liga Goalkeepers Shot-Stopping Stats', fontsize=18)
ax.set_xlabel('PSxG+/-', fontsize=14)
ax.set_ylabel('Goalkeeper', fontsize=14, labelpad=15)

# limit the x-axis to better visualize the data
ax.set_xlim([-12, 12])

# add labels to the bars
for bar in bars:
    value = bar.get_width()
    xpos = value + 0.2 if value > 0 else value - 0.2
    ax.text(xpos, bar.get_y() + bar.get_height()/2, '{:.2f}'.format(value), fontsize=10, color='black', va='center', ha='left' if value > 0 else 'right')

# show the plot
plt.show()
