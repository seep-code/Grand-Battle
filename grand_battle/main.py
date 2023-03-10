import pygame
import sys
from random import randrange as rd

pygame.init()

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

CANVAS = pygame.Surface((6000, 1080))

OOB = (10000, 10000)

PATH_INDENT = -12

DESCRIPTION_FONT_SIZE = 10

LEVEL_STATUS_FONT_SIZE = 24

clock = pygame.time.Clock()
FPS = 60
G = 0.5

GLOBAL_X = -500

CHARACTER_SPEED = 5
screen_scroll = 0

TURRETS_DESTROYED = 0

level_01_background = pygame.image.load('Resources/Textures/level_01.png')
level_02_background = pygame.image.load('Resources/Textures/level_02.png')
level_03_background = pygame.image.load('Resources/Textures/level_03.png')

background_theme = pygame.mixer.Sound("Resources/Sounds/background_theme.mp3")
button_click_sound = pygame.mixer.Sound("Resources/Sounds/button_click_sound.mp3")
destruction_sound = pygame.mixer.Sound("Resources/Sounds/destruction_sound.mp3")
game_over_sound = pygame.mixer.Sound("Resources/Sounds/game_over_sound.mp3")
jump_sound = pygame.mixer.Sound("Resources/Sounds/jump_sound.mp3")
shot_sound = pygame.mixer.Sound("Resources/Sounds/shot_sound.mp3")
victory_sound = pygame.mixer.Sound("Resources/Sounds/victory_sound.mp3")

wall_image = pygame.image.load("Resources/Textures/ground_texture.png")
ladder_image = pygame.image.load('Resources/Textures/ladder.png')
turret_image = pygame.image.load('Resources/Textures/turret.png')

l_1 = pygame.image.load('Resources/Textures/1_life.png')
l_2 = pygame.image.load('Resources/Textures/2_lives.png')
l_3 = pygame.image.load('Resources/Textures/3_lives.png')
l_4 = pygame.image.load('Resources/Textures/4_lives.png')

info = open('Resources/Other/info.txt')
data = info.readlines()
info.close()

SONG_VOLUME = 0
SOUNDS_VOLUME = 0

MAP_MATRIX = []
for i in range(18):
    MAP_MATRIX.append([])
    for j in range(120):
        if i == 0 or i == 17 or j == 0 or j == 119:
            MAP_MATRIX[len(MAP_MATRIX) - 1].append('P')
        else:
            MAP_MATRIX[len(MAP_MATRIX) - 1].append('0')

for i in range(16, 26):
    if data[i][:2] == "on":
        SONG_VOLUME += 10
for i in range(27, 37):
    if data[i][:2] == "on":
        SOUNDS_VOLUME += 10

background_theme.play(-1)
background_theme.set_volume(SONG_VOLUME / 100)

CHOSEN_DIFFICULTY = 'beginner'

MAP_MATRIX = []
for i in range(18):
    MAP_MATRIX.append([])
    for j in range(120):
        if i == 0 or i == 17 or j == 0 or j == 119:
            MAP_MATRIX[len(MAP_MATRIX) - 1].append('P')
        else:
            MAP_MATRIX[len(MAP_MATRIX) - 1].append('0')
MAP_SEGMENTS = []
for k in range(12):
    MAP_SEGMENTS.append([])
    for i in range(18):
        MAP_SEGMENTS[k].append([])
        for j in range(24):
            if i == 0 or i == 17:
                MAP_SEGMENTS[k][i].append('P')
            else:
                MAP_SEGMENTS[k][i].append('0')

MAP_SEGMENTS_NUMS = [rd(0, 12), rd(0, 12), rd(0, 12)]

# ---------------SEGMENT 01 (0)---------------#

for i in range(4, 6):
    for j in range(2, 4):
        MAP_SEGMENTS[0][i][j] = 'P'
for i in range(12, 17):
    for j in range(4, 6):
        MAP_SEGMENTS[0][i][j] = 'P'
for i in range(12, 14):
    for j in range(6, 11):
        MAP_SEGMENTS[0][i][j] = 'P'
for i in range(6, 8):
    for j in range(9, 13):
        MAP_SEGMENTS[0][i][j] = 'P'
for i in range(5, 7):
    for j in range(16, 18):
        MAP_SEGMENTS[0][i][j] = 'P'
for i in range(12, 17):
    for j in range(15, 19):
        MAP_SEGMENTS[0][i][j] = 'P'
for i in range(9, 17):
    for j in range(21, 24):
        MAP_SEGMENTS[0][i][j] = 'P'

for i in range(4, 12):
    MAP_SEGMENTS[0][i][4] = 'L'
for i in range(12, 17):
    MAP_SEGMENTS[0][i][3] = 'L'
for i in range(5, 12):
    MAP_SEGMENTS[0][i][18] = 'L'
for i in range(9, 17):
    MAP_SEGMENTS[0][i][20] = 'L'

MAP_SEGMENTS[0][2][2] = 'T'
MAP_SEGMENTS[0][4][11] = 'T'
MAP_SEGMENTS[0][10][8] = 'T'
MAP_SEGMENTS[0][10][16] = 'T'
MAP_SEGMENTS[0][7][22] = 'T'

# ---------------SEGMENT 02 (1)---------------#

for i in range(4, 6):
    for j in range(2, 6):
        MAP_SEGMENTS[1][i][j] = 'P'
for i in range(11, 17):
    for j in range(1, 7):
        MAP_SEGMENTS[1][i][j] = 'P'
for i in range(4, 6):
    for j in range(8, 11):
        MAP_SEGMENTS[1][i][j] = 'P'
for i in range(10, 12):
    for j in range(9, 11):
        MAP_SEGMENTS[1][i][j] = 'P'
for i in range(7, 10):
    for j in range(15, 17):
        MAP_SEGMENTS[1][i][j] = 'P'
for i in range(14, 17):
    for j in range(14, 22):
        MAP_SEGMENTS[1][i][j] = 'P'
for i in range(6, 8):
    for j in range(19, 24):
        MAP_SEGMENTS[1][i][j] = 'P'

for i in range(11, 17):
    MAP_SEGMENTS[1][i][1] = 'L'
for i in range(4, 11):
    MAP_SEGMENTS[1][i][6] = 'L'
for i in range(11, 17):
    MAP_SEGMENTS[1][i][7] = 'L'
for i in range(14, 17):
    MAP_SEGMENTS[1][i][13] = 'L'
for i in range(7, 14):
    MAP_SEGMENTS[1][i][17] = 'L'

MAP_SEGMENTS[1][9][4] = 'T'
MAP_SEGMENTS[1][2][9] = 'T'
MAP_SEGMENTS[1][15][10] = 'T'
MAP_SEGMENTS[1][12][15] = 'T'
MAP_SEGMENTS[1][12][19] = 'T'

# ---------------SEGMENT 03 (2)---------------#

for i in range(15, 17):
    for j in range(2, 5):
        MAP_SEGMENTS[2][i][j] = 'P'
for i in range(9, 11):
    for j in range(2, 5):
        MAP_SEGMENTS[2][i][j] = 'P'
for i in range(13, 17):
    for j in range(8, 11):
        MAP_SEGMENTS[2][i][j] = 'P'
for i in range(7, 9):
    for j in range(8, 11):
        MAP_SEGMENTS[2][i][j] = 'P'
for i in range(11, 17):
    for j in range(14, 17):
        MAP_SEGMENTS[2][i][j] = 'P'
for i in range(5, 7):
    for j in range(14, 17):
        MAP_SEGMENTS[2][i][j] = 'P'
for i in range(9, 17):
    for j in range(20, 23):
        MAP_SEGMENTS[2][i][j] = 'P'

for i in range(7, 17):
    MAP_SEGMENTS[2][i][7] = 'L'
for i in range(5, 17):
    MAP_SEGMENTS[2][i][13] = 'L'
for i in range(9, 17):
    MAP_SEGMENTS[2][i][19] = 'L'

MAP_SEGMENTS[2][7][3] = 'T'
MAP_SEGMENTS[2][5][9] = 'T'
MAP_SEGMENTS[2][11][9] = 'T'
MAP_SEGMENTS[2][9][15] = 'T'
MAP_SEGMENTS[2][7][21] = 'T'

# ---------------SEGMENT 04 (3)---------------#

for i in range(11, 13):
    for j in range(2, 5):
        MAP_SEGMENTS[3][i][j] = 'P'
for i in range(13, 17):
    for j in range(5, 7):
        MAP_SEGMENTS[3][i][j] = 'P'
for i in range(12, 14):
    for j in range(9, 13):
        MAP_SEGMENTS[3][i][j] = 'P'
for i in range(6, 8):
    for j in range(9, 19):
        MAP_SEGMENTS[3][i][j] = 'P'
for i in range(15, 17):
    for j in range(13, 15):
        MAP_SEGMENTS[3][i][j] = 'P'
for i in range(13, 17):
    for j in range(15, 17):
        MAP_SEGMENTS[3][i][j] = 'P'
for i in range(6, 8):
    for j in range(21, 23):
        MAP_SEGMENTS[3][i][j] = 'P'
for i in range(11, 17):
    for j in range(20, 23):
        MAP_SEGMENTS[3][i][j] = 'P'

for i in range(11, 17):
    MAP_SEGMENTS[3][i][1] = 'L'
for i in range(6, 17):
    MAP_SEGMENTS[3][i][8] = 'L'
for i in range(6, 17):
    MAP_SEGMENTS[3][i][19] = 'L'

MAP_SEGMENTS[3][9][3] = 'T'
MAP_SEGMENTS[3][10][10] = 'T'
MAP_SEGMENTS[3][15][11] = 'T'
MAP_SEGMENTS[3][4][16] = 'T'
MAP_SEGMENTS[3][9][21] = 'T'

# ---------------SEGMENT 05 (4)---------------#

for i in range(4, 6):
    for j in range(2, 3):
        MAP_SEGMENTS[4][i][j] = 'P'
for i in range(6, 11):
    for j in range(5, 7):
        MAP_SEGMENTS[4][i][j] = 'P'
for i in range(6, 8):
    for j in range(7, 11):
        MAP_SEGMENTS[4][i][j] = 'P'
for i in range(15, 17):
    for j in range(7, 11):
        MAP_SEGMENTS[4][i][j] = 'P'
for i in range(12, 17):
    for j in range(11, 14):
        MAP_SEGMENTS[4][i][j] = 'P'
for i in range(8, 17):
    for j in range(17, 21):
        MAP_SEGMENTS[4][i][j] = 'P'
for i in range(5, 7):
    for j in range(22, 24):
        MAP_SEGMENTS[4][i][j] = 'P'

for i in range(6, 17):
    MAP_SEGMENTS[4][i][4] = 'L'
for i in range(8, 17):
    MAP_SEGMENTS[4][i][16] = 'L'
for i in range(5, 17):
    MAP_SEGMENTS[4][i][21] = 'L'

MAP_SEGMENTS[4][2][1] = 'T'
MAP_SEGMENTS[4][4][7] = 'T'
MAP_SEGMENTS[4][13][9] = 'T'
MAP_SEGMENTS[4][10][12] = 'T'
MAP_SEGMENTS[4][6][19] = 'T'

# ---------------SEGMENT 06 (5)---------------#

for i in range(5, 7):
    for j in range(2, 4):
        MAP_SEGMENTS[5][i][j] = 'P'
