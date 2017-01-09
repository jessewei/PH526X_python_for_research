# HarvardX PH526X Week 4 Video 4.1.1 Getting Started With Pandas
# Pandas has Series (1d array-like) and DataFrame (2d array-like)

import pandas as pd

#/----------PANDAS SERIES----------/

# series with number index
x = pd.Series([6, 3, 8, 6])
print(x)

# series with letter index
x = pd.Series([6, 3, 8, 6], index=["q", "w", "e", "r"])
print(x)
print(x["q"])
print(x[["w","e"]])

sorted_index = sorted(x.index)
print("sorted_index: ", sorted_index)
# reindex x using reindex method
sorted_x = x.reindex(sorted_index)
print("After x is sorted, x_sorted: ")
print(sorted_x)

# define a dictionary to pass to pandas
age = {"Tim":29, "Jim":24, "Pam":27, "Sam":32}
# construct Pandas Series by passing age in
x = pd.Series(age)
print(x)
print('x.index gives: ', x.index)

# construct x series with letter index
x = pd.Series([6, 3, 8, 6], index=["q", "w", "e", "r"])
# construct y series with letter index
y = pd.Series([7, 3, 5, 2], index=["e", "q", "r", "t"])
print("x is:")
print(x)
print("y is:")
print(y)
print("x + y gives:")
print(x + y)



#/----------PANDAS DATAFRAME----------/

# construct a dictionary to pass to pandas
data = {"name": ["Tim", "Jim", "Pam", "Sam"],
        "age": [29, 31, 27, 35],
        "ZIP": ["02115", "02130", "67700", "00100"]}

# construct pandas DataFrame
x = pd.DataFrame(data, columns=["name", "age", "ZIP"])
print(x)
print('x["name"] gives:')
print(x["name"])
print("x.name also gives:")
print(x.name)

