# format specifier = { value : flags } format a value based on what flag
#                    are inserted.

# .(number)f = Round to that many decimal places (Fixed point)
# :(number)  = Allocate that many spaces.
# :03        = Allocate and zero pad that many spaces.
# :<         = Left justify.
# :>         = Right justify.
# :^         = Center align.
# :+         = Use a plus sign to indicate positive value.
# :=         = Place sign to leftmost position.
# :          = Insert a space before positive numbers.
# :,         = Comma seperator.


price1 = 3.14159
price2 = -987.65
price3 = 12.34

print(f" price 1 is {price1:^}\n"
      f" price 2 is {price2:.2f}\n"
      f" price 3 is {price3:.2f}")

