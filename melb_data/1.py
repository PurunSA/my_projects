import pandas as pd

url = 'https://raw.githubusercontent.com/PurunSA/my_projects/refs/heads/main/melb_data/melb_data_ps.csv'
data = pd.read_csv(url)
print(data.head())