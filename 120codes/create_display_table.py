#create and display data in a tabular format
#create tables using the tabulate module
#tabluate module is not inbuilt so install it from cmd using pip install tabulate

from tabulate import tabulate
data = [["Name", "Place", "Gender"], ["Aman", "New Delhi", "Male"], ["Hritika", "New Delhi", "Female"], ["Krishna", "UP", "Male"]]
print(tabulate(data))
print("\r")

#separate the headers from the values
print("Separating headers from values: ")
print(tabulate(data, headers='firstrow'))
print("\r")

#separate the headers from the values by adding a grid
print("Separating headers from values by adding a grid: ")
print(tabulate(data, headers='firstrow', tablefmt='grid'))
print("\r")

print("Separating headers from values by adding a fancy grid: ")
print(tabulate(data, headers='firstrow', tablefmt='fancy_grid'))
