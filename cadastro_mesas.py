# Passo 1

mesas = list()
mesas_disponiveis = [1, 2, 3, 4, 5]
    
while True:

  if mesas_disponiveis == []:
     print("Todas as mesas estão lotadas!")

  print("Mesas disponíveis:")
  for mesa in mesas_disponiveis:
      print(f"[{mesa}]", end="")
  print()

  num_mesa = int(input("Escolha uma das mesas dispníveis: "))

  if num_mesa in mesas_disponiveis:
     mesas_disponiveis.remove(num_mesa)
     break
  else:
     print("A mesa não existe ou está ocupada!")

while True:
   
   qtd_clientes = input("Digite a quantidade de pessoas da mesa: ")

   if qtd_clientes.isnumeric() and float(qtd_clientes) - int(qtd_clientes) == 0:
      break
   else:
      print("O valor digitado não é válido!")

mesas.append({'numero_mesa': num_mesa, 'quantidade_clientes': qtd_clientes, 'comanda': None, 'conta': 0})
