length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
height = float(input("Enter height: "))
cost = float(input("Enter painting cost per square meter: "))

# Area of four walls
area = 2 * (length + breadth) * height

# Total painting cost
total_cost = area * cost

print("Total cost of painting =", total_cost)