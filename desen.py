
# YAY DESENİ ÇİZİMİ

import pygame, sys, math

pygame.init()

FPS = 15  # Ekran güncelleme ayarı
fpsClock = pygame.time.Clock()

# pencereyi ayarla
screen = pygame.display.set_mode((700, 300), 0, 32)
pygame.display.set_caption('YAY DESENİ ÇİZİMİ')

BLACK = (0, 6, 255)
WHITE = (255, 0, 0)

delta_t = 0.1
m = 0.6
k = 3   # yay sabiti (-yayın kalınlığı)
c = 0.05 # -yayın daireleri arasındaki çap

x = 50   # x ekseni başlangıç noktası
y = 25    # y ekseni başlangıç noktası

vx = 10    # periyot ayarı
vy = 0

while True:
    # ekranı SİYAH ile doldur

    fx = 0
    fy = -k * (y-100) -c * vy

    vx = vx + (fx / m) * delta_t
    vy = vy + (fy / m) * delta_t

    x = x + vx * delta_t
    y = y + vy * delta_t

    if x > 300:
        screen.fill/(BLACK)
        x = 50
        
    pygame.draw.circle(screen, WHITE, (int(x), int(y)),3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FPS)