for i in range(12, 14):
    for j in range(2, 4):
        MAP_SEGMENTS[5][i][j] = 'P'
for i in range(6, 8):
    for j in range(9, 24):
        MAP_SEGMENTS[5][i][j] = 'P'
for i in range(12, 14):
    for j in range(8, 24):
        MAP_SEGMENTS[5][i][j] = 'P'

for i in range(5, 17):
    MAP_SEGMENTS[5][i][4] = 'L'
for i in range(6, 12):
    MAP_SEGMENTS[5][i][8] = 'L'
for i in range(12, 17):
    MAP_SEGMENTS[5][i][7] = 'L'

MAP_SEGMENTS[5][15][1] = 'T'
MAP_SEGMENTS[5][3][2] = 'T'
MAP_SEGMENTS[5][4][13] = 'T'
MAP_SEGMENTS[5][15][17] = 'T'
MAP_SEGMENTS[5][10][22] = 'T'

# ---------------SEGMENT 07 (6)---------------#

for i in range(4, 6):
    for j in range(2, 3):
        MAP_SEGMENTS[6][i][j] = 'P'
for i in range(7, 9):
    for j in range(4, 6):
        MAP_SEGMENTS[6][i][j] = 'P'
for i in range(9, 11):
    for j in range(4, 10):
        MAP_SEGMENTS[6][i][j] = 'P'
for i in range(15, 17):
    for j in range(10, 12):
        MAP_SEGMENTS[6][i][j] = 'P'
for i in range(12, 15):
    for j in range(14, 17):
        MAP_SEGMENTS[6][i][j] = 'P'
for i in range(8, 10):
    for j in range(17, 20):
        MAP_SEGMENTS[6][i][j] = 'P'
for i in range(12, 17):
    for j in range(21, 24):
        MAP_SEGMENTS[6][i][j] = 'P'

for i in range(4, 17):
    MAP_SEGMENTS[6][i][3] = 'L'
for i in range(12, 17):
    MAP_SEGMENTS[6][i][13] = 'L'
for i in range(8, 17):
    MAP_SEGMENTS[6][i][20] = 'L'

MAP_SEGMENTS[6][2][1] = 'T'
MAP_SEGMENTS[6][15][7] = 'T'
MAP_SEGMENTS[6][10][15] = 'T'
MAP_SEGMENTS[6][6][18] = 'T'
MAP_SEGMENTS[6][10][22] = 'T'

# ---------------SEGMENT 08 (7)---------------#

for i in range(8, 10):
    for j in range(2, 5):
        MAP_SEGMENTS[7][i][j] = 'P'
for i in range(15, 17):
    for j in range(2, 5):
        MAP_SEGMENTS[7][i][j] = 'P'
for i in range(8, 10):
    for j in range(8, 11):
        MAP_SEGMENTS[7][i][j] = 'P'
for i in range(15, 17):
    for j in range(9, 12):
        MAP_SEGMENTS[7][i][j] = 'P'
for i in range(13, 17):
    for j in range(12, 14):
        MAP_SEGMENTS[7][i][j] = 'P'
for i in range(4, 8):
    for j in range(14, 16):
        MAP_SEGMENTS[7][i][j] = 'P'
for i in range(4, 6):
    for j in range(16, 18):
        MAP_SEGMENTS[7][i][j] = 'P'
for i in range(10, 17):
    for j in range(19, 24):
        MAP_SEGMENTS[7][i][j] = 'P'

for i in range(8, 17):
    MAP_SEGMENTS[7][i][7] = 'L'
for i in range(13, 17):
    MAP_SEGMENTS[7][i][14] = 'L'
for i in range(4, 17):
    MAP_SEGMENTS[7][i][18] = 'L'

MAP_SEGMENTS[7][6][2] = 'T'
MAP_SEGMENTS[7][6][9] = 'T'
MAP_SEGMENTS[7][13][10] = 'T'
MAP_SEGMENTS[7][2][16] = 'T'
MAP_SEGMENTS[7][8][21] = 'T'

# ---------------SEGMENT 09 (8)---------------#

for i in range(7, 9):
    for j in range(2, 6):
        MAP_SEGMENTS[8][i][j] = 'P'
for i in range(14, 17):
    for j in range(2, 4):
        MAP_SEGMENTS[8][i][j] = 'P'
for i in range(12, 14):
    for j in range(6, 8):
        MAP_SEGMENTS[8][i][j] = 'P'
for i in range(4, 6):
    for j in range(9, 11):
        MAP_SEGMENTS[8][i][j] = 'P'
for i in range(4, 6):
    for j in range(14, 18):
        MAP_SEGMENTS[8][i][j] = 'P'
for i in range(9, 11):
    for j in range(11, 17):
        MAP_SEGMENTS[8][i][j] = 'P'
for i in range(9, 11):
    for j in range(18, 22):
        MAP_SEGMENTS[8][i][j] = 'P'
for i in range(14, 17):
    for j in range(11, 14):
        MAP_SEGMENTS[8][i][j] = 'P'

for i in range(14, 17):
    MAP_SEGMENTS[8][i][1] = 'L'
for i in range(14, 17):
    MAP_SEGMENTS[8][i][4] = 'L'
for i in range(9, 17):
    MAP_SEGMENTS[8][i][10] = 'L'
for i in range(4, 17):
    MAP_SEGMENTS[8][i][18] = 'L'

MAP_SEGMENTS[8][7][12] = 'T'
MAP_SEGMENTS[8][12][12] = 'T'
MAP_SEGMENTS[8][2][15] = 'T'
MAP_SEGMENTS[8][7][20] = 'T'
MAP_SEGMENTS[8][15][20] = 'T'

# ---------------SEGMENT 10 (9)---------------#

for i in range(10, 12):
    for j in range(2, 3):
        MAP_SEGMENTS[9][i][j] = 'P'
for i in range(5, 7):
    for j in range(4, 9):
        MAP_SEGMENTS[9][i][j] = 'P'
for i in range(13, 15):
    for j in range(7, 11):
        MAP_SEGMENTS[9][i][j] = 'P'
for i in range(6, 8):
    for j in range(12, 16):
        MAP_SEGMENTS[9][i][j] = 'P'
for i in range(11, 13):
    for j in range(15, 20):
        MAP_SEGMENTS[9][i][j] = 'P'
for i in range(13, 17):
    for j in range(15, 17):
        MAP_SEGMENTS[9][i][j] = 'P'
for i in range(14, 17):
    for j in range(22, 24):
        MAP_SEGMENTS[9][i][j] = 'P'

for i in range(5, 17):
    MAP_SEGMENTS[9][i][3] = 'L'
for i in range(13, 17):
    MAP_SEGMENTS[9][i][11] = 'L'
for i in range(11, 17):
    MAP_SEGMENTS[9][i][14] = 'L'
for i in range(6, 11):
    MAP_SEGMENTS[9][i][16] = 'L'
for i in range(14, 17):
    MAP_SEGMENTS[9][i][21] = 'L'

MAP_SEGMENTS[9][3][6] = 'T'
MAP_SEGMENTS[9][11][8] = 'T'
MAP_SEGMENTS[9][15][9] = 'T'
MAP_SEGMENTS[9][4][14] = 'T'
MAP_SEGMENTS[9][9][18] = 'T'

# ---------------SEGMENT 11 (10)---------------#

for i in range(6, 8):
    for j in range(2, 8):
        MAP_SEGMENTS[10][i][j] = 'P'
for i in range(13, 17):
    for j in range(4, 7):
        MAP_SEGMENTS[10][i][j] = 'P'
for i in range(11, 13):
    for j in range(8, 11):
        MAP_SEGMENTS[10][i][j] = 'P'
for i in range(9, 11):
    for j in range(12, 15):
        MAP_SEGMENTS[10][i][j] = 'P'
for i in range(14, 17):
    for j in range(13, 15):
        MAP_SEGMENTS[10][i][j] = 'P'
for i in range(13, 17):
    for j in range(17, 20):
        MAP_SEGMENTS[10][i][j] = 'P'
for i in range(9, 11):
    for j in range(21, 24):
        MAP_SEGMENTS[10][i][j] = 'P'

for i in range(13, 17):
    MAP_SEGMENTS[10][i][3] = 'L'
for i in range(11, 17):
    MAP_SEGMENTS[10][i][7] = 'L'
for i in range(6, 11):
    MAP_SEGMENTS[10][i][8] = 'L'
for i in range(9, 17):
    MAP_SEGMENTS[10][i][15] = 'L'
for i in range(9, 17):
    MAP_SEGMENTS[10][i][20] = 'L'

MAP_SEGMENTS[10][4][5] = 'T'
MAP_SEGMENTS[10][15][9] = 'T'
MAP_SEGMENTS[10][7][13] = 'T'
MAP_SEGMENTS[10][11][18] = 'T'
MAP_SEGMENTS[10][7][22] = 'T'

# ---------------SEGMENT 12 (11)---------------#

for i in range(12, 14):
    for j in range(2, 3):
        MAP_SEGMENTS[11][i][j] = 'P'
for i in range(14, 16):
    for j in range(5, 11):
        MAP_SEGMENTS[11][i][j] = 'P'
for i in range(4, 6):
    for j in range(7, 12):
        MAP_SEGMENTS[11][i][j] = 'P'
for i in range(9, 11):
    for j in range(6, 15):
        MAP_SEGMENTS[11][i][j] = 'P'
for i in range(4, 6):
    for j in range(17, 21):
        MAP_SEGMENTS[11][i][j] = 'P'
for i in range(13, 15):
    for j in range(18, 21):
        MAP_SEGMENTS[11][i][j] = 'P'
for i in range(15, 17):
    for j in range(18, 20):
        MAP_SEGMENTS[11][i][j] = 'P'
for i in range(9, 11):
    for j in range(22, 24):
        MAP_SEGMENTS[11][i][j] = 'P'

for i in range(14, 17):
    MAP_SEGMENTS[11][i][4] = 'L'
for i in range(9, 14):
    MAP_SEGMENTS[11][i][5] = 'L'
for i in range(4, 9):
    MAP_SEGMENTS[11][i][6] = 'L'
for i in range(13, 17):
    MAP_SEGMENTS[11][i][17] = 'L'
for i in range(4, 17):
    MAP_SEGMENTS[11][i][21] = 'L'

MAP_SEGMENTS[11][7][8] = 'T'
MAP_SEGMENTS[11][12][8] = 'T'
MAP_SEGMENTS[11][2][9] = 'T'
MAP_SEGMENTS[11][2][19] = 'T'
MAP_SEGMENTS[11][11][19] = 'T'


# --------------------------------------------#

