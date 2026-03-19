import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Excel file
# Adjusted to match your file structure in the screenshot
file_path = 'Hyetograph.xlsx' 

# Make sure 'Sheet1' matches the name of the tab in your Excel file
# If your tab is named something else (like "DDF"), change it here:
df = pd.read_excel(file_path, sheet_name='Sheet1')

# 2. Identify columns (Assumes column 1 is Time and others are Return Periods)
# Based on your previous table, this will pick 'T (hrs)' as the X-axis
time_col = df.columns[0]
storm_cols = df.columns[1:]

# 3. Setup the Plot
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# 4. Plot Cumulative Precipitation
for col in storm_cols:
    plt.plot(df[time_col], df[col], label=f'{col}', marker='.')

# 5. Formatting
plt.title('SCS Method Hyetographs from Atlas 14', fontsize=14)
plt.xlabel('Time (hours)', fontsize=12)
plt.ylabel('Precipitation Depth (inches)', fontsize=12)
plt.legend(title="Storm Frequency", bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()

# 6. Display the result
plt.show()
