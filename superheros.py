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


greater_height = heros.loc[heros['Height'] > 190]
print("Characters that are taller than 190 cm:")
print(greater_height)


unique_races = heros['Race'].unique()
print("Unique races:", unique_races)

greater_weight = heros.loc[heros['Weight'] > 190]
print("Characters that are taller than 190:")
print(greater_weight)

heros['Race'] = heros['Race'].replace('-', 'other')
heros

publisher_count = heros['Publisher'].value_counts()
top_publishers = publisher_count.head(5)

race_counts = heros['Race'].nunique()
print("Total number of unique races:", race_counts)

top_races = race_counts
print("The top 5 races:")
print(top_races)


counts = heros['Alignment'].value_counts()
print("Counts of each aligment if the character is either good, bad or neutral:")
print(counts)

heros['Alignment'] = heros['Alignment'].replace({'-', 'other'})

race_counts_series = pd.Series(race_counts)
race_counts_race = pd.DataFrame({'Race': race_counts_series})

race_counts = heros['Race'].value_counts()
top_races = race_counts.head(5)


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


top_races = race_counts.head(5)
plt.figure(figsize=(10, 6))
top_races.plot(kind='bar', color='skyblue')
plt.title('Top 5 Races by Count')
plt.xlabel('Race')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


publisher_count = heros['Publisher'].value_counts()
top_publishers = publisher_count.head(5)
plt.figure(figsize=(8, 8))
plt.pie(top_publishers, 
        labels=top_publishers.index, 
        autopct='%1.1f%%', 
        colors=plt.cm.Paired(range(len(top_publishers))),
        wedgeprops=dict(width=0.3))
plt.title('Top 5 Publishers by Number of Heroes')
plt.show()