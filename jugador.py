'''
Este módulo representa a cada jugador en el juego.
Almacena el nombre del jugador, su puntaje acumulado y las tiradas realizadas en cada turno.
Proporciona funciones para realizar las acciones del jugador, como tirar los dados, retener dados, seleccionar combinaciones y ver su puntaje.
'''

class Jugador:
  def __init__(self, nombre):
    self.nombre = nombre
    self.puntaje = 0
    self.tiradas = []

  def tirar_dados(self):
    self.tiradas.append(tirar_dados())

  def retener_dados(self):
    indices = seleccionar_dados(self.tiradas[-1])
    self.tiradas[-1] = retener_dados(self.tiradas[-1], indices)

  def seleccionar_combinacion(self):
    # Implementar la lógica para que el jugador seleccione una combinación
    pass

  def ver_puntaje(self):
    print(f"Jugador: {self.nombre}")
    print(f"Puntaje: {self.puntaje}")
    print(f"Tiradas: {self.tiradas}"