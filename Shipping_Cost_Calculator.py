# Shipping Cost Calculator

## Input weight of package and rate of shipping
weight = float(input("Enter the weight of shipment"))
rate = float(input("Enter rate per kilogram"))

# Calculate the shippig cost 
shipping_cost = weight*rate

# Display the Shipping Cost
print(f"Shipping Cost : {shipping_cost} USD")
