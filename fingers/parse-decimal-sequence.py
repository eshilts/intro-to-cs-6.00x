print "Enter a string of decimal numbers separated by commas (e.g. 1.23,4.567,8.9): "

decimal_string = raw_input("Decimal string: ")

number_string = ''
total = 0

for char in decimal_string:
  if char == ',':
    total += float(number_string)
    number_string = ''
  else:
    number_string += char

if number_string != '':
  total += float(number_string)

print "Total = ", total
