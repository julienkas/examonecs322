import pandas as pd

terrorismloc= pd.read_csv("locations.csv")
terrorismloc.head().to_html("terrorism_head.html")