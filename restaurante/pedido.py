produtos_disponiveis = {'refrigerante': 1.5, 'hamburguer': 10.0, 'hot-dog': 9.50}
   
def anotar_pedido():

  import mesa

  mesas = mesa.pegar_mesas()
  produtos_escolhidos = list()
  resposta = "SIM"
  existe_mesa = False
    
  while True:

    mesa_escolhida = int(input("Indique a mesa a qual será feita o pedido: "))

    for mesa in mesas:
        if mesa_escolhida == mesa.get('numero_mesa'):
            existe_mesa = True
            break
        else:
          continue

    if existe_mesa:
      break
    else:
      print("A mesa indicada não está cadastrada no sistema!")

  while resposta == "SIM":

    print("Refeição - Preço(R$)")
    for produto in produtos_disponiveis.keys():
        print(f"{produto} - {produtos_disponiveis[produto]}")

    while True:

      produto_escolhido = input("Digite o nome do produto escolhido pelo(s) cliente(s): ").lower()

      if produto_escolhido in produtos_disponiveis.keys():
          produtos_escolhidos.append({produto_escolhido: produtos_disponiveis[produto_escolhido]})
          break
      else:
          print("A refeição escolhida não consta no cardápio!")

    while True:
      
      resposta = input("Deseja continuar a pedir outras refeições (Sim/Não)? ").upper()

      if resposta == "SIM" or resposta == "NÃO" or resposta == "NAO":
          break
      else:
          print("A resposta não é válida! Por favor, digite uma das respostas disponíveis!")
    
  for mesa in mesas:

    if mesa_escolhida == mesa.get('numero_mesa'):
      mesa['comanda'].extend(produtos_escolhidos)
      return mesa
    
    



  