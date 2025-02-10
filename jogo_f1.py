import pygame
import sys

# Inicializando o pygame
pygame.init()

# Configurações de tela e cores
tamanho_tela = (800, 600)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Fórmula 1")
preto = (0, 0, 0)
branco = (255, 255, 255)

# Carregando a imagem do carro
carro_img = pygame.image.load("carro.png")  # Use uma imagem pequena de carro e ajuste o caminho
carro_img = pygame.transform.scale(carro_img, (50, 100))
carro_x = 375
carro_y = 500
velocidade_carro = 5
angulo_carro = 0

# Função de desenho da pista
def desenhar_pista():
    pygame.draw.rect(tela, branco, (150, 0, 500, 600))  # Retângulo principal da pista
    pygame.draw.rect(tela, preto, (200, 0, 400, 600))   # Interior da pista

# Função de rotação do carro
def rotacionar_carro(angulo):
    return pygame.transform.rotate(carro_img, angulo)

# Loop principal do jogo
rodando = True
while rodando:
    tela.fill(preto)  # Cor de fundo
    desenhar_pista()  # Desenho da pista
    
    # Eventos do jogo
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimentação do carro
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        angulo_carro += 5
    if teclas[pygame.K_RIGHT]:
        angulo_carro -= 5
    if teclas[pygame.K_UP]:
        carro_x -= int(velocidade_carro * pygame.math.sin(pygame.math.radians(angulo_carro)))
        carro_y -= int(velocidade_carro * pygame.math.cos(pygame.math.radians(angulo_carro)))
    if teclas[pygame.K_DOWN]:
        carro_x += int(velocidade_carro * pygame.math.sin(pygame.math.radians(angulo_carro)))
        carro_y += int(velocidade_carro * pygame.math.cos(pygame.math.radians(angulo_carro)))

    # Desenhando o carro na tela
    carro_rotacionado = rotacionar_carro(angulo_carro)
    carro_rect = carro_rotacionado.get_rect(center=(carro_x, carro_y))
    tela.blit(carro_rotacionado, carro_rect.topleft)

    # Atualizando a tela
    pygame.display.flip()

    # Definindo a velocidade do jogo
    pygame.time.Clock().tick(30)

# Encerrando o pygame
pygame.quit()
sys.exit()
