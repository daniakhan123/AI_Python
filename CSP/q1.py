# Input products and slots
products = [
    {"id": "P1", "frequency": 15, "volume": 2},
    {"id": "P2", "frequency": 8, "volume": 1},
    {"id": "P3", "frequency": 20, "volume": 3}
]

slots = [
    {"id": "S1", "distance": 1, "capacity": 3},
    {"id": "S2", "distance": 2, "capacity": 3},
    {"id": "S3", "distance": 3, "capacity": 3}
]

# Sort by frequency (descending) and distance (ascending)
products.sort(key=lambda p: -p["frequency"])
slots.sort(key=lambda s: s["distance"])

assignments = []

for product in products:
    assigned = False
    for slot in slots:
        if slot["capacity"] >= product["volume"]:
            assignments.append({
                "product": product["id"],
                "slot": slot["id"],
                "distance": slot["distance"],
                "cost": product["frequency"] * slot["distance"]
            })
            slot["capacity"] -= product["volume"]
            assigned = True
            break
    if not assigned:
        print(f"Product {product['id']} could not be assigned.")

# Output
print("\n✅ Product Assignments:")
total_cost = 0
for a in assignments:
    
    print(f"{a['product']} -> {a['slot']} (Distance: {a['distance']}, Cost: {a['cost']})")
    total_cost += a["cost"]

print(f"\nTotal Walking Distance Cost: {total_cost}")
