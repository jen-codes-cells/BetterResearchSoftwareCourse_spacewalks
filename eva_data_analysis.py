#load required packages
import matplotlib.pyplot as plt
import pandas as pd

# define functions
def read_json_to_dataframe (input_file):
    """
    Read data from a JSON file into a Pandas dataframe
    Clean data by removing any rows where duration is missing

    Args:
        input_file (file or str): file object or path to JSON file

    Returns:
        pandas dataframe: clean data as dataframe structure
    """
    print(f"Reading file: {input_file}")
    # read input file from json to pandas datarfame
    eva_df = pd.read_json(input_file, convert_dates=['date'], encoding='ascii')
    eva_df['eva'] = eva_df['eva'].astype(float) # extract eva (time spent in space) as numerical value
    eva_df.dropna(axis=0, subset=['duration', 'date'], inplace=True) # clean data by removing lines where duration is missing
    return eva_df

def write_dataframe_to_csv (df, save_path):
    """
    Exports a pandas dataframe object as a csv file
    Enforces UTF-8 encoding

    Args:
        df (pandas dataframe): the dataframe object to be exported
        save_path (file or str): object or path where the file should be saved to
    """
    print("__SAVING CSV__")
    # saves edited data to csv for later analysis
    df.to_csv(save_path, index=False, encoding='utf-8')

def plot_cumulative_time_in_space (df, file_path):
    """
    Generates a plot from a pandas dataframe object and saves it as a png file
    Extracts and calculates cumulative time
    Orders date values
    Plots cumulative time spent in space (Y-axis) against date (X-axis)

    Args:
        df (pandas dataframe): dataframe object containing 'date' column
        file_path (file or str): file object or path where plot should be saved
    """
    print("__PREPARING PLOT__")
    eva_data.sort_values('date', inplace=True) # order date values to work in plot X-axis
    # extract time spent in space and calculate cumulative value for plotting
    eva_data['duration_hours'] = eva_data['duration'].str.split(":").apply(lambda x: int(x[0]) + int(x[1])/60)
    eva_data['cumulative_time'] = eva_data['duration_hours'].cumsum()
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


# plot data
plot_cumulative_time_in_space(eva_data, graph_file)

print("__END__")