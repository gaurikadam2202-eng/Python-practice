area = float(input("Enter area of one wall: "))

interior_cost = float(input("Enter interior painting cost per sq.ft: "))
exterior_cost = float(input("Enter exterior painting cost per sq.ft: "))

total_cost = area * (interior_cost + exterior_cost)

print("Total painting cost =",total_cost)