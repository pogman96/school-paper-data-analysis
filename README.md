# Purpose
 For math exploration paper IB Math SL2 Block 3

# Explanation of main.py
 main.py is used as the data analyzer, it takes in raw historical data and outputs
 parsed and 7-day average data, seen in their respective folders.

# Replication of data analysis
 main.py requires the 'csv' and 'os' library to be used, as a result, a windows os is required.
 Folders with case sensitive matching names must be present in the directory of main.py to output correctly.
 
# Use of visualGraph.py
 visualGraph requires the 'pandas' and 'plotly.express' libraries to function, after correct
 installation, running the python file will allow to user to query and retrieve different graphs of the data
 (7 day moving average), (raw)

# Step by step replication
 1. Install python version 3+
 2. Navigate to python install folder and then double click the "Scripts" folder
 example path("C:\Users\Name\AppData\Local\Programs\Python\Python39\Scripts")
 3. Open windows powershell by shift-rightclicking empty space, then type 'pip install plotly' and 'pip install pandas' seperately, pressing enter in between uses
 4. Clone the testing branch, and extract to a folder
 5. Run main.py by double clicking to parse and process data
 6. Run visualGraph.py by double clicking to select interactive graphs
