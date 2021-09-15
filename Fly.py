import InsectClass as i

mosquito = i.Insect(2,4)
housefly = i.Insect(3,5)
# use this instead of hard-coding, get value from user if still needed 

mosquito.flight_length()

housefly.flight_length()

print("The mosquito can fly up to", mosquito.get_miles(), "miles")
print("The housefly can fly up to", housefly.get_miles(), "miles")

