total = 0

for i in range(1, 6):
    price = float(input("Enter price of product " + str(i) + ": "))
    total = total + price

gst = total * 18 / 100
final_bill = total + gst

print("Total Price =", total)
print("GST =", gst)
print("Final Bill =", final_bill)