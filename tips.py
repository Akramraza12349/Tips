
# tip1
from collections import Counter
import sys
data = [1, 2, 3, -4, -5]
for i in range(len(data)):
    if data[i] < 0:
        data[i] = 0
print(data)


data = [1, 2, 3, -4, -5]

for idx, num in enumerate(data):
    if num < 0:
        data[idx] = 0
print(data)


# tip2 use list comprehension instead of for loop

squares = [i*i for i in range(len(data))]
print(squares)


# tip3 we can use any iterable whether list, tuple
data = (2, 3, 41, 1, 10, 9)
sorted_data = sorted(data, reverse=True)
print(sorted_data)


data = [{"name": "Max", "age": 6}, {
    "name": "Lisa", "age": 16}, {"name": "Saba", "age": 20}]
sorted_data = sorted(data, key=lambda x: x["age"])
print(sorted_data)

sorted_data = sorted(data, key=lambda x: x["age"], reverse=True)
print(sorted_data)


# 4 store unique values with Sets
my_list = [1, 2, 3, 332, 55, 55, 5, 5]
my_set = set(my_list)
print(my_set)


# 5 save memory with generators
my_list = [i for i in range(10000)]
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")
my_list = (i for i in range(10000))
print(sum(my_list))
print(sys.getsizeof(my_list), "bytes")


# 6 define default values in dictionaries with .get() and .setdefault()

my_dict = {"item": "football", "price": 10}


# count = my_dict["count"] instead use below
count = my_dict.get("count")
count = my_dict.setdefault("count", 0)

print(count)


# 7 count hashable objects with collections.counter
my_list = [10, 20, 10, 20, 12, 12, 12, 12, 12, 2, 2, 2, 2]
counter = Counter(my_list)
print(counter)
most_common = counter.most_common(2)
print(most_common)

# 8 concat strings with .joins
list_of_strings = ["Hello", "my", "friends"]
my_string = " ".join(list_of_strings)
print(my_string)

# 9 merge two dictionaries
d1 = {"name": "Alex", "age": 25}
d2 = {"name": "Alex", "city": "New York"}

merged_dict = {**d1, **d2}
print(merged_dict)

# 10 simplify if statements for multiple checks
colors = ["green", "yellow", "red"]
