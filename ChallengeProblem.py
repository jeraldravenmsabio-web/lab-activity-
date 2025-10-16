weight = float(input("Weight (lbs): "))
destination = input("Destination (domestic/international): ").lower()
membership = input("Membership (standard/premium): ").lower()
cost = 10
if weight > 20:
    cost += 5
if destination == "international":
    cost *= 2
if membership == "premium":
    cost *= 0.8
print(f"Final Shipping Cost: ${cost:.2f}")
