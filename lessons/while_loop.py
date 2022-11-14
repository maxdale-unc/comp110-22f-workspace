for x in [1, 2, 3]:
   print(x)

print("----------------")

ys: list[int] = [110, 120]
for y in ys:
  print(y)

i: int = 0
ys: list[int] = [110, 120]
while i < len(ys):
  y: int = ys[i]
  print(y)
  i += 1