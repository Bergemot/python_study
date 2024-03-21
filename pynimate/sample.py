from matplotlib import pyplot as plt
import pandas as pd
import pynimate as nim

# sample data
df = pd.DataFrame(
    {
        "time": ["1960-01-01", "1961-01-01", "1962-01-01"],
        "Afghanistan": [1, 2, 3],
        "Angola": [2, 3, 4],
        "Albania": [1, 2, 5],
        "USA": [5, 3, 4],
        "Argentina": [1, 4, 5],
    }
).set_index("time")

# a Canvas object is created using pynimate.
cnv = nim.Canvas()

# A Barplot object is created using the DataFrame df, 
# specifying the format of the dates in the time column as "%Y-%m-%d", 
# and the dimension of the plot as "2d". 
bar = nim.Barplot(df, "%Y-%m-%d", "2d")

bar.set_time(callback=lambda i, datafier: datafier.data.index[i].strftime("%b, %Y"))
cnv.add_plot(bar)
cnv.animate()
plt.show()