slices = party_pizza_mini + large + medium
print(f"Total_number_of_slices: {slices}")

people = people+1
share = people//slices
leftover = people%slices
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")

people = people+2 #Eric and Brandon are coming too.
share = people//slices
leftover = people%slices
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")
#Mom says ("Wait, Brandon’s coming. We’re going to need more pizza. I’ll upgrade the mini to a party_pizza instead. It’s the same as 2 minis. Hopefully the leftovers will be enough to fill his hollow leg.”)

slices = slices + party_pizza_mini
share = slices//people
leftover = people%slices
print(f"Each person gets: {share}")
print(f"Leftover slices: {leftover}")
print("...for Mr. Hollow Leg")
