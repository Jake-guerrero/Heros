import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

heros = pd.read_csv('heroes_information.csv')
heros



height = heros['Height'].sum()
count = heros['Height'].count()
average_height = height / count
round_average_height = round(average_height, 2)
print("Average Height:", round_average_height)


publisher_count = heros['Publisher'].value_counts()
print("Number of heroes per publisher:\,", publisher_count)


unique_races = heros['Race'].unique()
print("Unique races:", unique_races)


total_unique_races = heros['Race'].nunique()
print("Total number of unique races:", total_unique_races)

top_5_races = race_counts.head(5)
print("The top 5 races:")
print(top_5_races)

total_race_occurances = race_counts.sum()
print("The total of all races in comics are:", total_race_occurances)


counts = heros['Alignment'].value_counts()
print("Counts of each aligment if the character is either good, bad or neutral:")
print(counts)



counts = heros['Alignment'].value_counts()
plt.figure(figsize=(10, 6))
counts.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Alignment for Comic Book Character')
plt.xlabel('Alignment')
plt.ylabel('Number of Heros/Villians')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


top_5_races = race_counts.head(5)
plt.figure(figsize=(10, 6))
top_5_races.plot(kind='bar', color='skyblue')
plt.title('Top 5 Races by Count')
plt.xlabel('Race')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


publisher_count = heros['Publisher'].value_counts()
top_publishers = publisher_count.head(5)

# Plot the pie chart
plt.figure(figsize=(8, 8))
plt.pie(top_publishers, 
        labels=top_publishers.index, 
        autopct='%1.1f%%', 
        colors=plt.cm.Paired(range(len(top_publishers))),
        wedgeprops=dict(width=0.3))
plt.title('Top 5 Publishers by Number of Heroes')
plt.show()