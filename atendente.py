from mesa import *

while True:
  opcao = int(input("Escolha umas das opções acima: "))

  match opcao:
      case 1:
          cadastrar_mesa()
      case 2:
          adicionar_comanda()
      case _:
          break
  
print(pegar_mesas())

