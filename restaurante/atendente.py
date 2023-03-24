from mesa import *
from relatorio_diario import *

while True:
  print("1 - Cadastrar uma mesa")
  print("2 - Anotar um pedido")
  print("3 - Gerar conta")
  print("4 - Fechar o dia")
  opcao = int(input("Escolha umas das opções acima: "))

  match opcao:
      case 1:
          cadastrar_mesa()
      case 2:
          adicionar_comanda()
      case 3:
          adicionar_conta()
      case 4:
          gerar_relatorio_diario()
          break
      case _:
          break

