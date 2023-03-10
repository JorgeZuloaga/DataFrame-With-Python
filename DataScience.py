import pandas as pd

import matplotlib

matplotlib.style.use("ggplot")

colors = ["#006D2C", "#31AAAA" , "#74C476"]

data = {"Year":[2011,2012,2013,2014,2015,2016,2017,2018,2019],
        "Month":["Jan", "Feb", "Mar","Jan", "Feb", "Mar","Jan", "Feb", "Mar"],
        "Value":[1,2,3,4,5,6,7,8,9]}

pivot_df = pd.DataFrame(data)

pivot_df=pd.pivot(pivot_df,index="Year",columns="Month", values="Value");

pivot_df.loc[:,["Jan", "Feb", "Mar"]].plot.bar(stacked=True, color = colors, figsize = (10,7))