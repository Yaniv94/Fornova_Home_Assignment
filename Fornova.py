import json

json_file_path = 'package.json'
output_file_path = 'output.txt'


# Function to calculate the total price (net price + taxes)
def calculate_total_price(net_price, taxes):
    total_tax = sum([float(tax) for tax in taxes.values()])
    return net_price + total_tax


# Read the JSON file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Extract relevant data from the JSON
shown_prices = data['assignment_results'][0]['shown_price']
net_prices = data['assignment_results'][0]['net_price']
number_of_guests = data['assignment_results'][0]['number_of_guests']
taxes_data = json.loads(data['assignment_results'][0]['ext_data']['taxes'])

cheapest_price = None
cheapest_room_type = None
cheapest_guests = number_of_guests
room_price_details = []

# Iterate over the shown_price dictionary to find the cheapest room and calculate total prices
for room_type, price in shown_prices.items():

    price_float = float(price)

    # Check if this room has the lowest price so far
    if cheapest_price is None or price_float < cheapest_price:
        cheapest_price = price_float
        cheapest_room_type = room_type
        cheapest_guests = number_of_guests

    # Calculate the total price for the current room (net price + taxes)
    net_price_float = float(net_prices[room_type])
    total_price = calculate_total_price(net_price_float, taxes_data)

    # Append the room details and total price to the list
    room_price_details.append(f"Room Type: {room_type}, Total Price: {total_price:.2f}")

# Write the results to an output file
with open(output_file_path, 'w') as output_file:
    # Task a
    output_file.write(f"a. Cheapest Price: {cheapest_price}\n\n")

    # Task b
    output_file.write(f"b. Cheapest Room Type: {cheapest_room_type}\n"
                      f"   Number of Guests in the Cheapest Room: {cheapest_guests}\n\n")
    # Task c
    output_file.write("c. Total prices for all rooms:\n")
    for detail in room_price_details:
        output_file.write(detail + '\n')

    # Explanation of how I calculated task c
    output_file.write("\n\n")
    output_file.write(
        f"This is how I calculated the total prices including taxes:\n"
        "Total Taxes = 14.70 (TAX) + 4.01 (City tax) = 18.71\n"
        f"I added 18.71 to the prices of all rooms. For example, the total price of the cheapest room with taxes included is {cheapest_price} + 18.71 = {cheapest_price + 18.71:.2f}.\n"
    )


#Besides writing the results to the output file, I have also added the results to the console:
# Task a
print(f"a. Cheapest Price: {cheapest_price}")

# Task b
print(f"b. Cheapest Room Type: {cheapest_room_type}\n Number of Guests in the Cheapest Room: {cheapest_guests}")

# Task c
print("\nc. Total prices for all rooms:")
for detail in room_price_details:
    print(detail)

# Explanation of how I calculated task c
print(f"\nThis is how I calculated the total prices including taxes:\n"
      "Total Taxes = 14.70 (TAX) + 4.01 (City tax) = 18.71\n"
      f"I added 18.71 to the prices of all rooms. For example, the total price of the cheapest room with taxes included is {cheapest_price} + 18.71 = {cheapest_price + 18.71:.2f}.")
