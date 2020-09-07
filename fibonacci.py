while True:

  n=int(input('Seleccione el n numero a convertir'))

  if n > 2:

    break

x=[0,1]

for i in range(n-2):

  x.append(x[-1]+x[-2])

print(x)

 