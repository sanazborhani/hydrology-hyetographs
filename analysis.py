import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the Excel file 
file_path = 'Hyetograph.xlsx' 

# 'header=3' tells pandas to start reading from the 4th row
# 'sheet_name' must match your tab exactly
df = pd.read_excel(file_path, 
                   sheet_name='Hyetographs Delmarva PRF 284', 
                   header=3)

# 2. Filter for only the Cumulative Precipitation columns
# We want 'T (hrs)' and the next 6 columns (10-yr through 500-yr)
# We avoid the 'Incremental' columns to keep the graph clean
time_col = 'T (hrs)'
cumulative_cols = ['10-year', '25-Year', '50-Year', '100-Year', '200-Year', '500-Year']

# 3. Setup the Plot
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 7))

# 4. Plotting
for col in cumulative_cols:
    plt.plot(df[time_col], df[col], label=col, linewidth=1.5)

# 5. Formatting for Professional Engineering Report
plt.title('SCS 24-Hour Rainfall Distributions (Atlas 14)', fontsize=14, fontweight='bold')
plt.xlabel('Time (hours)', fontsize=12)
plt.ylabel('Cumulative Precipitation (inches)', fontsize=12)
plt.legend(title="Return Period", loc='upper left')
plt.grid(True, which="both", ls="-", alpha=0.5)

# 6. Show the graph
plt.tight_layout()
plt.show()