class Button:
    def __init__(self, image, image_path, pos, difficulty_button=0, level_button=0, endless_button=0):
        self.image = image
        self.image_path = image_path
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.difficulty_button = difficulty_button
        self.level_button = level_button
        self.endless_button = endless_button

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            return True
        return False

    def changeCondition(self, position):
        global data
        global CHOSEN_DIFFICULTY
        c_d = 0
        if CHOSEN_DIFFICULTY == 'medium':
            c_d = 1
        if CHOSEN_DIFFICULTY == 'hard':
            c_d = 2
        if CHOSEN_DIFFICULTY == 'insane':
            c_d = 3
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.image_path = self.image_path[:PATH_INDENT] + "_enabled.png"
            self.image = pygame.image.load(self.image_path)
        else:
            self.image_path = self.image_path[:PATH_INDENT] + "disabled.png"
            self.image = pygame.image.load(self.image_path)
        if self.endless_button:
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom):
                personal_best_text = get_font(LEVEL_STATUS_FONT_SIZE).render("Personal best: " + data[87] + " metres",
                                                                             True, "#b68f40")
                personal_best_rect = personal_best_text.get_rect(center=(1000, 800))
                SCREEN.blit(personal_best_text, personal_best_rect)

        if self.level_button:
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom):
                l_b = self.level_button - 1
                status = data[c_d * 4 + l_b][0] + " stars"
                time = data[38 + c_d * 12 + l_b * 4][:2] + " hr " + data[39 + c_d * 12 + l_b * 4][:2] + " min " + \
                       data[40 + c_d * 12 + l_b * 4][:2] + " sec"
                if data[c_d * 4 + l_b][0] == '0':
                    status = "not completed"
                if data[38 + c_d * 12 + l_b * 4][:2] == "00" and data[39 + c_d * 12 + l_b * 4][:2] == "00" and \
                        data[40 + c_d * 12 + l_b * 4][:2] == "00":
                    time = "-"
                level_status_text = get_font(LEVEL_STATUS_FONT_SIZE).render("Status: " + status, True, "#b68f40")
                level_status_rect = level_status_text.get_rect(center=(1000, 800))
                level_time_text = get_font(LEVEL_STATUS_FONT_SIZE).render("Time: " + time, True, "#b68f40")
                level_time_rect = level_time_text.get_rect(center=(1000, 830))
                SCREEN.blit(level_status_text, level_status_rect)
                SCREEN.blit(level_time_text, level_time_rect)
        if self.difficulty_button:
            if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                              self.rect.bottom):
                level01_icon_path = "Resources/Textures/Level buttons/level01_button_stars-" + \
                                    data[(self.difficulty_button - 1) * 4][0] + "_disabled.png"
                level02_icon_path = "Resources/Textures/Level buttons/level02_button_stars-" + \
                                    data[(self.difficulty_button - 1) * 4 + 1][0] + "_disabled.png"
                level03_icon_path = "Resources/Textures/Level buttons/level03_button_stars-" + \
                                    data[(self.difficulty_button - 1) * 4 + 2][0] + "_disabled.png"
                level01_icon = pygame.image.load(level01_icon_path)
                level02_icon = pygame.image.load(level02_icon_path)
                level03_icon = pygame.image.load(level03_icon_path)
                SCREEN.blit(level01_icon, (250, 150))
                SCREEN.blit(level02_icon, (600, 150))
                SCREEN.blit(level03_icon, (950, 150))
                difficulty_description = pygame.image.load("Resources/Textures/difficulty_description_label.png")
                SCREEN.blit(difficulty_description, (400, 500))
                if self.difficulty_button == 1:
                    description_text_part01 = get_font(DESCRIPTION_FONT_SIZE).render(
                        "Beginner difficulty (I'm Too Young to Die):", True, "#605b00")
                    description_rect_part01 = description_text_part01.get_rect(center=(672, 518))
                    SCREEN.blit(description_text_part01, description_rect_part01)
                    description_text_part03 = get_font(DESCRIPTION_FONT_SIZE).render(
                        "   - 3 additional lifes in every attempt", True, "#605b00")
                    description_rect_part03 = description_text_part03.get_rect(center=(710, 585))
                    SCREEN.blit(description_text_part03, description_rect_part03)
                    description_text_part04 = get_font(DESCRIPTION_FONT_SIZE).render("   - Slow turrets and bullets",
                                                                                     True, "#605b00")
                    description_rect_part04 = description_text_part04.get_rect(center=(655, 620))
                    SCREEN.blit(description_text_part04, description_rect_part04)
                    beginner_difficulty = pygame.image.load("Resources/Textures/beginner_difficulty_icon.png")
                    SCREEN.blit(beginner_difficulty, (420, 550))
                if self.difficulty_button == 2:
                    description_text_part01 = get_font(DESCRIPTION_FONT_SIZE).render(
                        "Medium difficulty (Hurt Me Plenty):", True, "#605b00")
                    description_rect_part01 = description_text_part01.get_rect(center=(672, 518))
                    SCREEN.blit(description_text_part01, description_rect_part01)
                    description_text_part03 = get_font(DESCRIPTION_FONT_SIZE).render(
                        "   - 2 additional lifes in every attempt", True, "#605b00")
                    description_rect_part03 = description_text_part03.get_rect(center=(710, 585))
                    SCREEN.blit(description_text_part03, description_rect_part03)
                    description_text_part04 = get_font(DESCRIPTION_FONT_SIZE).render("   - Normal reaction of", True,
                                                                                     "#605b00")
                    description_rect_part04 = description_text_part04.get_rect(center=(625, 620))
                    SCREEN.blit(description_text_part04, description_rect_part04)
                    description_text_part05 = get_font(DESCRIPTION_FONT_SIZE).render("turrets and bullets speed", True,
                                                                                     "#605b00")
                    description_rect_part05 = description_text_part05.get_rect(center=(665, 655))
                    SCREEN.blit(description_text_part05, description_rect_part05)
                    medium_difficulty = pygame.image.load("Resources/Textures/medium_difficulty_icon.png")
                    SCREEN.blit(medium_difficulty, (420, 550))
                if self.difficulty_button == 3:
                    description_text_part01 = get_font(DESCRIPTION_FONT_SIZE).render(
                        "Hard difficulty (Ultra Violence):", True, "#605b00")
                    description_rect_part01 = description_text_part01.get_rect(center=(672, 518))
                    SCREEN.blit(description_text_part01, description_rect_part01)
                    description_text_part03 = get_font(DESCRIPTION_FONT_SIZE).render(
                        "   - 1 additional lifes in every attempt", True, "#605b00")
                    description_rect_part03 = description_text_part03.get_rect(center=(710, 585))
                    SCREEN.blit(description_text_part03, description_rect_part03)
                    description_text_part04 = get_font(DESCRIPTION_FONT_SIZE).render("   - Very fast reaction of", True,
                                                                                     "#605b00")
                    description_rect_part04 = description_text_part04.get_rect(center=(640, 620))
                    SCREEN.blit(description_text_part04, description_rect_part04)
                    description_text_part05 = get_font(DESCRIPTION_FONT_SIZE).render("turrets and bullets speed", True,
                                                                                     "#605b00")
                    description_rect_part05 = description_text_part05.get_rect(center=(665, 655))
                    SCREEN.blit(description_text_part05, description_rect_part05)
                    hard_difficulty = pygame.image.load("Resources/Textures/hard_difficulty_icon.png")
                    SCREEN.blit(hard_difficulty, (420, 550))
                if self.difficulty_button == 4:
                    description_text_part01 = get_font(DESCRIPTION_FONT_SIZE).render("Insane difficulty (Nightmare):",
                                                                                     True, "#605b00")
                    description_rect_part01 = description_text_part01.get_rect(center=(672, 518))
                    SCREEN.blit(description_text_part01, description_rect_part01)
                    description_text_part03 = get_font(DESCRIPTION_FONT_SIZE).render("   - Additional lifes is absent",
                                                                                     True, "#605b00")
                    description_rect_part03 = description_text_part03.get_rect(center=(665, 580))
                    SCREEN.blit(description_text_part03, description_rect_part03)
                    description_text_part04 = get_font(DESCRIPTION_FONT_SIZE).render("   - Perfect reaction of", True,
                                                                                     "#605b00")
                    description_rect_part04 = description_text_part04.get_rect(center=(630, 610))
                    SCREEN.blit(description_text_part04, description_rect_part04)
                    description_text_part05 = get_font(DESCRIPTION_FONT_SIZE).render("turrets and bullets speed", True,
                                                                                     "#605b00")
                    description_rect_part05 = description_text_part05.get_rect(center=(665, 640))
                    SCREEN.blit(description_text_part05, description_rect_part05)
                    description_text_part06 = get_font(DESCRIPTION_FONT_SIZE).render("   - No hope...", True, "#605b00")
                    description_rect_part06 = description_text_part06.get_rect(center=(585, 670))
                    SCREEN.blit(description_text_part06, description_rect_part06)
                    insane_difficulty = pygame.image.load("Resources/Textures/insane_difficulty_icon.png")
                    SCREEN.blit(insane_difficulty, (420, 550))
            else:
                self.image_path = self.image_path[:PATH_INDENT] + "disabled.png"
                self.image = pygame.image.load(self.image_path)


class Character(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity, lives):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Resources/Textures/character.png')
        self.flying_gun = pygame.image.load('Resources/Textures/flying_gun.png')
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.lives = lives
        self.velocity = velocity
        self.velocity_y = 0
        self.jump = False
        self.air = True
        self.climbing = False
        self.ladder = False
        self.change_direction = False
        self.look_direction = 1
        self.cooldown = 0
        self.check_alive = True

        self.size = self.image.get_size()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self):
        SCREEN.blit(pygame.transform.flip(self.image, self.change_direction, False), self.rect)
        if self.look_direction == 1:
            SCREEN.blit(pygame.transform.flip(self.flying_gun, self.change_direction, False),
                        (self.rect.x + self.width * self.look_direction, self.rect.y))
        else:
            SCREEN.blit(pygame.transform.flip(self.flying_gun, self.change_direction, False),
                        (self.rect.x - self.flying_gun.get_width(), self.rect.y))

    def get_x(self):
        return self.rect.x

    def move(self, move_left, move_right):
        global screen_scroll, G, GLOBAL_X
        x_change = 0
        y_change = 0
        hit = False
        if move_left:
            x_change = -self.velocity
            self.change_direction = True
            self.look_direction = -1

        if move_right:
            x_change = self.velocity
            self.change_direction = False
            self.look_direction = 1

        if self.jump and self.air is False:
            self.velocity_y = -10
            self.jump = False
            self.air = True

        if not self.ladder:
            self.velocity_y += G
        if self.velocity_y > 12:
            self.velocity_y = 12

        y_change += self.velocity_y
        GLOBAL_X += x_change

        for x in range(len(MAP_MATRIX)):
            for y in range(len(MAP_MATRIX[x])):
                block = MAP_MATRIX[x][y]
                tile = pygame.Rect((240 + y * 50 + screen_scroll, x * 50), (50, 50))

                if block == 'P':
                    if tile.colliderect(self.rect.x + x_change, self.rect.y, self.width,
                                        self.height):
                        x_change = 0
                        hit = True

                    if tile.colliderect(self.rect.x, self.rect.y + y_change, self.width,
                                        self.height):
                        if self.velocity_y < 0:
                            self.velocity_y = 0
                            y_change = 0

                        elif self.velocity_y > 0:
                            self.velocity_y = 0
                            self.air = False
                            y_change = 0

                if block == 'L':
                    if tile.colliderect(self.rect.x, self.rect.y, self.width,
                                        self.height) and self.climbing:
                        if 240 + y * 50 + screen_scroll < self.rect.centerx < 240 + y * 50 + 50 + screen_scroll:
                            self.ladder = True
                            self.air = True
                            self.velocity_y = 0
                            y_change += -2

        if y_change > 0 and self.rect.bottom % 50 != 0:
            self.air = True

        if self.rect.left + x_change < 640 or self.rect.right + x_change > SCREEN_WIDTH - 640:
            screen_scroll -= x_change
            x_change = 0

        self.rect.y += y_change
        self.rect.x += x_change

        if self.cooldown > 0:
            self.cooldown -= 1

        if self.lives == 4:
            SCREEN.blit(l_4, (1435, -4))
        if self.lives == 3:
            SCREEN.blit(l_3, (1435, -4))
        if self.lives == 2:
            SCREEN.blit(l_2, (1435, -4))
        if self.lives == 1:
            SCREEN.blit(l_1, (1435, -4))

        if self.lives == 0:
            self.check_alive = False

        return [x_change, move_left, move_right, hit]

    def shoot(self):
        if self.look_direction == 1:
            return Bullet(self.rect.x + self.size[0] + self.flying_gun.get_width(),
                          self.rect.y + self.size[1] // 3 - 7,
                          5, self.look_direction)
        return Bullet(self.rect.x - self.flying_gun.get_width(), self.rect.y + self.size[1] // 3 - 7, 5,
                      self.look_direction)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Resources/Textures/player_bullet.png")
        self.speed = speed
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.direction = direction

    def update(self, change, enemy_group, char):
        if change[0] == 0 and change[1] and not change[3]:
            if self.direction == 1:
                self.rect.x += self.speed + CHARACTER_SPEED
            else:
                self.rect.x -= self.speed - CHARACTER_SPEED
        else:
            if self.direction == 1:
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed

        if change[0] == 0 and change[2] and not change[3]:
            if self.direction == 1:
                self.rect.x += self.speed - CHARACTER_SPEED
            else:
                self.rect.x -= self.speed + CHARACTER_SPEED
        else:
            if self.direction == 1:
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed

        for x in range(len(MAP_MATRIX)):
            for y in range(len(MAP_MATRIX[x])):
                block = MAP_MATRIX[x][y]
                tile = pygame.Rect((240 + y * 50 + screen_scroll, x * 50), (50, 50))

                if block == 'P':
                    if tile.colliderect(self.rect.x + self.speed, self.rect.y, self.rect.width,
                                        self.rect.height):
                        self.kill()

        if abs(char.rect.x - self.rect.x) > 1600:
            self.kill()

        for enemy in enemy_group:
            if self.rect.colliderect(enemy):
                self.kill()
                enemy.health -= 1


