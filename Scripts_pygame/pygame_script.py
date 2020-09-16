# Importe de paquetes
import pygame
import random

"""
CONFIGURACIÓN GENERAL
"""
# Se inicializan todos los módulos de pygame
pygame.init()

# Se define el modo del display/ventana
ancho = 600
altura = 600
screen = pygame.display.set_mode((ancho, altura))
background = pygame.image.load("graficos/fondo.jpg")
background = pygame.transform.scale(background, (ancho, altura)) # Reescalamiento

# Título e ícono
pygame.display.set_caption("Mi primer juego")
icon = pygame.image.load("graficos/spaceship.png") 
pygame.display.set_icon(icon)  # No funcionará dependiendo del tema que usen en su SO

# Parámetros iniciales de objetos del juego
# Configuración
game_speed = 2

# Jugadores
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

# Proyectil
bullet_img = pygame.image.load("graficos/bullet.png")

# Controlador del while para apertura y cerradura de la ventana
running = True


"""
ELEMENTOS Y SISTEMAS DEL JUEGO
"""
# Clases 
class Flotador:

    def __init__(self, x, y, img, mov_rate = 1.5, speedX = 0):
        self.img = img
        self.size = self.img.get_size()
        self.x, self.y = x, y
        self.speedX = speedX
        self.mov_rate = mov_rate*game_speed
        self.actualizar_posicion()

    def actualizar_posicion(self):
        self.x += self.speedX
        screen.blit(self.img, (self.x, self.y))

    def check_boundary(self):
        borde_izquierdo = 0
        borde_derecho = ancho - self.size[0]
        if self.x <= borde_izquierdo:
            self.x = borde_izquierdo
        elif self.x >= borde_derecho:
            self.x = borde_derecho

class Enemigo(Flotador):

    def __init__(self, x, y, img, speedX = None, approaching_speed = 0.05):
        if speedX is not None:
            self.speedX = random.choice([-speedX, speedX])
        else:
            self.speedX = random.choice([-game_speed, game_speed])
        super().__init__(x, y, img, speedX = self.speedX)
        self.approaching_speed = approaching_speed 

    def check_boundary(self):
        borde_izquierdo = 0
        borde_derecho = ancho - self.size[0]
        xPosition = self.x
        if xPosition <= borde_izquierdo:
            self.speedX = - self.speedX
            self.y += self.approaching_speed*altura 
        elif xPosition >= borde_derecho:
            self.speedX = - self.speedX
            self.y += self.approaching_speed*altura 

class Bala(Flotador):

    def __init__(self, x, y, img, emisor, speedX = 0):
        self.disparado = False
        self.emisor = emisor
        super().__init__(x, y, img, speedX = speedX)

    def fire(self):
        self.disparado = True
        x = self.x + self.emisor.size[0]/2 - self.size[0]/2 # ajuste a los tamaños del
                                                            # emisor de la bala
        screen.blit(self.img, (x, self.y))

    def actualizar_posicion(self):
        if self.disparado:
            self.y -= self.mov_rate
            self.fire()
        # Una vez que la bala llega al final de la pantalla
        # regresamos su estado a la posicion del cohete y disparado = False
        if self.y <= 0:  
            self.disparado = False
            self.x, self.y = self.emisor.x, self.emisor.y


# Inicialización de datos y objetos:
cohete = Flotador(playerX, playerY, player_img)
alien = Enemigo(alienX, 0.2*altura, alien_img)
bala_normal = Bala(playerX, playerY, bullet_img, cohete)

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
            if event.key == pygame.K_SPACE:
                bala_normal.fire()

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
    #screen.fill((0, 140, 205))
    screen.blit(background, (0,0))

    # Cambio de estado de los objetos
    cohete.actualizar_posicion()
    alien.actualizar_posicion()
    bala_normal.actualizar_posicion()

    # Colisiones con el borde de la pantalla
    cohete.check_boundary()
    alien.check_boundary()

    # Actualizando los cambios
    pygame.display.update()