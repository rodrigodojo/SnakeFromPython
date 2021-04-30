py gamer

import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('BoxCat_Games_-_08_cpu_talk (1).mp')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin (1).wav')

largura = 640
altura = 480

x_cobra = int(largura/2)
y_cobra = int(altura/2)

x_maca = randint(40,600)
y_maca = randint(50,430)	

ponto = 0
fonte = pygame.font.sysfont('arial', 40, bold=True, italic=True)
	
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('jogo')
relogio = pygame.time.Clock()
lista_cobra = []

def aumenta_cobra(lista_cobra) -> recebe paramento lista desenha a cobra 
	for XeY in lista_cobra:   ->listas
	   pygame.draw.rect(tela, (0,255,0),(XeY[0],XeY[1],20, 20) ->cores ->pose��o


while True:
	relogio.tick(30)
	tela.fill(255,255,255)) -> ( cor do Fundo )

	mensagem =f'pontos: {pontos}'
	texto_formatado = fonte.render(mensagem,True,(0,0,0)) -> (cor do texto preto  0,0,0,)
	
	for event in pygame.event.get():
		if event.type == QUIT:
		   pygame.quit()
		   exit()
 		
		'''

if event.type == KEYDOWN:
	   if event.key == k_a:
		x = x - 20
	   if event.key == k_d:
		x = x + 20
	   if event.key == k_w:
		y = y - 20
	   if event.key == k_s:
		y = y + 20***


if pygame.key.get_pressed()[k_a]:
	x_cobra = x_cobra - 20
if pygame.key.get_pressed()[k_s]:
	x_cobra = x_cobra + 20
if pygame.key.get_pressed()[k_w]:
	y_cobra = y_cobra -20
if pygame.key.get_pressed()[k_s]:
	y_cobra = y_cobra +20

cobra = pygame.draw.rect(tela,(0,255,0), (x_cobra,y_cobra,20,20)) ->(cobra )
maca = pygame.draw.rect(tela,(255,0,0), (x_maca,y_maca,20,20))     _>(maca)

if cobra.colliderect(ma�a):
	x_maca randint(40,600)
	y_maca randint(50,430)
	pontos += 1
	barulho_colisao.play()


lista_cabeca = []
list_cabeca.append(x_cobra)  _>(2 lista corpo)
lista_cabeca.append(y_cobra)

lista_cobra.append(lista_cabeca)   ->loop

aumenta_cobra(lista_cobra)


	
tela.blit(texto_formatado,(450,40))


pygame.display.update()












______________________________________________________
(lista cobrinha) interacao do loop corpo da cobra 

lista
=[[x0,y0],[x1,y0],[x2,y0],[x3,y0],[x4,y0]