bullet_group = pygame.sprite.Group()


class Turret(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, health, bullet_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Resources/Textures/turret.png')
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.size = self.image.get_size()
        self.health = health
        self.look_direction = -1
        self.change_direction = False
        self.cooldown = 60
        self.bullet_speed = bullet_speed

    def shoot(self):
        if self.look_direction == 1:
            return EnemyBullet(self.rect.x + self.size[0], self.rect.y + self.size[1] // 3 + 9,
                               self.bullet_speed, self.look_direction)
        return EnemyBullet(self.rect.x, self.rect.y + self.size[1] // 3 + 9, self.bullet_speed,
                           self.look_direction)

    def update(self, change, char):
        if change[0] == 0 and change[1] and not change[3]:
            self.rect.x += CHARACTER_SPEED
        if change[0] == 0 and change[2] and not change[3]:
            self.rect.x -= CHARACTER_SPEED

        if (char.rect.right + 20 < self.rect.left) and abs(self.rect.bottom - char.rect.bottom) < 50:
            self.look_direction = -1
            self.change_direction = False
        if (char.rect.left - 20 > self.rect.right) and abs(self.rect.bottom - char.rect.bottom) < 50:
            self.look_direction = 1
            self.change_direction = True

        SCREEN.blit(pygame.transform.flip(self.image, self.change_direction, False), self.rect)

        if self.health == 0:
            self.kill()
            destruction_sound.play()
            destruction_sound.set_volume(SOUNDS_VOLUME / 100)
            global TURRETS_DESTROYED
            TURRETS_DESTROYED += 1

        if 0 < self.rect.left - char.rect.right < 700 and abs(self.rect.bottom - char.rect.bottom) < 50:
            if self.cooldown > 0:
                self.cooldown -= 1
            if self.cooldown == 0:
                self.cooldown = 60
                enemy_bullet_group.add(self.shoot())
        if 0 < char.rect.left - self.rect.right < 700 and abs(self.rect.bottom - char.rect.bottom) < 50:
            if self.cooldown > 0:
                self.cooldown -= 1
            if self.cooldown == 0:
                self.cooldown = 60
                enemy_bullet_group.add(self.shoot())


turret_group = pygame.sprite.Group()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed, direction):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Resources/Textures/enemy_bullet.png")
        self.speed = speed
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)
        self.direction = direction

    def update(self, change, char):
        if change[0] == 0 and change[1] and not change[3]:
            if self.direction == 1:
                self.rect.x += self.speed + CHARACTER_SPEED
            else:
                self.rect.x -= self.speed - CHARACTER_SPEED
        else:
            if self.direction == 1:
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed
        if change[0] == 0 and change[2] and not change[3]:
            if self.direction == 1:
                self.rect.x += self.speed - CHARACTER_SPEED
            else:
                self.rect.x -= self.speed + CHARACTER_SPEED
        else:
            if self.direction == 1:
                self.rect.x += self.speed
            else:
                self.rect.x -= self.speed

        for x in range(len(MAP_MATRIX)):
            for y in range(len(MAP_MATRIX[x])):
                block = MAP_MATRIX[x][y]
                tile = pygame.Rect((240 + y * 50 + screen_scroll, x * 50), (50, 50))

                if block == 'P':
                    if tile.colliderect(self.rect.x + self.speed, self.rect.y, self.rect.width,
                                        self.rect.height):
                        self.kill()

        if abs(char.rect.x - self.rect.x) > 1600:
            self.kill()

        if self.rect.colliderect(char.rect):
            char.lives -= 1
            self.kill()


enemy_bullet_group = pygame.sprite.Group()


class Portal(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, difficulty):
        pygame.sprite.Sprite.__init__(self)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.difficulty = difficulty
        self.image = pygame.image.load(f'Resources/Textures/portal_{difficulty}.png')
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def check_completion(self, character):
        if self.rect.colliderect(character.rect.x - character.width // 2, character.rect.y, character.width,
                                 character.height):
            return True

    def draw(self):
        SCREEN.blit(self.image, self.rect)

    def update(self, change):
        if change[0] == 0 and change[1] and not change[3]:
            self.rect.x += CHARACTER_SPEED
        if change[0] == 0 and change[2] and not change[3]:
            self.rect.x -= CHARACTER_SPEED


def endless_map_update():
    global MAP_MATRIX
    global MAP_SEGMENTS
    global MAP_SEGMENTS_NUMS
    for k in range(len(MAP_SEGMENTS_NUMS) - 3, len(MAP_SEGMENTS_NUMS)):
        new_segment = MAP_SEGMENTS_NUMS[k]
        for i in range(18):
            for j in range(24):
                MAP_MATRIX[i].append(MAP_SEGMENTS[new_segment][i][j])


def get_font(size):
    return pygame.font.Font("Resources/Textures/font.ttf", size)


