# Importe de paquetes
import pygame

"""
CONFIGURACIÓN GENERAL
"""
# Se inicializan todos los módulos de pygame
pygame.init()

# Se define el modo del display/ventana
ancho = 600
altura = 600
screen = pygame.display.set_mode((ancho, altura))

# Título e ícono
pygame.display.set_caption("Mi primer juego")
icon = pygame.image.load("graficos/spaceship.png") 
pygame.display.set_icon(icon)  # No funcionará dependiendo del tema que usen en su SO

# Parámetros iniciales de objetos del juego
player_img = pygame.image.load("graficos/spaceship_player.png")
alien_img = pygame.image.load("graficos/alien.png")
size = player_img.get_size()
playerX = ancho/2 - size[0]/2  # La posición debe tomar en cuenta el tamaño de 
                               # la imagen en sí
playerY = round(0.8*altura)
speedX = 0

# Controlador del while para apertura y cerradura de la ventana
running = True


"""
ELEMENTOS Y SISTEMAS DEL JUEGO
"""
# Clases 
class Flotador:

    def __init__(self, x, y, img, mov_rate = 0.3):
        self.img = img
        self.size = self.img.get_size()
        self.x, self.y = x, y
        self.actualizar_posicion(x, y)
        self.mov_rate = mov_rate

    def actualizar_posicion(self, x=None, y=None):
        x = self.x if x is None else x 
        y = self.y if y is None else y    
        screen.blit(self.img, (x,y))

# Inicialización de datos y objetos:
cohete = Flotador(playerX, playerY, player_img)
alien = Flotador(playerX, 0.2*altura, alien_img)

# Ciclo de repetición del juego
while running:
    for event in pygame.event.get():  # <-- Recolector de eventos que suceden en CADA 
                                      #     iteración del while
 
        """
        TIPOS DE EVENTOS:
        - QUIT: Cerrar el juego
        - KEYDOWN: Alguna tecla presionada
        - KEYUP: Alguna tecla levantada
        """       
        # QUIT: Cerrar el juego cuando el evento recibido sea el de salir de la ventana
        if event.type == pygame.QUIT: 
            running = False

        # KEYDOWN: Reacción a teclas presionadas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedX = -cohete.mov_rate
            if event.key == pygame.K_RIGHT:
                speedX = +cohete.mov_rate

        # KEYUP: Reacción a teclas levantadas
        key = pygame.key.get_pressed()
        if event.type == pygame.KEYUP:
            if any([key[pygame.K_LEFT], key[pygame.K_RIGHT]]):
                if key[pygame.K_LEFT]:
                    speedX = -cohete.mov_rate
                else:
                    speedX = +cohete.mov_rate
            else:
                speedX = 0

    """
    ACTUALIZACIÓN DE LA PANTALLA:
    - Fondo
    - Posición del jugador
    """
    # Fondo: Red, Green, Blue
    screen.fill((0, 140, 205))

    # Cambio de estado del cohete
    playerX += speedX
    cohete.actualizar_posicion(playerX, playerY)
    alien.actualizar_posicion()

    # Colisiones con el borde de la pantalla
    borde_izquierdo = 0
    borde_derecho = ancho - cohete.size[0]
    if playerX <= borde_izquierdo:
        playerX = borde_izquierdo
    elif playerX >= borde_derecho:
        playerX = borde_derecho

    # Actualizando los cambios
    pygame.display.update() 
