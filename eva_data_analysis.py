#load required packages
import matplotlib.pyplot as plt
import pandas as pd
import sys

# define functions

def main (input_file, output_file, graph_file):
    print("__START__")
    # read data from json file
    eva_data = read_json_to_dataframe(input_file)

    # Calculate and add crew size to data
    eva_data = add_crew_size_column(eva_data) # colleague request 1

    # convert and export file to csv
    write_dataframe_to_csv(eva_data, output_file)

    # sort dataframe by date
    eva_data.sort_values("date", inplace=True)

    # plot data
    plot_cumulative_time_in_space(eva_data, graph_file)

    print("__END__")

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
    # extract time spent in space and calculate cumulative value for plotting
    df = add_duration_hours(df)
    df['cumulative_time'] = df['duration_hours'].cumsum()
    print(f"Plotting {graph_file} to graph file")
    # plot cumulative time spent in space against date
    plt.plot(df['date'], df['cumulative_time'], 'ko-')
    plt.xlabel('Year')
    plt.ylabel('Total time spent in space to date (hours)')
    plt.tight_layout()
    plt.savefig(file_path)
    plt.show()
    print("__FINISHED PLOTTING__")

def text_to_duration(duration):
    """
    Convert a text format duration "HH:MM" to duration in hours

    Args:
        duration (str): The text format duration

    Returns:
        duration_hours (float): The duration in hours
    """
    hours, minutes = duration.split(":")
    duration_hours = int(hours) + int(minutes)/60  # there is an intentional bug on this line (should divide by 60 not 6)
    return duration_hours


def add_duration_hours(df):
    """
    Add duration in hours (duration_hours) variable to the dataset

    Args:
        df (pd.DataFrame): The input dataframe.

    Returns:
        df_copy (pd.DataFrame): A copy of df with the new duration_hours variable added
    """
    df_copy = df.copy()
    df_copy["duration_hours"] = df_copy["duration"].apply(
        text_to_duration
    )
    return df_copy

def calculate_crew_size(crew): # colleague request 2
    """
    Calculate the size of the crew for a single crew entry

    Args:
        crew (str): The text entry in the crew column containing a list of crew member names

    Returns:
        (int): The crew size
    """
    if crew.split() == []:
        return None
    else:
        return len(re.split(r';', crew))-1
    
def add_crew_size_column(df): # colleauge request 3
    """
    Add crew_size column to the dataset containing the value of the crew size

    Args:
        df (pd.DataFrame): The input data frame.

    Returns:
        df_copy (pd.DataFrame): A copy of the dataframe df with the new crew_size variable added
    """
    print('Adding crew size variable (crew_size) to dataset')
    df_copy = df.copy()
    df_copy["crew_size"] = df_copy["crew"].apply(
        calculate_crew_size
    )
    return df_copy


# main code

if __name__ == "__main__":

    if len(sys.argv) < 3:
        # Data source: https://data.nasa.gov/resource/eva.json (with modifications)
        input_file = open('./data/eva-data.json', 'r', encoding='ascii') # forcing ASCII encoding to avoid cross-platform errors
        output_file = open('./results/eva-data.csv', 'w', encoding='utf-8') # forcing UTF-8 encoding to avoid cross-platform errors
        print("Using default input and output")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        print("Using custom input and output files")


    graph_file = './results/cumulative_eva_graph.png'
    main(input_file, output_file, graph_file)