def difficulty_list(return_to_main_menu_P):
    global SOUNDS_VOLUME
    global SONG_VOLUME
    while True:
        diffculty_list_mouse_pos = pygame.mouse.get_pos()

        return_to_main_menu_P.changeCondition(diffculty_list_mouse_pos)
        return_to_main_menu_P.update(SCREEN)

        beginner_difficulty = Button(
            image=pygame.image.load("Resources/Textures/Difficulty buttons/beginner_difficulty_button_disabled.png"),
            image_path="Resources/Textures/Difficulty buttons/beginner_difficulty_button_disabled.png", pos=(1500, 300),
            difficulty_button=1)

        beginner_difficulty.changeCondition(diffculty_list_mouse_pos)
        beginner_difficulty.update(SCREEN)

        medium_difficulty = Button(
            image=pygame.image.load("Resources/Textures/Difficulty buttons/medium_difficulty_button_disabled.png"),
            image_path="Resources/Textures/Difficulty buttons/medium_difficulty_button_disabled.png", pos=(1500, 400),
            difficulty_button=2)

        medium_difficulty.changeCondition(diffculty_list_mouse_pos)
        medium_difficulty.update(SCREEN)

        hard_difficulty = Button(
            image=pygame.image.load("Resources/Textures/Difficulty buttons/hard_difficulty_button_disabled.png"),
            image_path="Resources/Textures/Difficulty buttons/hard_difficulty_button_disabled.png", pos=(1500, 500),
            difficulty_button=3)

        hard_difficulty.changeCondition(diffculty_list_mouse_pos)
        hard_difficulty.update(SCREEN)

        insane_difficulty = Button(
            image=pygame.image.load("Resources/Textures/Difficulty buttons/insane_difficulty_button_disabled.png"),
            image_path="Resources/Textures/Difficulty buttons/insane_difficulty_button_disabled.png", pos=(1500, 600),
            difficulty_button=4)

        insane_difficulty.changeCondition(diffculty_list_mouse_pos)
        insane_difficulty.update(SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_main_menu_P.checkForInput(diffculty_list_mouse_pos):
                    button_click_sound.play()
                    main_menu()
                if beginner_difficulty.checkForInput(diffculty_list_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    return 'beginner'
                if medium_difficulty.checkForInput(diffculty_list_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    return 'medium'
                if hard_difficulty.checkForInput(diffculty_list_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    return 'hard'
                if insane_difficulty.checkForInput(diffculty_list_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    return 'insane'
        pygame.display.update()


def play():
    global CHOSEN_DIFFICULTY
    global SOUNDS_VOLUME
    global SONG_VOLUME

    while True:
        chosen_diff = 0
        if CHOSEN_DIFFICULTY == 'beginner':
            chosen_diff = 0
        if CHOSEN_DIFFICULTY == 'medium':
            chosen_diff = 1
        if CHOSEN_DIFFICULTY == 'hard':
            chosen_diff = 2
        if CHOSEN_DIFFICULTY == 'insane':
            chosen_diff = 3

        play_mouse_pos = pygame.mouse.get_pos()

        SCREEN.fill("#121212")
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))
        choose_difficulty = Button(
            image=pygame.image.load("Resources/Textures/Difficulty buttons/difficulty_button_disabled.png"),
            image_path="Resources/Textures/Difficulty buttons/difficulty_button_disabled.png", pos=(1500, 200))

        choose_difficulty.changeCondition(play_mouse_pos)
        choose_difficulty.update(SCREEN)

        level01_button_path = "Resources/Textures/Level buttons/level01_button_stars-" + data[chosen_diff * 4][
            0] + "_disabled.png"
        level01_button = Button(image=pygame.image.load(level01_button_path), image_path=level01_button_path,
                                pos=(400, 300), level_button=1)

        level01_button.changeCondition(play_mouse_pos)
        level01_button.update(SCREEN)

        level02_button_path = "Resources/Textures/Level buttons/level02_button_stars-" + data[chosen_diff * 4 + 1][
            0] + "_disabled.png"
        level02_button = Button(image=pygame.image.load(level02_button_path), image_path=level02_button_path,
                                pos=(750, 300), level_button=2)

        level02_button.changeCondition(play_mouse_pos)
        level02_button.update(SCREEN)

        level03_button_path = "Resources/Textures/Level buttons/level03_button_stars-" + data[chosen_diff * 4 + 2][
            0] + "_disabled.png"
        level03_button = Button(image=pygame.image.load(level03_button_path), image_path=level03_button_path,
                                pos=(1100, 300), level_button=3)

        level03_button.changeCondition(play_mouse_pos)
        level03_button.update(SCREEN)

        endless_button_path = "Resources/Textures/endless_mode_button_disabled.png"
        endless_button = Button(image=pygame.image.load(endless_button_path), image_path=endless_button_path,
                                pos=(1490, 830), endless_button=1)

        endless_button.changeCondition(play_mouse_pos)
        endless_button.update(SCREEN)

        return_to_main_menu_P = Button(image=pygame.image.load("Resources/Textures/return_button_disabled.png"),
                                       image_path="Resources/Textures/return_button_disabled.png", pos=(310, 900))

        return_to_main_menu_P.changeCondition(play_mouse_pos)
        return_to_main_menu_P.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_main_menu_P.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    main_menu()
                if choose_difficulty.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    CHOSEN_DIFFICULTY = difficulty_list(return_to_main_menu_P)
                if level01_button.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    level_01()
                if level02_button.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    level_02()
                if level03_button.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    level_03()
                if endless_button.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    endless_mode()
        pygame.display.update()


def level_background(lvl_n):
    if lvl_n == 'endless':
        CANVAS.blit(level_02_background, (-240, 0))
    else:
        if lvl_n == 1:
            CANVAS.blit(level_01_background, (-560, 0))
        elif lvl_n == 2:
            CANVAS.blit(level_02_background, (-240, 0))
        elif lvl_n == 3:
            CANVAS.blit(level_03_background, (-240, 0))
        for i in range(22):
            for j in range(1, 8):
                CANVAS.blit(wall_image, (j * - 50 + screen_scroll, i * 50))
        for i in range(22):
            for j in range(1, 8):
                CANVAS.blit(wall_image, (5950 + j * 50 + screen_scroll, i * 50))
    for i in range(18):
        for j in range(len(MAP_MATRIX[i])):
            if MAP_MATRIX[i][j] == 'P':
                CANVAS.blit(wall_image, (j * 50 + screen_scroll, i * 50))
            elif MAP_MATRIX[i][j] == 'L':
                CANVAS.blit(ladder_image, (j * 50 + screen_scroll, i * 50))
    for i in range(4):
        for j in range(len(MAP_MATRIX[i])):
            CANVAS.blit(wall_image, (j * 50 + screen_scroll, 900 + i * 50))

    SCREEN.blit(CANVAS, (240, 0))


def level_01():
    completed = False
    global TURRETS_DESTROYED
    TURRETS_DESTROYED = 0
    global CHOSEN_DIFFICULTY
    bullet_group.empty()
    enemy_bullet_group.empty()
    turret_group.empty()
    TURRET_HEALTH = 0
    CHARACTER_HEALTH = 0
    BULLET_SPEED = 0
    if CHOSEN_DIFFICULTY == 'beginner':
        TURRET_HEALTH = 1
        CHARACTER_HEALTH = 4
        BULLET_SPEED = 2
    if CHOSEN_DIFFICULTY == 'medium':
        TURRET_HEALTH = 2
        CHARACTER_HEALTH = 3
        BULLET_SPEED = 3
    if CHOSEN_DIFFICULTY == 'hard':
        TURRET_HEALTH = 3
        CHARACTER_HEALTH = 2
        BULLET_SPEED = 4
    if CHOSEN_DIFFICULTY == 'insane':
        TURRET_HEALTH = 4
        CHARACTER_HEALTH = 1
        BULLET_SPEED = 5

    global screen_scroll
    screen_scroll = 0
    player = Character(700, 770, CHARACTER_SPEED, CHARACTER_HEALTH)
    portal = Portal(6150, 370, CHOSEN_DIFFICULTY)
    playing = True
    move_left = False
    move_right = False

    level_num = 1

    MAP_MATRIX.clear()
    for i in range(18):
        MAP_MATRIX.append([])
        for j in range(120):
            if i == 0 or i == 17 or j == 0 or j == 119:
                MAP_MATRIX[len(MAP_MATRIX) - 1].append('P')
            else:
                MAP_MATRIX[len(MAP_MATRIX) - 1].append('0')

    for i in range(6, 8):
        for j in range(9, 23):
            MAP_MATRIX[i][j] = 'P'
    for i in range(12, 14):
        for j in range(8, 13):
            MAP_MATRIX[i][j] = 'P'
    for i in range(12, 14):
        for j in range(21, 25):
            MAP_MATRIX[i][j] = 'P'
    for i in range(11, 17):
        for j in range(29, 31):
            MAP_MATRIX[i][j] = 'P'
    for i in range(9, 11):
        for j in range(29, 38):
            MAP_MATRIX[i][j] = 'P'
    for i in range(4, 6):
        for j in range(42, 53):
            MAP_MATRIX[i][j] = 'P'
    for i in range(12, 17):
        for j in range(41, 44):
            MAP_MATRIX[i][j] = 'P'
    for i in range(10, 12):
        for j in range(47, 58):
            MAP_MATRIX[i][j] = 'P'
    for i in range(4, 6):
        for j in range(59, 63):
            MAP_MATRIX[i][j] = 'P'
    for i in range(9, 17):
        for j in range(63, 71):
            MAP_MATRIX[i][j] = 'P'
    for i in range(12, 14):
        for j in range(73, 77):
            MAP_MATRIX[i][j] = 'P'
    for i in range(7, 9):
        for j in range(80, 89):
            MAP_MATRIX[i][j] = 'P'
    for i in range(13, 15):
        for j in range(80, 90):
            MAP_MATRIX[i][j] = 'P'
    for i in range(9, 11):
        for j in range(94, 119):
            MAP_MATRIX[i][j] = 'P'
    for i in range(9, 17):
        for j in range(94, 96):
            MAP_MATRIX[i][j] = 'P'

    MAP_MATRIX[4][15] = 'T'
    MAP_MATRIX[15][17] = 'T'
    MAP_MATRIX[7][30] = 'T'
    MAP_MATRIX[15][35] = 'T'
    MAP_MATRIX[2][47] = 'T'
    MAP_MATRIX[15][45] = 'T'
    MAP_MATRIX[8][55] = 'T'
    MAP_MATRIX[15][53] = 'T'
    MAP_MATRIX[10][74] = 'T'
    MAP_MATRIX[5][83] = 'T'
    MAP_MATRIX[5][86] = 'T'
    MAP_MATRIX[11][87] = 'T'
    MAP_MATRIX[7][113] = 'T'

    for i in range(12, 17):
        MAP_MATRIX[i][7] = 'L'
    for i in range(6, 12):
        MAP_MATRIX[i][23] = 'L'
    for i in range(9, 17):
        MAP_MATRIX[i][28] = 'L'
    for i in range(12, 17):
        MAP_MATRIX[i][40] = 'L'
    for i in range(4, 10):
        MAP_MATRIX[i][53] = 'L'
    for i in range(10, 17):
        MAP_MATRIX[i][58] = 'L'
    for i in range(9, 17):
        MAP_MATRIX[i][62] = 'L'
    for i in range(7, 13):
        MAP_MATRIX[i][89] = 'L'
    for i in range(9, 17):
        MAP_MATRIX[i][93] = 'L'

    for i in range(18):
        for j in range(120):
            if MAP_MATRIX[i][j] == 'T':
                turret_group.add(Turret(j * 50 + 290, i * 50 + 50, TURRET_HEALTH, BULLET_SPEED))

    clock1 = pygame.time.get_ticks()

    while playing:

        clock.tick(FPS)
        level_background(level_num)
        change = player.move(move_left, move_right)
        for i in turret_group:
            i.update(change, player)
        portal.update(change)
        portal.draw()
        player.draw()
        bullet_group.update(change, turret_group, player)
        bullet_group.draw(SCREEN)
        enemy_bullet_group.update(change, player)
        enemy_bullet_group.draw(SCREEN)
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))

        if not player.check_alive:
            playing = False

        if portal.check_completion(player):
            playing = False
            completed = True
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_left = True
                    move_right = False
                    player.ladder = False
                    player.climbing = False
                if event.key == pygame.K_d:
                    move_right = True
                    move_left = False
                    player.ladder = False
                    player.climbing = False
                if event.key == pygame.K_SPACE and not player.air:
                    player.jump = True
                    jump_sound.play()
                    jump_sound.set_volume(SOUNDS_VOLUME / 100)
                if event.key == pygame.K_ESCAPE:
                    playing = False
                if event.key == pygame.K_w and not move_left and not move_right:
                    player.climbing = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_d:
                    move_right = False
                if event.key == pygame.K_w:
                    player.climbing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if player.cooldown == 0:
                        player.cooldown = 30
                        shot_sound.play()
                        shot_sound.set_volume(SOUNDS_VOLUME / 100)
                        bullet_group.add(player.shoot())

        pygame.display.update()

    ticks = pygame.time.get_ticks() - clock1
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 60)
    hours = int(ticks / 3600000 % 24)
    if seconds < 10:
        seconds = '0' + str(seconds)
    if minutes < 10:
        minutes = '0' + str(minutes)
    if hours < 10:
        hours = '0' + str(hours)
    c_d = 0
    if CHOSEN_DIFFICULTY == 'medium':
        c_d = 1
    if CHOSEN_DIFFICULTY == 'hard':
        c_d = 2
    if CHOSEN_DIFFICULTY == 'insane':
        c_d = 3
    if completed:
        victory_sound.play()
        victory_sound.set_volume(SOUNDS_VOLUME / 100)
        if TURRETS_DESTROYED in range(12, 14):
            if data[c_d * 4][0] == '3':
                if int(data[38 + c_d * 12 + 0][:2]) * 3600 + int(data[39 + c_d * 12 + 0][:2]) * 60 + int(
                        data[40 + c_d * 12 + 0][:2]) > ticks / 1000:
                    data[38 + c_d * 12 + 0] = str(hours) + '\n'
                    data[39 + c_d * 12 + 0] = str(minutes) + '\n'
                    data[40 + c_d * 12 + 0] = str(seconds) + '\n'
            else:
                data[38 + c_d * 12 + 0] = str(hours) + '\n'
                data[39 + c_d * 12 + 0] = str(minutes) + '\n'
                data[40 + c_d * 12 + 0] = str(seconds) + '\n'

            data[c_d * 4] = '3\n'
        elif TURRETS_DESTROYED in range(8, 12) and data[c_d * 4][0] != '3':
            if data[c_d * 4][0] == '2':
                if int(data[38 + c_d * 12 + 0][:2]) * 3600 + int(data[39 + c_d * 12 + 0][:2]) * 60 + int(
                        data[40 + c_d * 12 + 0][:2]) > ticks / 1000:
                    data[38 + c_d * 12 + 0] = str(hours) + '\n'
                    data[39 + c_d * 12 + 0] = str(minutes) + '\n'
                    data[40 + c_d * 12 + 0] = str(seconds) + '\n'
            else:
                data[38 + c_d * 12 + 0] = str(hours) + '\n'
                data[39 + c_d * 12 + 0] = str(minutes) + '\n'
                data[40 + c_d * 12 + 0] = str(seconds) + '\n'
            data[c_d * 4] = '2\n'
        elif TURRETS_DESTROYED in range(0, 8) and data[c_d * 4][0] != '2' and data[c_d * 4][0] != '3':
            if data[c_d * 4][0] == '1':
                if int(data[38 + c_d * 12 + 0][:2]) * 3600 + int(data[39 + c_d * 12 + 0][:2]) * 60 + int(
                        data[40 + c_d * 12 + 0][:2]) > ticks / 1000:
                    data[38 + c_d * 12 + 0] = str(hours) + '\n'
                    data[39 + c_d * 12 + 0] = str(minutes) + '\n'
                    data[40 + c_d * 12 + 0] = str(seconds) + '\n'
            else:
                data[38 + c_d * 12 + 0] = str(hours) + '\n'
                data[39 + c_d * 12 + 0] = str(minutes) + '\n'
                data[40 + c_d * 12 + 0] = str(seconds) + '\n'
            data[c_d * 4] = '1\n'
    else:
        game_over_sound.play()
        game_over_sound.set_volume(SOUNDS_VOLUME / 100)

    info_copy = open('Resources/Other/info.txt', 'w')
    for i in data:
        info_copy.write(i)
    info_copy.close()

    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        retry_button = Button(image=pygame.image.load("Resources/Textures/restart_button_disabled.png"),
                              image_path="Resources/Textures/restart_button_disabled.png", pos=(790, 700))

        retry_button.changeCondition(play_mouse_pos)
        retry_button.update(SCREEN)

        return_to_level_menu = Button(image=pygame.image.load("Resources/Textures/exit_button_disabled.png"),
                                      image_path="Resources/Textures/exit_button_disabled.png", pos=(1130, 700))

        return_to_level_menu.changeCondition(play_mouse_pos)
        return_to_level_menu.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                victory_sound.stop()
                game_over_sound.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_level_menu.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    victory_sound.stop()
                    game_over_sound.stop()
                    play()
                if retry_button.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    victory_sound.stop()
                    game_over_sound.stop()
                    level_01()

        pygame.display.update()


