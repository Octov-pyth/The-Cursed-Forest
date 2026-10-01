import sys
import pygame

# 1. INISIALISASI PYGAME
pygame.init()

# Konstanta Layar & Warna
LEBAR, TINGGI = 600, 400
LAYAR = pygame.display.set_mode((LEBAR, TINGGI))
pygame.display.set_caption("Pendekar Pedang 2D - The Cursed Forest")

HIJAU = (0, 255, 0)
MERAH = (255, 0, 0)
HITAM = (20, 20, 20)
PUTIH = (255, 255, 255)


# 2. IMPLEMENTASI OOP (CLASS KARAKTER)
class Pendekar:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)  # Bentuk fisik (kotak 40x40)
        self.kecepatan = 5
        self.sisa_pedang = 5

    def gerak(self, tombol):
        if tombol[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.kecepatan
        if tombol[pygame.K_RIGHT] and self.rect.x < LEBAR - self.rect.width:
            self.rect.x += self.kecepatan
        if tombol[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.kecepatan
        if tombol[pygame.K_DOWN] and self.rect.y < TINGGI - self.rect.height:
            self.rect.y += self.kecepatan

    def gambar(self, layar):
        pygame.draw.rect(layar, HIJAU, self.rect)  # Kotak hijau = Pendekar


class Monster:

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 40, 40)

    def gambar(self, layar):
        pygame.draw.rect(layar, MERAH, self.rect)  # Kotak merah = Monster


# 3. FUNCTION UNTUK UI (TEKS)
def tampilkan_teks(teks, x, y, ukuran=24):
    font = pygame.font.SysFont("Arial", ukuran)
    gambar_teks = font.render(teks, True, PUTIH)
    LAYAR.blit(gambar_teks, (x, y))


# 4. FUNCTION UTAMA (GAME LOOP)
def main():
    clock = pygame.time.Clock()
    player = Pendekar(50, 180)
    monster = Monster(450, 180)

    status_game = "BERMAIN"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if status_game == "BERMAIN":
            tombol = pygame.key.get_pressed()
            player.gerak(tombol)

            # Deteksi tabrakan 2D
            if player.rect.colliderect(monster.rect):
                if player.sisa_pedang > 0:
                    player.sisa_pedang -= 1
                    monster.rect.x = -100  # Hilangkan monster
                    status_game = "MENANG"
                else:
                    status_game = "GAMEOVER"

        # Render Visual
        LAYAR.fill(HITAM)

        if status_game == "BERMAIN":
            player.gambar(LAYAR)
            monster.gambar(LAYAR)
            tampilkan_teks(f"Sisa Pedang: {player.sisa_pedang}", 10, 10)
            tampilkan_teks("Gunakan Tombol Panah untuk Gerak!", 10, 370, 18)

        elif status_game == "MENANG":
            tampilkan_teks("MONSTER DIKALAHKAN! KAMU MENANG!", 100, 180, 28)
            tampilkan_teks(f"Sisa Pedang: {player.sisa_pedang}", 220, 220, 20)

        elif status_game == "GAMEOVER":
            tampilkan_teks("GAME OVER! PEDANGMU PATAH!", 120, 180, 28)

        pygame.display.flip()
        clock.tick(60)


main()