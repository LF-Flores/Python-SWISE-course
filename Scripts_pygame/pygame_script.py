# Importe de paquetes
import pygame

# Se inicializan todos los módulos de pygame
pygame.init()

# Se define el modo del display/ventana
screen = pygame.display.set_mode((800, 600))

# Título e ícono
pygame.display.set_caption("Mi primer juego")
icon = pygame.image.load("graficos/spaceship.png") 
pygame.display.set_icon(icon)  # No funcionará dependiendo del tema que usen en su SO

# Posición inicial del jugador
player_img = pygame.image.load("graficos/spaceship_player.png")
playerX = 400 - 64/2  # La posición debe tomar en cuenta el tamaño de la imagen en sí
playerY = 480

# Controlador del while para apertura y cerradura de la ventana
running = True

def player(x,y):
    screen.blit(player_img, (x,y))


# Ciclo de repetición del juego
while running:
    for event in pygame.event.get():  # <-- Recolector de eventos que suceden en CADA 
                                      #     iteración del while
        
        # Cerrar el juego cuando el evento recibido sea el de salir de la ventana
        if event.type == pygame.QUIT: 
            running = False

    ## Actualización de la pantalla
    # Red, Green, Blue
    screen.fill((0, 140, 205))

    # acción del jugador
    player(playerX, playerY)
    pygame.display.update() 

    
            