def level_02():
    completed = False
    global TURRETS_DESTROYED
    TURRETS_DESTROYED = 0
    global CHOSEN_DIFFICULTY
    bullet_group.empty()
    enemy_bullet_group.empty()
    turret_group.empty()
    TURRET_HEALTH = 0
    CHARACTER_HEALTH = 0
    BULLET_SPEED = 0
    if CHOSEN_DIFFICULTY == 'beginner':
        TURRET_HEALTH = 1
        CHARACTER_HEALTH = 4
        BULLET_SPEED = 2
    if CHOSEN_DIFFICULTY == 'medium':
        TURRET_HEALTH = 2
        CHARACTER_HEALTH = 3
        BULLET_SPEED = 3
    if CHOSEN_DIFFICULTY == 'hard':
        TURRET_HEALTH = 3
        CHARACTER_HEALTH = 2
        BULLET_SPEED = 4
    if CHOSEN_DIFFICULTY == 'insane':
        TURRET_HEALTH = 4
        CHARACTER_HEALTH = 1
        BULLET_SPEED = 5

    global screen_scroll
    screen_scroll = 0
    player = Character(700, 770, CHARACTER_SPEED, CHARACTER_HEALTH)
    portal = Portal(6150, 570, CHOSEN_DIFFICULTY)
    playing = True
    move_left = False
    move_right = False
    level_num = 2

    MAP_MATRIX.clear()
    for i in range(18):
        MAP_MATRIX.append([])
        for j in range(120):
            if i == 0 or i == 17 or j == 0 or j == 119:
                MAP_MATRIX[len(MAP_MATRIX) - 1].append('P')
            else:
                MAP_MATRIX[len(MAP_MATRIX) - 1].append('0')

    for i in range(6, 8):
        for j in range(9, 17):
            MAP_MATRIX[i][j] = 'P'
    for i in range(12, 14):
        for j in range(8, 23):
            MAP_MATRIX[i][j] = 'P'
    for i in range(6, 8):
        for j in range(22, 26):
            MAP_MATRIX[i][j] = 'P'
    for i in range(11, 17):
        for j in range(28, 38):
            MAP_MATRIX[i][j] = 'P'
    for i in range(6, 8):
        for j in range(40, 47):
            MAP_MATRIX[i][j] = 'P'
    for i in range(13, 17):
        for j in range(41, 45):
            MAP_MATRIX[i][j] = 'P'
    for i in range(12, 17):
        for j in range(48, 55):
            MAP_MATRIX[i][j] = 'P'
    for i in range(13, 15):
        for j in range(57, 69):
            MAP_MATRIX[i][j] = 'P'
    for i in range(6, 8):
        for j in range(58, 69):
            MAP_MATRIX[i][j] = 'P'
    for i in range(9, 13):
        for j in range(73, 79):
            MAP_MATRIX[i][j] = 'P'
    for i in range(13, 17):
        for j in range(73, 77):
            MAP_MATRIX[i][j] = 'P'
    for i in range(8, 12):
        for j in range(83, 89):
            MAP_MATRIX[i][j] = 'P'
    for i in range(11, 13):
        for j in range(92, 97):
            MAP_MATRIX[i][j] = 'P'
    for i in range(13, 17):
        for j in range(98, 119):
            MAP_MATRIX[i][j] = 'P'

    MAP_MATRIX[10][17] = 'T'
    MAP_MATRIX[15][25] = 'T'
    MAP_MATRIX[4][23] = 'T'
    MAP_MATRIX[9][33] = 'T'
    MAP_MATRIX[4][43] = 'T'
    MAP_MATRIX[15][46] = 'T'
    MAP_MATRIX[10][50] = 'T'
    MAP_MATRIX[4][60] = 'T'
    MAP_MATRIX[4][66] = 'T'
    MAP_MATRIX[11][62] = 'T'
    MAP_MATRIX[6][85] = 'T'
    MAP_MATRIX[11][113] = 'T'

    for i in range(12, 17):
        MAP_MATRIX[i][7] = 'L'
    for i in range(6, 12):
        MAP_MATRIX[i][8] = 'L'
    for i in range(11, 17):
        MAP_MATRIX[i][27] = 'L'
    for i in range(6, 12):
        MAP_MATRIX[i][21] = 'L'
    for i in range(13, 17):
        MAP_MATRIX[i][40] = 'L'
    for i in range(6, 17):
        MAP_MATRIX[i][39] = 'L'
    for i in range(12, 17):
        MAP_MATRIX[i][47] = 'L'
    for i in range(6, 13):
        MAP_MATRIX[i][57] = 'L'
    for i in range(9, 17):
        MAP_MATRIX[i][72] = 'L'
    for i in range(8, 17):
        MAP_MATRIX[i][82] = 'L'
    for i in range(11, 17):
        MAP_MATRIX[i][91] = 'L'

    for i in range(18):
        for j in range(120):
            if MAP_MATRIX[i][j] == 'T':
                turret_group.add(Turret(j * 50 + 290, i * 50 + 50, TURRET_HEALTH, BULLET_SPEED))

    clock2 = pygame.time.get_ticks()

    while playing:
        play_mouse_pos = pygame.mouse.get_pos()

        clock.tick(FPS)
        level_background(level_num)
        change = player.move(move_left, move_right)
        for i in turret_group:
            i.update(change, player)
        portal.update(change)
        portal.draw()
        player.draw()
        bullet_group.update(change, turret_group, player)
        bullet_group.draw(SCREEN)
        enemy_bullet_group.update(change, player)
        enemy_bullet_group.draw(SCREEN)
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))

        if not player.check_alive:
            playing = False

        if portal.check_completion(player):
            playing = False
            completed = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_left = True
                    move_right = False
                    player.ladder = False
                    player.climbing = False
                if event.key == pygame.K_d:
                    move_right = True
                    move_left = False
                    player.ladder = False
                    player.climbing = False
                if event.key == pygame.K_SPACE and not player.air:
                    player.jump = True
                    jump_sound.play()
                    jump_sound.set_volume(SOUNDS_VOLUME / 100)
                if event.key == pygame.K_ESCAPE:
                    playing = False
                if event.key == pygame.K_w and not move_left and not move_right:
                    player.climbing = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_d:
                    move_right = False
                if event.key == pygame.K_w:
                    player.climbing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if player.cooldown == 0:
                        player.cooldown = 30
                        shot_sound.play()
                        shot_sound.set_volume(SOUNDS_VOLUME / 100)
                        bullet_group.add(player.shoot())

        pygame.display.update()

    ticks = pygame.time.get_ticks() - clock2
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 60)
    hours = int(ticks / 3600000 % 24)
    if seconds < 10:
        seconds = '0' + str(seconds)
    if minutes < 10:
        minutes = '0' + str(minutes)
    if hours < 10:
        hours = '0' + str(hours)
    c_d = 0
    if CHOSEN_DIFFICULTY == 'medium':
        c_d = 1
    if CHOSEN_DIFFICULTY == 'hard':
        c_d = 2
    if CHOSEN_DIFFICULTY == 'insane':
        c_d = 3

    if completed:
        victory_sound.play()
        victory_sound.set_volume(SOUNDS_VOLUME / 100)
        if TURRETS_DESTROYED in range(11, 13):
            if data[c_d * 4 + 1][0] == '3':
                if int(data[38 + c_d * 12 + 4][:2]) * 3600 + int(data[39 + c_d * 12 + 4][:2]) * 60 + int(
                        data[40 + c_d * 12 + 4][:2]) > ticks / 1000:
                    data[38 + c_d * 12 + 4] = str(hours) + '\n'
                    data[39 + c_d * 12 + 4] = str(minutes) + '\n'
                    data[40 + c_d * 12 + 4] = str(seconds) + '\n'
            else:
                data[38 + c_d * 12 + 4] = str(hours) + '\n'
                data[39 + c_d * 12 + 4] = str(minutes) + '\n'
                data[40 + c_d * 12 + 4] = str(seconds) + '\n'
            data[c_d * 4 + 1] = '3\n'
        elif TURRETS_DESTROYED in range(7, 11) and data[c_d * 4 + 1][0] != '3':
            if data[c_d * 4 + 1][0] == '2':
                if int(data[38 + c_d * 12 + 4][:2]) * 3600 + int(data[39 + c_d * 12 + 4][:2]) * 60 + int(
                        data[40 + c_d * 12 + 4][:2]) > ticks / 1000:
                    data[38 + c_d * 12 + 4] = str(hours) + '\n'
                    data[39 + c_d * 12 + 4] = str(minutes) + '\n'
                    data[40 + c_d * 12 + 4] = str(seconds) + '\n'
            else:
                data[38 + c_d * 12 + 4] = str(hours) + '\n'
                data[39 + c_d * 12 + 4] = str(minutes) + '\n'
                data[40 + c_d * 12 + 4] = str(seconds) + '\n'
            data[c_d * 4 + 1] = '2\n'
        elif TURRETS_DESTROYED in range(0, 7) and data[c_d * 4 + 1][0] != '2' and data[c_d * 4 + 1][0] != '3':
            if data[c_d * 4 + 1][0] == '1':
                if int(data[38 + c_d * 12 + 4][:2]) * 3600 + int(data[39 + c_d * 12 + 4][:2]) * 60 + int(
                        data[40 + c_d * 12 + 4][:2]) > ticks / 1000:
                    data[38 + c_d * 12 + 4] = str(hours) + '\n'
                    data[39 + c_d * 12 + 4] = str(minutes) + '\n'
                    data[40 + c_d * 12 + 4] = str(seconds) + '\n'
            else:
                data[38 + c_d * 12 + 4] = str(hours) + '\n'
                data[39 + c_d * 12 + 4] = str(minutes) + '\n'
                data[40 + c_d * 12 + 4] = str(seconds) + '\n'
            data[c_d * 4 + 1] = '1\n'
    else:
        game_over_sound.play()
        game_over_sound.set_volume(SOUNDS_VOLUME / 100)

    info_copy = open('Resources/Other/info.txt', 'w')
    for i in data:
        info_copy.write(i)
    info_copy.close()

    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        retry_button = Button(image=pygame.image.load("Resources/Textures/restart_button_disabled.png"),
                              image_path="Resources/Textures/restart_button_disabled.png", pos=(790, 700))

        retry_button.changeCondition(play_mouse_pos)
        retry_button.update(SCREEN)

        return_to_level_menu = Button(image=pygame.image.load("Resources/Textures/exit_button_disabled.png"),
                                      image_path="Resources/Textures/exit_button_disabled.png", pos=(1130, 700))

        return_to_level_menu.changeCondition(play_mouse_pos)
        return_to_level_menu.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_sound.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_level_menu.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    victory_sound.stop()
                    game_over_sound.stop()
                    play()
                if retry_button.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    victory_sound.stop()
                    game_over_sound.stop()
                    level_02()

        pygame.display.update()


