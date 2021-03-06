import sys


def is_estetic(slice, L):
    ingredients = [ingredient for ingredient in [row for row in slice]]

    return ingredients.count(0) == L and ingredients.count(1) == L


def size(slice):
    return len(slice) * len(slice[0])


def backtrack(slice):
    if not is_estetic(slice):
        return
    if size(slice) == H:
        return slice

    better_slice = find_better_slice(slice)


def slice(pizza):
    return backtrack(pizza)


input_file_name = (len(sys.argv) > 1 and sys.argv[1]) or "datasets/example.in"

print(input_file_name)

input = open(input_file_name, "r")

str_args = input.readline().split(" ")
args = [int(str_arg) for str_arg in str_args]

[TOTAL_ROWS, TOTAL_COLS, L, H] = args

pizza = []

for row in input:
    pizza += [[1 if col == "T" else 0 for col in row]]

slices = slice(pizza)


print TOTAL_ROWS, TOTAL_COLS, L, H
print pizza
print slices
