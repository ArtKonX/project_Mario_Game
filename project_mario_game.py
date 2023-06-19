import pygame as pg


pg.init()

W = 600
H = 400

pg.mouse.set_visible(False)
sc = pg.display.set_mode((W, H))
pg.display.set_caption("SuperMario")
pg.display.set_icon(pg.image.load("files/mario.png"))
sky_mario = pg.image.load("files/sky.png")
ground = pg.image.load("files/ground.jpg")
pg.display.update()

WHITE = (255, 255, 255)
BLUE = (40, 123, 241)
GREEN = (178, 255, 102)
RED = (255, 0, 0)

level = 1

sound_jump = pg.mixer.Sound("files/sound_jump.mp3")

FPS = 60

clock = pg.time.Clock()
ground_mario = H - 98
jump_height = 25
move = jump_height + 2

RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
JUMP = "up"
motion = STOP

l = True
r = True

count_jump = 0
count_flattening = 0

side = 60
direction = RIGHT

size_style = pg.font.SysFont('arial', 25)
name_game = size_style.render('SUPER MARIO', 1, RED)
text_position = name_game.get_rect(topleft=(0, 0))

pg.mixer.music.load("files/super-mario-saundtrek.mp3")
pg.mixer.music.play(-1)

list_mario_position_right = []
first_elem_mario_position_right = pg.image.load("files/Stay_Right.png").convert_alpha()
first_elem_mario_position_right = pg.transform.scale(first_elem_mario_position_right, (60, 90))
list_mario_position_right.append(first_elem_mario_position_right)
second_elem_mario_position_right = pg.image.load("files/Wolk_Right.png").convert_alpha()
second_elem_mario_position_right = pg.transform.scale(second_elem_mario_position_right, (60, 90))
list_mario_position_right.append(second_elem_mario_position_right)
third_elem_mario_position_right = pg.image.load("files/Run_Right.png").convert_alpha()
third_elem_mario_position_right = pg.transform.scale(third_elem_mario_position_right, (60, 90))
list_mario_position_right.append(third_elem_mario_position_right)

list_mario_position_left = []
first_elem_mario_position_left = pg.image.load("files/Stay_Left.png").convert_alpha()
first_elem_mario_position_left = pg.transform.scale(first_elem_mario_position_left, (60, 90))
list_mario_position_left.append(first_elem_mario_position_left)
second_elem_mario_position_left = pg.image.load("files/Wolk_Left.png").convert_alpha()
second_elem_mario_position_left = pg.transform.scale(second_elem_mario_position_left, (60, 90))
list_mario_position_left.append(second_elem_mario_position_left)
third_elem_mario_position_left = pg.image.load("files/Run_Left.png").convert_alpha()
third_elem_mario_position_left = pg.transform.scale(third_elem_mario_position_left, (60, 90))
list_mario_position_left.append(third_elem_mario_position_left)

mario_stay_right = pg.image.load("files/Stay_Right.png").convert_alpha()
mario_stay_right = pg.transform.scale(mario_stay_right, (60, 90))

mario_stay_left = pg.image.load("files/Stay_Left.png").convert_alpha()
mario_stay_left = pg.transform.scale(mario_stay_left, (60, 90))

mario_jump_right = pg.image.load("files/Jump_Right.png").convert_alpha()
mario_jump_right = pg.transform.scale(mario_jump_right, (60, 90))

mario_jump_left = pg.image.load("files/Jump_Left.png").convert_alpha()
mario_jump_left = pg.transform.scale(mario_jump_left, (60, 90))