def level_03():
    completed = False
    global TURRETS_DESTROYED
    TURRETS_DESTROYED = 0
    global CHOSEN_DIFFICULTY
    bullet_group.empty()
    enemy_bullet_group.empty()
    turret_group.empty()
    TURRET_HEALTH = 0
    CHARACTER_HEALTH = 0
    BULLET_SPEED = 0
    if CHOSEN_DIFFICULTY == 'beginner':
        TURRET_HEALTH = 1
        CHARACTER_HEALTH = 4
        BULLET_SPEED = 2
    if CHOSEN_DIFFICULTY == 'medium':
        TURRET_HEALTH = 2
        CHARACTER_HEALTH = 3
        BULLET_SPEED = 3
    if CHOSEN_DIFFICULTY == 'hard':
        TURRET_HEALTH = 3
        CHARACTER_HEALTH = 2
        BULLET_SPEED = 4
    if CHOSEN_DIFFICULTY == 'insane':
        TURRET_HEALTH = 4
        CHARACTER_HEALTH = 1
        BULLET_SPEED = 5

    global screen_scroll
    screen_scroll = 0
    player = Character(700, 770, CHARACTER_SPEED, CHARACTER_HEALTH)
    portal = Portal(6150, 470, CHOSEN_DIFFICULTY)
    playing = True
    move_left = False
    move_right = False
    level_num = 3

    MAP_MATRIX.clear()
    for i in range(18):
        MAP_MATRIX.append([])
        for j in range(120):
            if i == 0 or i == 17 or j == 0 or j == 119:
                MAP_MATRIX[len(MAP_MATRIX) - 1].append('P')
            else:
                MAP_MATRIX[len(MAP_MATRIX) - 1].append('0')

    for i in range(9, 11):
        for j in range(8, 12):
            MAP_MATRIX[i][j] = 'P'
    for i in range(9, 11):
        for j in range(18, 22):
            MAP_MATRIX[i][j] = 'P'
    for i in range(14, 16):
        for j in range(10, 14):
            MAP_MATRIX[i][j] = 'P'
    for i in range(14, 16):
        for j in range(23, 27):
            MAP_MATRIX[i][j] = 'P'
    for i in range(12, 17):
        for j in range(28, 32):
            MAP_MATRIX[i][j] = 'P'
    for i in range(10, 17):
        for j in range(34, 39):
            MAP_MATRIX[i][j] = 'P'
    for i in range(11, 17):
        for j in range(45, 50):
            MAP_MATRIX[i][j] = 'P'
    for i in range(11, 13):
        for j in range(52, 62):
            MAP_MATRIX[i][j] = 'P'
    for i in range(5, 7):
        for j in range(52, 62):
            MAP_MATRIX[i][j] = 'P'
    for i in range(9, 11):
        for j in range(65, 69):
            MAP_MATRIX[i][j] = 'P'
    for i in range(8, 10):
        for j in range(71, 78):
            MAP_MATRIX[i][j] = 'P'
    for i in range(10, 17):
        for j in range(75, 78):
            MAP_MATRIX[i][j] = 'P'
    for i in range(6, 9):
        for j in range(83, 90):
            MAP_MATRIX[i][j] = 'P'
    for i in range(13, 17):
        for j in range(83, 89):
            MAP_MATRIX[i][j] = 'P'
    for i in range(8, 11):
        for j in range(93, 99):
            MAP_MATRIX[i][j] = 'P'
    for i in range(14, 16):
        for j in range(99, 102):
            MAP_MATRIX[i][j] = 'P'
    for i in range(11, 17):
        for j in range(103, 119):
            MAP_MATRIX[i][j] = 'P'

    MAP_MATRIX[7][9] = 'T'
    MAP_MATRIX[15][19] = 'T'
    MAP_MATRIX[7][20] = 'T'
    MAP_MATRIX[10][30] = 'T'
    MAP_MATRIX[15][42] = 'T'
    MAP_MATRIX[3][55] = 'T'
    MAP_MATRIX[9][55] = 'T'
    MAP_MATRIX[3][60] = 'T'
    MAP_MATRIX[9][60] = 'T'
    MAP_MATRIX[6][74] = 'T'
    MAP_MATRIX[4][87] = 'T'
    MAP_MATRIX[6][95] = 'T'
    MAP_MATRIX[12][100] = 'T'

    for i in range(14, 17):
        MAP_MATRIX[i][9] = 'L'
    for i in range(9, 17):
        MAP_MATRIX[i][22] = 'L'
    for i in range(9, 14):
        MAP_MATRIX[i][12] = 'L'
    for i in range(10, 17):
        MAP_MATRIX[i][33] = 'L'
    for i in range(11, 17):
        MAP_MATRIX[i][44] = 'L'
    for i in range(5, 17):
        MAP_MATRIX[i][62] = 'L'
    for i in range(8, 17):
        MAP_MATRIX[i][70] = 'L'
    for i in range(13, 17):
        MAP_MATRIX[i][82] = 'L'
    for i in range(8, 17):
        MAP_MATRIX[i][92] = 'L'
    for i in range(11, 17):
        MAP_MATRIX[i][102] = 'L'

    for i in range(18):
        for j in range(120):
            if MAP_MATRIX[i][j] == 'T':
                turret_group.add(Turret(j * 50 + 290, i * 50 + 50, TURRET_HEALTH, BULLET_SPEED))

    clock3 = pygame.time.get_ticks()

    while playing:
        play_mouse_pos = pygame.mouse.get_pos()

        clock.tick(FPS)
        level_background(level_num)
        change = player.move(move_left, move_right)
        for i in turret_group:
            i.update(change, player)
        portal.update(change)
        portal.draw()
        player.draw()
        bullet_group.update(change, turret_group, player)
        bullet_group.draw(SCREEN)
        enemy_bullet_group.update(change, player)
        enemy_bullet_group.draw(SCREEN)
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))

        if not player.check_alive:
            playing = False

        if portal.check_completion(player):
            playing = False
            completed = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_left = True
                    move_right = False
                    player.ladder = False
                    player.climbing = False
                if event.key == pygame.K_d:
                    move_right = True
                    move_left = False
                    player.ladder = False
                    player.climbing = False
                if event.key == pygame.K_SPACE and not player.air:
                    player.jump = True
                    jump_sound.play()
                    jump_sound.set_volume(SOUNDS_VOLUME / 100)
                if event.key == pygame.K_ESCAPE:
                    playing = False
                if event.key == pygame.K_w and not move_left and not move_right:
                    player.climbing = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_d:
                    move_right = False
                if event.key == pygame.K_w:
                    player.climbing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if player.cooldown == 0:
                        player.cooldown = 30
                        shot_sound.play()
                        shot_sound.set_volume(SOUNDS_VOLUME / 100)
                        bullet_group.add(player.shoot())

        pygame.display.update()

    ticks = pygame.time.get_ticks() - clock3
    seconds = int(ticks / 1000 % 60)
    minutes = int(ticks / 60000 % 60)
    hours = int(ticks / 3600000 % 24)
    if seconds < 10:
        seconds = '0' + str(seconds)
    if minutes < 10:
        minutes = '0' + str(minutes)
    if hours < 10:
        hours = '0' + str(hours)
    c_d = 0
    if CHOSEN_DIFFICULTY == 'medium':
        c_d = 1
    if CHOSEN_DIFFICULTY == 'hard':
        c_d = 2
    if CHOSEN_DIFFICULTY == 'insane':
        c_d = 3

    if completed:
        victory_sound.play()
        victory_sound.set_volume(SOUNDS_VOLUME / 100)
        if TURRETS_DESTROYED in range(12, 14):
            if data[c_d * 4 + 2][0] == '3':
                if int(data[38 + c_d * 12 + 8][:2]) * 3600 + int(data[39 + c_d * 12 + 8][:2]) * 60 + int(
                        data[40 + c_d * 12 + 8][:2]) > ticks / 1000:
                    data[38 + c_d * 12 + 8] = str(hours) + '\n'
                    data[39 + c_d * 12 + 8] = str(minutes) + '\n'
                    data[40 + c_d * 12 + 8] = str(seconds) + '\n'
            else:
                data[38 + c_d * 12 + 8] = str(hours) + '\n'
                data[39 + c_d * 12 + 8] = str(minutes) + '\n'
                data[40 + c_d * 12 + 8] = str(seconds) + '\n'
            data[c_d * 4 + 2] = '3\n'
        elif TURRETS_DESTROYED in range(8, 12) and data[c_d * 4 + 2][0] != '3':
            if data[c_d * 4 + 2][0] == '2':
                if int(data[38 + c_d * 12 + 8][:2]) * 3600 + int(data[39 + c_d * 12 + 8][:2]) * 60 + int(
                        data[40 + c_d * 12 + 8][:2]) > ticks / 1000:
                    data[38 + c_d * 12 + 8] = str(hours) + '\n'
                    data[39 + c_d * 12 + 8] = str(minutes) + '\n'
                    data[40 + c_d * 12 + 8] = str(seconds) + '\n'
            else:
                data[38 + c_d * 12 + 8] = str(hours) + '\n'
                data[39 + c_d * 12 + 8] = str(minutes) + '\n'
                data[40 + c_d * 12 + 8] = str(seconds) + '\n'
            data[c_d * 4 + 2] = '2\n'
        elif TURRETS_DESTROYED in range(0, 8) and data[c_d * 4 + 2][0] != '2' and data[c_d * 4 + 2][0] != '3':
            if data[c_d * 4 + 2][0] == '1':
                if int(data[38 + c_d * 12 + 8][:2]) * 3600 + int(data[39 + c_d * 12 + 8][:2]) * 60 + int(
                        data[40 + c_d * 12 + 8][:2]) > ticks / 1000:
                    data[38 + c_d * 12 + 8] = str(hours) + '\n'
                    data[39 + c_d * 12 + 8] = str(minutes) + '\n'
                    data[40 + c_d * 12 + 8] = str(seconds) + '\n'
            else:
                data[38 + c_d * 12 + 8] = str(hours) + '\n'
                data[39 + c_d * 12 + 8] = str(minutes) + '\n'
                data[40 + c_d * 12 + 8] = str(seconds) + '\n'
            data[c_d * 4 + 2] = '1\n'
    else:
        game_over_sound.play()
        game_over_sound.set_volume(SOUNDS_VOLUME / 100)

    info_copy = open('Resources/Other/info.txt', 'w')
    for i in data:
        info_copy.write(i)
    info_copy.close()

    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        retry_button = Button(image=pygame.image.load("Resources/Textures/restart_button_disabled.png"),
                              image_path="Resources/Textures/restart_button_disabled.png", pos=(790, 700))

        retry_button.changeCondition(play_mouse_pos)
        retry_button.update(SCREEN)

        return_to_level_menu = Button(image=pygame.image.load("Resources/Textures/exit_button_disabled.png"),
                                      image_path="Resources/Textures/exit_button_disabled.png", pos=(1130, 700))

        return_to_level_menu.changeCondition(play_mouse_pos)
        return_to_level_menu.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_sound.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_level_menu.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    victory_sound.stop()
                    game_over_sound.stop()
                    play()
                if retry_button.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    victory_sound.stop()
                    game_over_sound.stop()
                    level_03()

        pygame.display.update()


