import os
import pandas as pd

csv_path = os.path.join('static', 'data', 'cities.csv')
cities_csv = pd.read_csv(csv_path)

cities_csv.to_html('table.html', index=False, classes=['table', 'table-striped', 'table-hover'])