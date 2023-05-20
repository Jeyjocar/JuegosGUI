"""
28-02-2023
Librerías para Juegos
Jeyfrey Calero"""

import pygame

pygame.init()
time = pygame.time.Clock() #Velocidad del juego
fps = 60 #FtS fotogramas X Segundo
suelo = 150 #para ingresar el suelo PANEL
anchoPantalla = 800
altoPantalla = 400 + suelo
pantalla = pygame.display.set_mode((anchoPantalla, altoPantalla)) #esta va a heredar los valores de nuestra
pygame.display.set_caption("Battle War")
font = pygame.font.SysFont("Cambria", 30)
Background = pygame.image.load('Imagenes/fondo.png').convert_alpha()
red = (255,0,0)
green = (0,255,0)
sueloGame = pygame.image.load('Imagenes/suelo2.png').convert_alpha()


def mostrar_Texto(texto, fuente, color, x, y):
    img = font.render(texto, True, color)
    pantalla.blit(img, (x, y))

def dibujarFondo():
    pantalla.blit(Background, (0, 0))  #BLIT acomoda el fondo según las coordenadas de pantalla

def dibujarSuelo():
    pantalla.blit(sueloGame, (0, altoPantalla - suelo))
    mostrar_Texto(f'{heroe.nombre_personaje} HP{heroe.vida_maxima}', font, red, 100, 
                  altoPantalla-suelo+10)
    for count, i in enumerate(villanos):
        mostrar_Texto(f'{i.nombre_personaje} HP{i.vida_maxima}', font, green, 500,
                      (altoPantalla-suelo+10)+count*60)



class Personaje():
    def __init__(self, eje_x, eje_y, nombre_personaje, vida_maxima, fortaleza, posion):
        self.nombre_personaje = nombre_personaje
        self.vida_maxima = vida_maxima
        self.fortaleza = fortaleza
        self.iniciar_posion = posion
        self.posion = posion
        self.vivo = True
        self.animacion_estado = []
        self.indices = 0
        self.tipo_estado = 2
        self.time = pygame.time.get_ticks() #obtiene un intervalo aleatorio de tiempo
        load_state = []
        for i in range(8):
            My_imagen = pygame.image.load(f'imagenes/{nombre_personaje}/inactivo/{i}.png')
            My_imagen = pygame.transform.scale(My_imagen, (My_imagen.get_width()*4, My_imagen.get_height()*4))
            load_state.append(My_imagen)
        self.animacion_estado.append(load_state)

        for i in range(8):
            My_imagen = pygame.image.load(f'imagenes/{nombre_personaje}/atacar/{i}.png')
            My_imagen = pygame.transform.scale(My_imagen, (My_imagen.get_width()*4, My_imagen.get_height()*4))
            load_state.append(My_imagen)
        self.animacion_estado.append(load_state)

        self.imagen = self.animacion_estado[self.tipo_estado][self.indices] 

        self.rectangulo_imagen = self.imagen.get_rect()
        self.rectangulo_imagen.center = (eje_x, eje_y)
    
    def actualizar_Animacion(self):
        actions = 100
        self.imagen = self.animacion_estado[self.tipo_estado][self.indices]
        if pygame.time.get_ticks() - self.time > actions:
            self.time = pygame.time.get_ticks()
            self.indices += 1
        if self.indices >= len(self.animacion_estado[self.tipo_estado]):
            self.indices = 0

    def dibujar_Personaje(self):
        pantalla.blit(self.imagen, self.rectangulo_imagen)

class Barravida():
    def __init__(self, eje_x, eje_y, HP, vida_maxima):
        self.eje_x = eje_x
        self.eje_y = eje_y
        self.HP = HP
        self.vida_maxima = vida_maxima

    def DibujarBarravida(self, HP):
        pygame.draw.rectangle(pantalla, red (self.eje_x, self.eje_y, 150, 20))


heroe = Personaje(150, 305, "personajes",30, 10, 3)
villano1 = Personaje(500,320, "villano", 25, 8, 2)
villano2 = Personaje(700,320, "villano", 20, 6, 3)
villanos = []
Barravidaheroe = Barravida(100, altoPantalla + 40, heroe.fortaleza, heroe.vida_maxima)
villanos.append(villano1)
villanos.append(villano2)


pygame.display.set_caption('FirstGame')


def principal():
    jugar = True
    time.tick(fps) #TICK función predefinida de tiempo en PYTHON
    while jugar:
        dibujarFondo()
        dibujarSuelo()
        Barravidaheroe.DibujarBarravida(heroe.vida_maxima)
        heroe.actualizar_Animacion()
        heroe.dibujar_Personaje()

        for villano in villanos:
            villano.actualizar_Animacion()
            villano.dibujar_Personaje()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: # "QUIT" es cerrar
                jugar  = False
        pygame.display.update()
    pygame.quit()

if __name__=='__main__':
    principal()





