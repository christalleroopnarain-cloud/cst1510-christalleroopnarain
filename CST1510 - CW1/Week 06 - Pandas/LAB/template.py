"""
RECORD CHECK  -  my version
===========================

Name  : Christalle Roopnarain
Lane  :  IT      
Date  : 05/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("Week 06 - Pandas/LAB/temp_data.csv") # Creating dataframe from csv file in week 6 lab folder

df["percent"] = (df["used_gb"] / df["total_gb"]) * 100 #adding percent column

#adding status coulumn
df["status"] = df["percent"].apply(
    lambda p: "OVER LIMIT" if p >= 100 else "WARNING" if p >= 90 else "OK"
)

df.to_csv("Week 06 - Pandas/LAB/full_dataframe.csv", index=False) #saving the full dataframe to a new csv in Week 6 lab folder

df = df[df["status"] != "OK"] #filtering out the OK columns

grouped_by_status = df.groupby("status") #grouping by status

print(df) #printing the full dataframe
print()
print(grouped_by_status.size())#printing a count per group



df["status"].value_counts().plot(kind="bar", title="Counts per status") #Creating the bar chart
plt.tight_layout()
plt.savefig("Week 06 - Pandas/LAB/counts_per_status.png") #saving the bar chart as a png in week 6 lab folder
plt.show()
