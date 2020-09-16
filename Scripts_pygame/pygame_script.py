# Importe de paquetes
import pygame
import random

"""
CONFIGURACIÓN GENERAL
"""
# Se inicializan todos los módulos de pygame
pygame.init()

# Se define el modo del display/ventana
ancho = 800
altura = 600
screen = pygame.display.set_mode((ancho, altura))

# Título e ícono
pygame.display.set_caption("Mi primer juego")
icon = pygame.image.load("graficos/spaceship.png") 
pygame.display.set_icon(icon)  # No funcionará dependiendo del tema que usen en su SO

# Parámetros iniciales de objetos del juego
# Jugador
player_img = pygame.image.load("graficos/spaceship_player.png")
size = player_img.get_size()
playerX = ancho/2 - size[0]/2  # La posición debe tomar en cuenta el tamaño de 
                               # la imagen en sí
playerY = round(0.8*altura)
speedX = 0

# Alien
alien_img = pygame.image.load("graficos/alien.png")
alienX = random.randint(0, ancho - size[0])
franja_enemigos = random.randint(round(size[1]/2), 0.2*altura)

# Controlador del while para apertura y cerradura de la ventana
running = True


"""
ELEMENTOS Y SISTEMAS DEL JUEGO
"""
# Clases 
class Flotador:

    def __init__(self, x, y, img, mov_rate = 0.3, speedX = 0):
        self.img = img
        self.size = self.img.get_size()
        self.x, self.y = x, y
        self.speedX = speedX
        self.mov_rate = mov_rate
        self.actualizar_posicion()

    def actualizar_posicion(self):
        self.x += self.speedX
        screen.blit(self.img, (self.x, self.y))

    def check_boundary(self):
        borde_izquierdo = 0
        borde_derecho = ancho - self.size[0]
        xPosition = self.x
        if xPosition <= borde_izquierdo:
            self.x = borde_izquierdo
        elif xPosition >= borde_derecho:
            self.x = borde_derecho

class Enemigo(Flotador):

    def __init__(self, x, y, img, mov_rate = 0.3, speedX = 0.5):
        super().__init__(x, y, img, mov_rate, speedX = speedX)

    def check_boundary(self):
        borde_izquierdo = 0
        borde_derecho = ancho - self.size[0]
        xPosition = self.x
        if xPosition <= borde_izquierdo:
            self.speedX = self.mov_rate
        elif xPosition >= borde_derecho:
            self.speedX = -self.mov_rate



# Inicialización de datos y objetos:
cohete = Flotador(playerX, playerY, player_img)
alien = Enemigo(alienX, 0.2*altura, alien_img)

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
                cohete.speedX = -cohete.mov_rate
            if event.key == pygame.K_RIGHT:
                cohete.speedX = +cohete.mov_rate

        # KEYUP: Reacción a teclas levantadas
        key = pygame.key.get_pressed()
        if event.type == pygame.KEYUP:
            if any([key[pygame.K_LEFT], key[pygame.K_RIGHT]]):
                if key[pygame.K_LEFT]:
                    cohete.speedX = -cohete.mov_rate
                else:
                    cohete.speedX = +cohete.mov_rate
            else:
                cohete.speedX = 0

    """
    ACTUALIZACIÓN DE LA PANTALLA:
    - Fondo
    - Posición del jugador
    """
    # Fondo: Red, Green, Blue
    screen.fill((0, 140, 205))

    # Cambio de estado de los objetos
    cohete.actualizar_posicion()
    alien.actualizar_posicion()

    # Colisiones con el borde de la pantalla
    cohete.check_boundary()
    alien.check_boundary()

    # Actualizando los cambios
    pygame.display.update()