def endless_mode():
    global MAP_MATRIX
    global MAP_SEGMENTS
    global MAP_SEGMENTS_NUMS
    global GLOBAL_X
    GLOBAL_X = -500
    bullet_group.empty()
    enemy_bullet_group.empty()
    turret_group.empty()
    global screen_scroll
    screen_scroll = 0
    player = Character(700, 770, 5, 4)
    playing = True
    move_left = False
    move_right = False
    level_num = 'endless'
    MAP_SEGMENTS_NUMS.clear()
    MAP_SEGMENTS_NUMS = [rd(0, 12), rd(0, 12), rd(0, 12)]
    MAP_MATRIX.clear()
    for i in range(18):
        MAP_MATRIX.append([])
        for j in range(24):
            if i == 0 or i == 17 or j < 8:
                MAP_MATRIX[i].append('P')
            else:
                MAP_MATRIX[i].append('0')
    endless_map_update()

    turrets_update = 0
    for i in range(18):
        for j in range(turrets_update, len(MAP_MATRIX[0])):
            if MAP_MATRIX[i][j] == 'T':
                turret_group.add(Turret(j * 50 + 290 + screen_scroll, i * 50 + 50, 3, 4))

    map_last_update = 0
    turrets_update += 72

    while playing:
        clock.tick(FPS)
        level_background(level_num)
        change = player.move(move_left, move_right)
        for i in turret_group:
            i.update(change, player)
        player.draw()
        bullet_group.update(change, turret_group, player)
        bullet_group.draw(SCREEN)
        enemy_bullet_group.update(change, player)
        enemy_bullet_group.draw(SCREEN)
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))

        if not player.check_alive:
            playing = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    move_right = False
                    move_left = True
                    player.ladder = False
                    player.climbing = False
                if event.key == pygame.K_d:
                    move_left = False
                    move_right = True
                    player.ladder = False
                    player.climbing = False
                if event.key == pygame.K_SPACE and not player.air:
                    player.jump = True
                    jump_sound.play()
                    jump_sound.set_volume(SOUNDS_VOLUME / 100)
                if event.key == pygame.K_ESCAPE:
                    bullet_group.empty()
                    enemy_bullet_group.empty()
                    turret_group.empty()
                    playing = False
                if event.key == pygame.K_w and not move_left and not move_right:
                    player.climbing = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    move_left = False
                if event.key == pygame.K_d:
                    move_right = False
                if event.key == pygame.K_w:
                    player.climbing = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if player.cooldown == 0:
                        player.cooldown = 30
                        shot_sound.play()
                        shot_sound.set_volume(SOUNDS_VOLUME / 100)
                        bullet_group.add(player.shoot())

        if GLOBAL_X % 3600 in range(1500, 1600) and GLOBAL_X - map_last_update not in range(0,
                                                                                            100) and GLOBAL_X > map_last_update:
            for i in range(GLOBAL_X, GLOBAL_X + 102):
                if i % 3600 == 1600:
                    map_last_update = i
            MAP_SEGMENTS_NUMS.append(rd(0, 12))
            MAP_SEGMENTS_NUMS.append(rd(0, 12))
            MAP_SEGMENTS_NUMS.append(rd(0, 12))
            endless_map_update()
            for i in range(18):
                for j in range(turrets_update, len(MAP_MATRIX[0])):
                    if MAP_MATRIX[i][j] == 'T':
                        turret_group.add(Turret(j * 50 + 290 + screen_scroll, i * 50 + 50, 3, 4))
            turrets_update += 72

        pygame.display.update()

    game_over_sound.play()
    game_over_sound.set_volume(SOUNDS_VOLUME / 100)
    data[87] = str(max(int(data[87]), (GLOBAL_X + 500) // 50))
    info_copy = open('Resources/Other/info.txt', 'w')
    for i in data:
        info_copy.write(i)
    info_copy.close()
    while True:
        play_mouse_pos = pygame.mouse.get_pos()

        retry_button = Button(image=pygame.image.load("Resources/Textures/restart_button_disabled.png"),
                              image_path="Resources/Textures/restart_button_disabled.png", pos=(790, 700))

        retry_button.changeCondition(play_mouse_pos)
        retry_button.update(SCREEN)

        return_to_level_menu = Button(image=pygame.image.load("Resources/Textures/exit_button_disabled.png"),
                                      image_path="Resources/Textures/exit_button_disabled.png", pos=(1130, 700))

        return_to_level_menu.changeCondition(play_mouse_pos)
        return_to_level_menu.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over_sound.stop()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_level_menu.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    game_over_sound.stop()
                    play()
                if retry_button.checkForInput(play_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    game_over_sound.stop()
                    endless_mode()

        pygame.display.update()


def options():
    global SOUNDS_VOLUME
    global SONG_VOLUME
    while True:

        options_mouse_pos = pygame.mouse.get_pos()

        SCREEN.fill("#121212")
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))
        return_to_main_menu_O = Button(image=pygame.image.load("Resources/Textures/return_button_disabled.png"),
                                       image_path="Resources/Textures/return_button_disabled.png", pos=(310, 900))

        return_to_main_menu_O.changeCondition(options_mouse_pos)
        return_to_main_menu_O.update(SCREEN)

        song_on_off_button = Button(image=pygame.image.load("Resources/Textures/music_en_dis_button_disabled.png"),
                                    image_path="Resources/Textures/music_en_dis_button_disabled.png", pos=(530, 300))
        song_on_off_button.changeCondition(options_mouse_pos)
        song_on_off_button.update(SCREEN)

        sounds_on_off_button = Button(image=pygame.image.load("Resources/Textures/volume_en_dis_button_disabled.png"),
                                      image_path="Resources/Textures/volume_en_dis_button_disabled.png", pos=(530, 600))
        sounds_on_off_button.changeCondition(options_mouse_pos)
        sounds_on_off_button.update(SCREEN)

        song_volume_buttons = []
        for i in range(10):
            song_vol_button_condition = ""
            if data[i + 16][:2] == "of":
                song_vol_button_condition = "off"
            else:
                song_vol_button_condition = "on"
            song_volume_button_path = "Resources/Textures/volume_button_" + song_vol_button_condition + "_disabled.png"
            song_volume_buttons.append(
                Button(image=pygame.image.load(song_volume_button_path), image_path=song_volume_button_path,
                       pos=(800 + i * 70, 300)))
        for i in range(10):
            song_volume_buttons[i].changeCondition(options_mouse_pos)
            song_volume_buttons[i].update(SCREEN)

        sounds_volume_buttons = []
        for i in range(10):
            sounds_vol_button_condition = ""
            if data[i + 27][:2] == "of":
                sounds_vol_button_condition = "off"
            else:
                sounds_vol_button_condition = "on"
            sounds_volume_button_path = "Resources/Textures/volume_button_" + sounds_vol_button_condition + \
                                        "_disabled.png"
            sounds_volume_buttons.append(
                Button(image=pygame.image.load(sounds_volume_button_path), image_path=sounds_volume_button_path,
                       pos=(800 + i * 70, 600)))
        for i in range(10):
            sounds_volume_buttons[i].changeCondition(options_mouse_pos)
            sounds_volume_buttons[i].update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if return_to_main_menu_O.checkForInput(options_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    main_menu()
                if song_on_off_button.checkForInput(options_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    if not SONG_VOLUME:
                        SONG_VOLUME = 10
                        data[16] = "on"
                    else:
                        SONG_VOLUME = 0
                        data[16] = "off"
                    for i in range(17, 26):
                        data[i] = "off"

                if sounds_on_off_button.checkForInput(options_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    if not SOUNDS_VOLUME:
                        SOUNDS_VOLUME = 10
                        data[27] = "on"
                    else:
                        SOUNDS_VOLUME = 0
                        data[27] = "off"
                    for i in range(28, 37):
                        data[i] = "off"

                for i in range(10):
                    if song_volume_buttons[i].checkForInput(options_mouse_pos):
                        SONG_VOLUME = i * 10 + 10
                        button_click_sound.play()
                        button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                        for j in range(16, 17 + i):
                            data[j] = "on"
                        for j in range(17 + i, 26):
                            data[j] = "off"
                info_copy = open('Resources/Other/info.txt', 'w')
                for j in data:
                    w_str = j
                    if j in ["on", "off"]:
                        w_str += '\n'
                    info_copy.write(w_str)
                info_copy.close()
                background_theme.set_volume(SONG_VOLUME / 100)

                for i in range(10):
                    if sounds_volume_buttons[i].checkForInput(options_mouse_pos):
                        SOUNDS_VOLUME = i * 10 + 10
                        button_click_sound.play()
                        button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                        for j in range(27, 28 + i):
                            data[j] = "on"
                        for j in range(28 + i, 37):
                            data[j] = "off"
                info_copy = open('Resources/Other/info.txt', 'w')
                for j in data:
                    w_str = j
                    if j in ["on", "off"]:
                        w_str += '\n'
                    info_copy.write(w_str)
                info_copy.close()

        pygame.display.update()


def main_menu():
    global SOUNDS_VOLUME
    global SONG_VOLUME
    while True:
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))

        SCREEN.fill("#121212")
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(0, 0, 240, 1080))
        pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(1680, 0, 240, 1080))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(100).render("GRAND BATTLE", True, "#b68f40")
        menu_rect = menu_text.get_rect(center=(960, 200))

        play_button = Button(image=pygame.image.load("Resources/Textures/play_button_disabled.png"),
                             image_path="Resources/Textures/play_button_disabled.png", pos=(960, 400))
        options_button = Button(image=pygame.image.load("Resources/Textures/options_button_disabled.png"),
                                image_path="Resources/Textures/options_button_disabled.png", pos=(960, 600))
        quit_button = Button(image=pygame.image.load("Resources/Textures/quit_button_disabled.png"),
                             image_path="Resources/Textures/quit_button_disabled.png", pos=(960, 800))

        SCREEN.blit(menu_text, menu_rect)

        for button in [play_button, options_button, quit_button]:
            button.changeCondition(menu_mouse_pos)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    play()
                if options_button.checkForInput(menu_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    options()
                if quit_button.checkForInput(menu_mouse_pos):
                    button_click_sound.play()
                    button_click_sound.set_volume(SOUNDS_VOLUME / 100)
                    pygame.quit()
                    sys.exit()
        pygame.display.update()


main_menu()
