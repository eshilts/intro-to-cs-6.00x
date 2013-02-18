def clip(lo, x, hi):
  '''
  Takes in three numbers and returns a value based on the value of x.
  Returns:
  - lo, when x < lo
  - hi, when x > hi
  - x, otherwise
  '''

  return min(max(lo, x), hi)

print clip(0, 1, 2)
print clip(1, 0, 2)
print clip(0, 2, 1)
