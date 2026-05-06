#load required packages
import matplotlib.pyplot as plt
import pandas as pd

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding='ascii') # forcing ASCII encoding to avoid cross-platform errors
output_file = open('./eva-data.csv', 'w', encoding='utf-8') # forcing UTF-8 encoding to avoid cross-platform errors
graph_file = './cumulative_eva_graph.png'

print("__START__")
print(f"Reading file: {input_file}")

# read input file from json to pandas datarfame
eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
eva_df['eva'] = eva_df['eva'].astype(float) # extract eva (time spent in space) as numerical value
eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True) # clean data by removing lines where duration is missing

print("__SAVING CSV__")

# saves edited data to csv for later analysis
eva_df.to_csv(output_file, index=False, encoding='utf-8')

print("__PREPARING PLOT__")

eva_df.sort_values('date', inplace=True) # order date values to work in plot X-axis

# extract time spent in space and calculate cumulative value for plotting
eva_df['duration_hours'] = eva_df['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_df['cumulative_time'] = eva_df['duration_hours'].cumsum()

print(f"Plotting {graph_file} to graph file")

# plot cumulative time spent in space against date
plt.plot(eva_df['date'], eva_df['cumulative_time'], 'ko-')
plt.xlabel('Year')
plt.ylabel('Total time spent in space to date (hours)')
plt.tight_layout()
plt.savefig(graph_file)
plt.show()

print("__FINISHED__")