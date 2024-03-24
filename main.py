import pygame
import random
import tkinter as tk


def start_game():
    root.destroy()

def quit_game():
    root.destroy()
    pygame.display.quit()

def reset_game():
    global start_ticks, hits, target_x, target_y, game_active
    start_ticks = pygame.time.get_ticks()
    hits = 0
    target_x = random.randint(0, SCREEN_WIDTH - target_width)
    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
    game_active = True

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

font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 26)
game_time = 10
reset_game()

running = True
while running:
    screen.fill(color)
    current_ticks = pygame.time.get_ticks()
    seconds_passed = (current_ticks - start_ticks) // 1000
    time_left = max(game_time - seconds_passed, 0)
    timer_text = font.render(f"Time Left: {time_left}s", True, (255, 255, 255))
    screen.blit(timer_text, (10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_active and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                hits += 1
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
        elif not game_active and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if retry_button.collidepoint(mouse_x, mouse_y):
                reset_game()

    if game_active:
        screen.blit(target_image, (target_x, target_y))
    else:
        result_text = font.render(f"Количество попаданий: {hits}", True, (255, 255, 255))
        screen.blit(result_text, (
        SCREEN_WIDTH // 2 - result_text.get_width() // 2, SCREEN_HEIGHT // 2 - result_text.get_height() // 2))
        retry_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 40)
        pygame.draw.rect(screen, (0, 255, 0), retry_button)
        retry_text = button_font.render("Попробуй еще раз", True, (255, 255, 255))
        screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50 + 10))

    pygame.display.update()

    if time_left <= 0:
        game_active = False

pygame.quit()