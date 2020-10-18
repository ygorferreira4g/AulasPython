print("Digite o numero maximo do triangulo.\n")
print("Atenção, o numero deve ser impar.\n")
n = int(input("valor\n"))
print("\n")

if (n % 2 ==0):
  print("Número invalido.\n")
else:
  b = int((n - 1)/2)
  i =0
  for x in range(i, b+1):
    j=i+1
    for xx in range(i + 1, n-1):
      print(j, end="")
      j += 1
    print("\n ")
    i += 1
    n -= 1


