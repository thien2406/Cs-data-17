product = {
    "id": 1,
    "name": "Boseon",
    "price": 150000,
    "quantity": 10
}
print(product["name"])

product["price"]=18000

print(product["price"])

product["category"]= "Laptop"

del product["quantity"]

print(product)