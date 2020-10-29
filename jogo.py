import pygame
from random import uniform 
pygame.init()

background = pygame.image.load('estrada.jpg')
carro1 = pygame.image.load('carro.png')
carro2 = pygame.image.load('carro2.png')
carro3 = pygame.image.load('carro2.png')
x = 300
y = 500
carrosFixosX = 300
carrosFixosY = 500
velocidade =  20 #quantos pixels vai andar

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Jogo de Corrida - FIF 201")
janela_aberta = True
while(janela_aberta):
    
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    elif comandos[pygame.K_DOWN]:
        y += velocidade
    elif comandos[pygame.K_RIGHT]:
        x += velocidade
    elif comandos[pygame.K_LEFT]:
        x -= velocidade

    carrosFixosY -= velocidade
    if(carrosFixosY < 0):
        carrosFixosY = 600
    janela.fill((128,128, 128))
    janela.blit(background, (0,0))
    janela.blit(carro1, (x,y))
    janela.blit(carro2, (carrosFixosX,carrosFixosY-200))
    janela.blit(carro3, (carrosFixosX+100,carrosFixosY))

    pygame.display.update()
pygame.quit()