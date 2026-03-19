import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Setup the data (Based on your DMC-Region C snippet)
# You can also load this from a CSV: df = pd.read_csv('rainfall_data.csv')
data = {
    'Time_hrs': [0, 0.1, 0.2, 0.3, 0.4],
    '10-Year': [0, 0.00655, 0.01183, 0.01715, 0.02258],
    '25-Year': [0, 0.0082, 0.01481, 0.02147, 0.02827],
    '50-Year': [0, 0.00965, 0.01742, 0.02526, 0.03325],
    '100-Year': [0, 0.01129, 0.02037, 0.02955, 0.0389],
}

df = pd.DataFrame(data)

# 2. Set Plot Style
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

# 3. Plotting Cumulative Curves
for column in df.columns[1:]:
    plt.plot(df['Time_hrs'], df[column], marker='o', label=f'{column} Storm')

# 4. Formatting the Graph
plt.title('SCS Method: Cumulative Precipitation Hyetograph', fontsize=14)
plt.xlabel('Time (hours)', fontsize=12)
plt.ylabel('Precipitation Depth (inches)', fontsize=12)
plt.legend(title="Return Period")
plt.grid(True, which="both", ls="-", alpha=0.5)

# Save and Show
plt.tight_layout()
plt.savefig('ddf_graph.png', dpi=300)
plt.show()

# --- Optional: Incremental Bar Chart (For a single return period) ---
def plot_incremental(return_period='100-Year'):
    plt.figure(figsize=(8, 5))
    # Calculate difference between rows to get incremental depth
    incremental = df[return_period].diff().fillna(0)
    
    plt.bar(df['Time_hrs'], incremental, width=0.08, color='skyblue', edgecolor='navy')
    plt.title(f'Incremental Rainfall Hyetograph - {return_period}')
    plt.xlabel('Time (hrs)')
    plt.ylabel('Incremental Depth (in)')
    plt.show()

# plot_incremental('100-Year')
