def realizar_soma(mesa_escolhida, mesas):
  for mesa in mesas:
    if mesa_escolhida == mesa['numero_mesa']:

      for pedido in mesa['comanda']:
        mesa['conta'] += sum(pedido.values())

      return mesa

def gerar_conta():

  import mesa, random

  num_aleatorio = random.randint(1, 100)

  mesas = mesa.pegar_mesas()
  existe_mesa = False
  
  while True:

    mesa_escolhida = int(input("Indique a mesa a qual será gerado a conta: "))

    for mesa in mesas:

      if mesa_escolhida == mesa['numero_mesa']:
        existe_mesa = True
        break
      else:
        continue
    
    if existe_mesa:
      break
    else:
      print("A mesa indicada não está cadastrada no sistema!")
  
  mesa = realizar_soma(mesa_escolhida, mesas)
  
  arquivo = open(f'Notas/conta{num_aleatorio}.txt', 'w')

  for mesa in mesas:
    if mesa_escolhida == mesa['numero_mesa']:
      arquivo.write(f"{mesa['numero_mesa']}, {mesa['quantidade_clientes']}, {mesa['comanda']}, {mesa['conta']}")
  
  arquivo.close()

  return mesa


