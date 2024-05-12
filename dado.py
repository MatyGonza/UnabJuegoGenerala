
def tirar_dados():
  """Tira 5 dados y devuelve una lista con los resultados."""
  return [random.randint(1, 6) for _ in range(5)]

def retener_dados(dados, indices):
  """Devuelve una nueva lista con los dados retenidos y actualiza la lista original.

  Args:
    dados: Lista con los resultados de los dados.
    indices: Lista de índices de los dados a retener.
  """
  dados_retenidos = [dados[i] for i in indices]
  dados[:] = [d for i, d in enumerate(dados) if i not in indices]
  return dados_retenidos

def seleccionar_dados(dados):
  """Solicita al usuario que seleccione los dados a retener y devuelve la selección.

  Args:
    dados: Lista con los resultados de los dados.
  """
  print("Dados:", dados)
  indices = []
  while True:
    indice = int(input("Ingrese el índice del dado a retener (o 0 para terminar): "))
    if indice == 0:
      break
    if 0 < indice <= len(dados):
      indices.append(indice - 1)
      dados[:] = retener_dados(dados, indices)
    else:
      print("Índice inválido.")
  return indices