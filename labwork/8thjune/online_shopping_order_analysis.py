sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

#display product sold more than 20 times
print("Products sold more than 20 times")
for product, quantity in sales.items():
    if quantity>20:
     print(product)

## 2. Find the best-selling product
best=max(sales,key=sales.get)
print("Best selling products:\n",best,f"({sales[best]})")

## 3. Find the least-selling product
least=min(sales,key=sales.get)
print("Least sold product :\n",least,f"({sales[least]})")

# 4. Calculate total products sold
total=sum(sales.values())
print("Total selling:",total)

# 5. Create a list of products requiring promotion (sales < 15)
promotion = []
for product, quantity in sales.items():
    if quantity < 15:
        promotion.append(product)

print("Products Requiring Promotion:", promotion)

# 6. Count products having sales between 10 and 30
count = 0
for quantity in sales.values():
    if 10 <= quantity <= 30:
        count += 1

print("Products Having Sales Between 10 and 30:", count)
   
