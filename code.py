item = input("what item would you like buy?:" )
price = float(input("what is the price?:" ))
quality = int(input("how many would you like the buy?:"))

total = price * quality

print(f"you have bought {quality} x  {item}/s") # type: ignore
print(f"Your total is:${total}") # type: ignore