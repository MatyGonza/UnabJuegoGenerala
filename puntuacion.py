def calcular_puntuacion(dados):
  """Calcula la puntuación de una tirada de dados según las reglas del juego.

  Args:
    dados: Lista con los resultados de los dados.
  """
  # Implementar la lógica para calcular la puntuación de cada combinación
  # (escalera real, poker, generala, etc.) y devolver la puntuación correspondiente.
  pass

# Ejemplo de cálculo de puntuación para una generala
def es_generala(dados):
  return len(set(dados)) == 1

def calcular_puntuacion_generala(dados):
  if es_generala(dados):
    return 50 if len(dados) == 5 else 60
  return 0