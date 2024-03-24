import pygame
import random
import tkinter as tk


def start_game():
    root.destroy()

def quit_game():
    root.destroy()
    pygame.display.quit()


pygame.init()


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/apex.jpg")
pygame.display.set_icon(icon)

target_image = pygame.image.load("img/mishen.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (76, 81, 74)

root = tk.Tk()
root.title("Приветствую тебя в моей первой игре!")
root.configure(bg="light blue")
root.geometry("470x270")

tk_img = tk.PhotoImage(file="img/tkimg2.png")
tk_label = tk.Label(root, image=tk_img)
tk_label.place(x=0, y=0, relwidth=1, relheight=1)

button1 = tk.Button(root, text="Начать игру", bg="grey55", command=start_game)
button1.place(relx=0.32, rely=0.63, height=35, width=100)

button2 = tk.Button(root, text="Выйти", bg="grey54", command=quit_game)
button2.place(relx=0.32, rely=0.8, height=35, width=100)

root.mainloop()

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    screen.blit(target_image, (target_x, target_y))
    pygame.display.update()


pygame.quit()