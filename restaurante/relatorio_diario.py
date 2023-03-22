def gerar_relatorio_diario():

  import openpyxl, mesa

  mesas = mesa.pegar_mesas()
  wb = openpyxl.Workbook()

  ab = wb['Sheet']
  ab.title = "Relatório"

  linha = 1

  ab['A1'] = "Mesas"

  for mesa in mesas:
    ab[f'A{linha+1}'] = f"{mesa['numero_mesa']}"
    linha += 1

  linha = 1

  ab['B1'] = "Quantidade de Clientes"

  for mesa in mesas:
    ab[f'B{linha+1}'] = f"{mesa['quantidade_clientes']}"
    linha += 1

  linha = 1

  ab['C1'] = "Comandas"

  for mesa in mesas:
    ab[f'C{linha+1}'] = f"{mesa['comanda']}"
    linha += 1

  linha = 1

  ab['D1'] = "Contas"

  for mesa in mesas:
    ab[f'D{linha+1}'] = f"{mesa['conta']}"
    linha += 1

  wb.save("relatorio_diario.xlsx")
