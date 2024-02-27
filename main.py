size = 5
cross = [[' ' for _ in range(size)] for _ in range(size)]
print(cross)
for i in range(size):
   cross[i][i] = '*'
   cross[i][size-i-1] = '*'



for row in cross:
   print(' '. join(row))
























