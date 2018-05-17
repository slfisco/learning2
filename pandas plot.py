#pandas plot test
import pandas as pd
import matplotlib.pyplot as pp

file = pd.read_csv("testcsv.csv")
print(file)
#print(file.dtypes)
pp.plot(file["Entry"],file["Value"])
pp.show()
