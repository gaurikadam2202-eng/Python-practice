radius = 20
length = 50
breadth = 40
cost_per_meter = 35

# Perimeter of the field
perimeter = 3.14 * radius + 2 * (length + breadth)

# Fencing 5 times
total_wire = perimeter * 5

# Total cost
total_cost = total_wire * cost_per_meter

print("Total cost of fencing =", total_cost)