rect_mario = list_mario_position_right[0].get_rect(center=(W // 2, H // 2))

rect_mario.bottom = ground_mario

list_gumba = []
first_elem_gumba_position_right = pg.image.load("files/Gumba_Right.png").convert_alpha()
first_elem_gumba_position_right = pg.transform.scale(first_elem_gumba_position_right, (60, 60))
list_gumba.append(first_elem_gumba_position_right)
second_elem_gumba_position_left= pg.image.load("files/Gumba_Left.png").convert_alpha()
second_elem_gumba_position_left = pg.transform.scale(second_elem_gumba_position_left, (60, 60))
list_gumba.append(second_elem_gumba_position_left)

rect_gumba = list_gumba[0].get_rect(center=(W + 0, H - 130))

rect_gumba_two = list_gumba[0].get_rect(center=(W + 500, H - 130))

class Mario:

    def __init__(self, list_mario_left, list_mario_right, mario_stay_left, mario_stay_right, mario_jump_left, mario_jump_right, rect_mario):
        self.list_mario_left = list_mario_left
        self.list_mario_right = list_mario_right
        self.mario_stay_left = mario_stay_left
        self.mario_stay_right = mario_stay_right
        self.mario_jump_left = mario_jump_left
        self.mario_jump_right = mario_jump_right
        self.rect_mario = rect_mario
        self.img_counter = 0

    def mario_walk_left(self):
        if self.img_counter == 15:
            self.img_counter = 0
        sc.blit(self.list_mario_left[self.img_counter // 5], self.rect_mario)
        self.img_counter += 1

    def mario_walk_right(self):
        if self.img_counter == 15:
            self.img_counter = 0
        sc.blit(self.list_mario_right[self.img_counter // 5], self.rect_mario)
        self.img_counter += 1

    def mario_stay_left_(self):
        sc.blit(self.mario_stay_left, self.rect_mario)

    def mario_stay_right_(self):
        sc.blit(self.mario_stay_right, self.rect_mario)

    def mario_jump_left_(self):
        sc.blit(self.mario_jump_left, self.rect_mario)

    def mario_jump_right_(self):
        sc.blit(self.mario_jump_right, self.rect_mario)

class Gumba:

    def __init__(self, list_gumba, rect_gumba_first, rect_gumba_second):
        self.list_gumba = list_gumba
        self.rect_gumba_first = rect_gumba_first
        self.rect_gumba_second = rect_gumba_second
        self.img_counter = 0
        self.count = 0

    def first_gumba_walk(self):
        if self.img_counter == 18:
            self.img_counter = 0
        sc.blit(self.list_gumba[self.img_counter // 9], self.rect_gumba_first)
        self.img_counter += 1

    def first_gumba_animation(self):
        global direction
        if self.rect_gumba_first.x + side >= W:
            direction = LEFT
        elif self.rect_gumba_first.x <= 0:
            direction = RIGHT
        if direction == RIGHT:
            self.rect_gumba_first.x += 3
        else:
            self.rect_gumba_first.x -= 3

    def second_gumba_walk(self):
        if self.img_counter == 18:
            self.img_counter = 0
        sc.blit(self.list_gumba[self.img_counter // 9], self.rect_gumba_second)
        self.img_counter += 1

    def second_gumba_animation(self):
        global direction
        if self.rect_gumba_second.x + side >= W:
            direction = LEFT
        elif self.rect_gumba_second.x <= 0:
            direction = RIGHT
        if direction == RIGHT:
            self.rect_gumba_second.x += 3
        else:
            self.rect_gumba_second.x -= 3

    @staticmethod
    def first_gumba_moving():
        global count_flattening
        if rect_gumba.collidepoint(rect_mario.midbottom):
            rect_gumba.x = W
            count_flattening += 1

    @staticmethod
    def second_gumba_moving():
        global count_flattening
        if rect_gumba_two.collidepoint(rect_mario.midbottom):
            rect_gumba_two.x = W
            count_flattening += 1

mr = Mario(list_mario_position_left, list_mario_position_right, mario_stay_left, mario_stay_right, mario_jump_left, mario_jump_right, rect_mario)

gb = Gumba(list_gumba, rect_gumba, rect_gumba_two)

while True:

    keys = pg.key.get_pressed()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE and ground_mario == rect_mario.bottom:
                motion = JUMP
                move = -jump_height
                sound_jump.play()
                count_jump += 1
            if event.key == pg.K_z:
                if motion == LEFT:
                    rect_mario.x -= 20
                if motion == RIGHT:
                    rect_mario.x += 20
            if event.key == pg.K_LEFT:
                motion = LEFT
                rect_mario.x -= 5
                l = True
                r = False
            if event.key == pg.K_RIGHT:
                motion = RIGHT
                rect_mario.x += 5
                l = False
                r = True
        elif event.type == pg.KEYUP:
            if event.key in [pg.K_LEFT,
                             pg.K_RIGHT, pg.K_z]:
                motion = STOP

    if keys[pg.K_z]:
        if motion == LEFT:
            rect_mario.x -= 8
        if motion == RIGHT:
            rect_mario.x += 8

    if keys[pg.K_LEFT]:
        if motion == JUMP:
            if rect_mario.x <= -80:
                rect_mario.x = W - rect_mario.x - 80
            else:
                rect_mario.x -= 5

    if keys[pg.K_RIGHT]:
        if motion == JUMP:
            if rect_mario.x >= W:
                rect_mario.x = rect_mario.x - W - 80
            else:
                rect_mario.x += 5

    if move <= jump_height:
        motion == JUMP
        if rect_mario.bottom + move < ground_mario:
            rect_mario.bottom += move
            if move < jump_height:
                move += 2
        else:
            rect_mario.bottom = ground_mario
            move = jump_height + 2

    if motion == LEFT:
        if rect_mario.x <= -80:
            rect_mario.x = W - rect_mario.x - 80
        else:
            rect_mario.x -= 5

    if motion == RIGHT:
        if rect_mario.x >= W:
            rect_mario.x = rect_mario.x - W - 80
        else:
            rect_mario.x += 5

    sc.fill(BLUE)
    sc.blit(sky_mario, (0, -180))
    sc.blit(ground, (0, 300))
    sc.blit(name_game, text_position)

    if motion == STOP:
        if l:
            mr.mario_stay_left_()
            r = False
        elif r:
            mr.mario_stay_right_()
            l = False
    elif motion == LEFT:
        mr.mario_walk_left()
    elif motion == RIGHT:
        mr.mario_walk_right()
    elif motion == JUMP and rect_mario.bottom != ground_mario + 1:
        if rect_mario.bottom == ground_mario:
            if l:
                mr.mario_walk_left()
                r = False
            elif r:
                mr.mario_walk_right()
                l = False
        else:
            if l:
                mr.mario_jump_left_()
                r = False
            elif r:
                mr.mario_jump_right_()
                l = False

    if count_flattening >= 10:
        gb.second_gumba_walk()
        gb.second_gumba_animation()
        if level < 2:
            level += 1
    else:
        level += 0

    title_jump = size_style.render(f'Количество прыжков {count_jump}', 1, WHITE)
    position_title_jump = title_jump.get_rect(topleft=(180, 350))
    sc.blit(title_jump, position_title_jump)

    title_flattened = size_style.render(f'Количество Расплющенных Грибков {count_flattening}', 1, WHITE)
    position_title_flattened = title_flattened.get_rect(center=(290, 70))
    sc.blit(title_flattened, position_title_flattened)

    title_level = size_style.render(f'Уровень {level}', 1, RED)
    position_title_level = title_level.get_rect(center=(300, 150))
    sc.blit(title_level, position_title_level)

    gb.first_gumba_walk()
    gb.first_gumba_animation()
    Gumba.first_gumba_moving()
    Gumba.second_gumba_moving()

    if count_flattening >= 25:
        sc.fill(BLUE)
        win_game_title = size_style.render(f'Вы прошли игру! Поздравляем!', 1, RED)
        position_win_game_title = title_jump.get_rect(center=(250, H // 2))
        sc.blit(win_game_title, position_win_game_title)

    pg.display.update()

    clock.tick(FPS)
