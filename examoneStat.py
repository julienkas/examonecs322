import pandas as pd

terrorismStat= pd.read_csv("stats.csv")
terrorismStat.head().to_html("terrorismstat_head.html")