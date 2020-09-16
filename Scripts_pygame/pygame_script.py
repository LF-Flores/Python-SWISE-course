# Importe de paquetes
import pygame

# Se inicializan todos los módulos de pygame
pygame.init()

# Se define el modo del display/ventana
screen = pygame.display.set_mode((600, 600))

# Controlador del while para apertura y cerradura de la ventana
running = True

# Ciclo de repetición del juego
while running:
    for event in pygame.event.get():  # <-- Recolector de eventos que suceden en CADA 
                                      #     iteración del while
        pass
        
        # # Cerrar el juego cuando el evento recibido sea el de salir de la ventana
        # if event.type == pygame.QUIT: 
        #     running = False
            