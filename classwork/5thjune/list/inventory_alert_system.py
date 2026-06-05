stock = [25, 5, 0, 12, 3, 18, 0, 30]

out_of_stock = 0
restock = []
available = 0
healthy_stock = []

for qty in stock:

    if qty == 0:
        out_of_stock += 1

    if qty < 10:
        restock.append(qty)

    if qty > 0:
        available += 1

    if qty >= 15:
        healthy_stock.append(qty)

print("Out of Stock Products:", out_of_stock)
print("Restock Required:", restock)
print("Available Products:", available)
print("Healthy Stock:", healthy_stock)
