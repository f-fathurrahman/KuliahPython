import pandas as pd
import numpy as np

# the bad way: using Python tuples as keys
index = [("California", 2000),
         ("California", 2010),
         ("New York", 2000),
         ("New York", 2010),
         ("Texas", 2000),
         ("Texas", 2010)]
populations = [33871648, 37253956,
               18976457, 19378102,
               20851820, 25145561]
pop = pd.Series(populations, index=index)
print(pop)

# using Pandas multiindex
# initialize from tuples
index = pd.MultiIndex.from_tuples(index)
print(index)
# MultiIndex contains multiple levels of indexing: the state names and
# the years as well as
# multiple labels for each data point which encode these levels

pop = pop.reindex(index)
print(pop)

# access all data for which the second index is 2010
print(pop[:,2010])

# access population for California
print(pop["California"])
print(type(pop["California"]))


# MultiIndex as extra dimension

# convert a multiply indexed Series into a conventionally indexed DataFrame:
pop_df = pop.unstack()
print(pop_df)

# the inverse of unstack()
print(pop_df.stack())
print(type(pop_df.stack()))


# create multiply indexed Series or DataFrame by passing a list of two or more
# index arrays to the constructor.
df = pd.DataFrame(np.random.rand(4,2),
                  index=[ ["a", "a", "b", "b"], [1, 2, 1, 2] ],
                  columns=["data1", "data2"])
print(df)

# Pass a dictionary with appropriate tuples as keys
data = { ("California", 2000): 33871648,
         ("California", 2010): 37253956,
         ("Texas", 2000): 20851820,
         ("Texas", 2010): 25145561,
         ("New York", 2000): 18976457,
         ("New York", 2010): 19378102}

print(pd.Series(data))
