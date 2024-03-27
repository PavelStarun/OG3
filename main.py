import pygame
import random
import tkinter as tk
import os

def start_game():
    root.destroy()


def quit_game():
    root.destroy()
    pygame.display.quit()


def reset_game():
    global start_ticks, hits, target_x, target_y, game_active, target_speed, target_direction
    start_ticks = pygame.time.get_ticks()
    hits = 0
    target_x = random.randint(0, SCREEN_WIDTH - target_width)
    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    game_active = True

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100, 100)

pygame.init()

pygame.mixer.music.load("music/fon.ogg")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)

hit_sound = pygame.mixer.Sound("music/shot.ogg")
hit_sound.set_volume(0.7)

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
target_image = pygame.image.load("img/mishen.png")
target_width, target_height = 80, 80
color = (76, 81, 74)
font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 26)


root = tk.Tk()
root.title("Приветствую тебя в моей первой игре! ИГРА - ТИР")
root.configure(bg="light blue")
width_tk = 470
height_tk = 270
center_x = 100 + (SCREEN_WIDTH - width_tk) // 2
center_y = 100 + (SCREEN_HEIGHT - height_tk) // 2
root.geometry(f'{width_tk}x{height_tk}+{center_x}+{center_y}')

tk_img = tk.PhotoImage(file="img/tkimg2.png")
tk_label = tk.Label(root, image=tk_img)
tk_label.place(x=0, y=0, relwidth=1, relheight=1)

button1 = tk.Button(root, text="Начать игру", bg="grey55", command=start_game)
button1.place(relx=0.32, rely=0.63, height=35, width=100)

button2 = tk.Button(root, text="Выйти", bg="grey54", command=quit_game)
button2.place(relx=0.32, rely=0.8, height=35, width=100)

root.mainloop()


level = 1
game_time = 10
reset_game()
target_speed_x = float(0.15)
target_speed_y = float(0.15)

lavel = True
while lavel():
    pass


pygame.quit()