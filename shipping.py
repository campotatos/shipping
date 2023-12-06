# This program determines the cheapest shipping method and cost of shipping based off of weight of their package

# declaring weight variable
weight = float(input())

# ground shipping
two_lbs = weight * 1.50 + 20.00
six_lbs = weight * 3.00 + 20.00
ten_lbs = weight * 4.00 + 20.00
over_ten = weight * 4.75 + 20.00

if weight <= 2:
    print(two_lbs)
elif weight <= 6:
    print(six_lbs)
elif weight <= 10:
    print(ten_lbs)
elif weight >= 10:
    print(over_ten)

# declaring variable for premium ground shipping
prem_grd_ship = 125.00
print(prem_grd_ship)

# drone shipping
drone_two_lbs = weight * 4.50
drone_six_lbs = weight * 9.00
drone_ten_lbs = weight * 12.00
drone_over_ten = weight * 14.5

if weight <= 2:
    print(drone_two_lbs)
elif weight <= 6:
    print(drone_six_lbs)
elif weight <= 10:
    print(drone_ten_lbs)
elif weight >= 10:
    print(drone_over_ten)

