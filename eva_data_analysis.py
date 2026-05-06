#load required packages
import matplotlib.pyplot as plt
import pandas as pd

# define functions
def read_json_to_dataframe (input_file):
    print(f"Reading file: {input_file}")
    # read input file from json to pandas datarfame
    eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
    eva_df['eva'] = eva_df['eva'].astype(float) # extract eva (time spent in space) as numerical value
    eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True) # clean data by removing lines where duration is missing
    return eva_df

def write_dataframe_to_csv (df, save_path):
    print("__SAVING CSV__")
    # saves edited data to csv for later analysis
    df.to_csv(save_path, index=False, encoding='utf-8')

def plot_cumulative_time_in_space (df, file_path):
    print(f"Plotting {graph_file} to graph file")
    # plot cumulative time spent in space against date
    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(file_path)
    plt.show()
    print("__FINISHED PLOTTING__")

# Data source: https://data.nasa.gov/resource/eva.json (with modifications)
input_file = open('./eva-data.json', 'r', encoding='ascii') # forcing ASCII encoding to avoid cross-platform errors
output_file = open('./eva-data.csv', 'w', encoding='utf-8') # forcing UTF-8 encoding to avoid cross-platform errors
graph_file = './cumulative_eva_graph.png'

print("__START__")
# read data from json file
eva_data = read_json_to_dataframe(input_file)

# convert and export file to csv
write_dataframe_to_csv(eva_data, output_file)

print("__PREPARING PLOT__")

eva_data.sort_values('date', inplace=True) # order date values to work in plot X-axis

# extract time spent in space and calculate cumulative value for plotting
eva_data['duration_hours'] = eva_data['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
eva_data['cumulative_time'] = eva_data['duration_hours'].cumsum()

# plot data
plot_cumulative_time_in_space(eva_data, graph_file)

print("__END__")