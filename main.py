import pygame
import random
import tkinter as tk


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
    if level == 2:
        target_speed_x = random.choice([-2, 2])  # Скорость движения мишени по X
        target_speed_y = random.choice([-2, 2])  # Скорость движения мишени по Y
    else:
        target_speed_x = 0.4
        target_speed_y = 0.3


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")

target_image = pygame.image.load("img/mishen.png")
target_width, target_height = 80, 80
color = (76, 81, 74)
font = pygame.font.Font(None, 36)
button_font = pygame.font.Font(None, 26)
level = 1

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

game_time = 10
reset_game()
target_speed_x = 0.5
target_speed_y = 0.5

running = True
while running:
    screen.fill(color)
    current_ticks = pygame.time.get_ticks()
    seconds_passed = (current_ticks - start_ticks) // 1000
    time_left = max(game_time - seconds_passed, 0)
    timer_text = font.render(f"Time Left: {time_left}s", True, (255, 255, 255))
    screen.blit(timer_text, (10, 10))

    if game_active:
        if game_active and level == 2:
            target_x += target_speed_x
            target_y += target_speed_y
            # Изменение направления при достижении границ экрана
            if target_x <= 0 or target_x >= SCREEN_WIDTH - target_width:
                target_speed_x *= -0.4
            if target_y <= 0 or target_y >= SCREEN_HEIGHT - target_height:
                target_speed_y *= -0.4
        screen.blit(target_image, (target_x, target_y))
        if time_left == 0:
            game_active = False
    else:
        result_text = font.render(f"Количество попаданий: {hits}", True, (255, 255, 255))
        screen.blit(result_text, (SCREEN_WIDTH // 2 - result_text.get_width() // 2, SCREEN_HEIGHT // 2 - 20))

        retry_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 50, 200, 40)
        pygame.draw.rect(screen, (0, 255, 0), retry_button)
        retry_text = button_font.render("Попробуй еще раз", True, (255, 255, 255))
        screen.blit(retry_text, retry_button.topleft + pygame.math.Vector2(10, 10))

        level2_button = pygame.Rect(SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 + 100, 200, 40)
        pygame.draw.rect(screen, (0, 0, 255),         level2_button)
        level2_text = button_font.render("Уровень 2", True, (255, 255, 255))
        screen.blit(level2_text, level2_button.topleft + pygame.math.Vector2(10, 10))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if game_active:
                if target_x <= mouse_x <= target_x + target_width and target_y <= mouse_y <= target_y + target_height:
                    hits += 1
                    target_x = random.randint(0, SCREEN_WIDTH - target_width)
                    target_y = random.randint(0, SCREEN_HEIGHT - target_height)
            elif retry_button.collidepoint(mouse_x, mouse_y):
                level = 1
                reset_game()
            elif level2_button.collidepoint(mouse_x, mouse_y) and not game_active:
                level = 2
                reset_game()

    pygame.display.update()

pygame.quit()

