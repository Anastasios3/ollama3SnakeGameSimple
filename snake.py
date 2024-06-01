import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)

dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


class snake_class:

    def __init__(self):
        self.length = 1
        self.dirc = 'right'
        self.position = [100, 50]
        self.body = [[100, 50]]

    def get_head(self):
        return self.position

    def get_body(self):
        return self.body

    def set_dirc(self, direction):
        if direction == 'up' and self.dirc != 'down':
            self.dirc = direction
        elif direction == 'down' and self.dirc != 'up':
            self.dirc = direction
        elif direction == 'right' and self.dirc != 'left':
            self.dirc = direction
        elif direction == 'left' and self.dirc != 'right':
            self.dirc = direction

    def move(self):
        if self.dirc == 'up':
            new_head = [self.position[0], self.position[1] - snake_block]
        elif self.dirc == 'down':
            new_head = [self.position[0], self.position[1] + snake_block]
        elif self.dirc == 'right':
            new_head = [self.position[0] + snake_block, self.position[1]]
        elif self.dirc == 'left':
            new_head = [self.position[0] - snake_block, self.position[1]]

        self.body.insert(0, list(new_head))
        self.position = new_head

        if len(self.body) > self.length:
            self.body.pop()

    def grow(self):
        self.length += 1

    def check_collision(self):
        head = self.body[0]
        if head[0] < 0 or head[0] >= dis_width or \
           head[1] < 0 or head[1] >= dis_height:
            return True
        for segment in self.body[1:]:
            if head == segment:
                return True
        return False


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def main():
    game_over = False
    game_close = False

    snake = snake_class()
    food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
    food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

    while not game_over:

        while game_close:
            dis.fill(black)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                    game_close = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.set_dirc('up')
                elif event.key == pygame.K_DOWN:
                    snake.set_dirc('down')
                elif event.key == pygame.K_LEFT:
                    snake.set_dirc('left')
                elif event.key == pygame.K_RIGHT:
                    snake.set_dirc('right')

        snake.move()

        if snake.check_collision():
            game_close = True

        if snake.get_head() == [food_x, food_y]:
            snake.grow()
            food_x = round(random.randrange(0, dis_width - snake_block) / snake_block) * snake_block
            food_y = round(random.randrange(0, dis_height - snake_block) / snake_block) * snake_block

        dis.fill(black)

        for segment in snake.body:
            pygame.draw.rect(dis, yellow, [segment[0], segment[1], snake_block, snake_block])

        pygame.draw.rect(dis, white, [food_x, food_y, snake_block, snake_block])

        score = snake.length - 1
        screen_text = score_font.render('Score: ' + str(score), True, white)
        dis.blit(screen_text, [10, 5])

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
