
# Read data with time index..............................................................
# Import the pandas library as pd.
# Read in the data from a CSV file called 'climate_change.csv' using pd.read_csv.
# Use the parse_dates key-word argument to parse the "date" column as dates.
# Use the index_col key-word argument to set the "date" column as the index.

# Import pandas as pd
import pandas as pd

# Read the data from file using read_csv
climate_change = pd.read_csv('climate_change.csv',parse_dates=["date"],index_col="date")
