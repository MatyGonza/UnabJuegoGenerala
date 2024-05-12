'''
Este módulo controla el flujo general del juego.
Define la secuencia de turnos, gestiona la interacción con los jugadores y determina el ganador.
Muestra las tiradas de cada jugador, las puntuaciones y el estado actual del juego.
'''

from dados import tirar_dados, retener_dados, seleccionar_dados
from puntuacion import calcular_puntuacion
from jugador import Jugador

def iniciar_juego(jugador1, jugador2):
  # Inicializar el juego (mostrar instrucciones, etc.)
  pass

def jugar_turno(jugador):
  # Implementar el turno de un jugador (tirar dados, retener, seleccionar combinación)
  jugador.tirar_dados()
  for _ in range(2):
    jugador.retener_dados()
  jugador.seleccionar_combinacion()
  jugador.puntaje += calcular_puntuacion(jugador.tiradas[-1])

def mostrar_puntuaciones(jugador1, jugador2):
  jugador1.ver_puntaje()
  jugador2.ver_puntaje()

def determinar_ganador(jugador1, jugador2):
  # Implementar la lógica para determinar el ganador
  pass