import pygame
import math
import time


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
        self.papa = None
        self.Gpos = (None, None)


def insert(path, root, node):
    global f
    f = 1
    if root is None:
        root = node
        root.papa = None
        path.append(0)
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
                node.papa = root
                if len(path) >= 1:
                    path.append(int(200 / math.pow(2, len(path))))
                else:
                    path.append(200)

            else:
                if len(path) >= 1:
                    path.append(int(200 / math.pow(2, len(path))))
                else:
                    path.append(200)
                insert(path, root.right, node)

        else:
            if root.left is None:
                root.left = node
                node.papa = root
                if len(path) >= 1:
                    path.append(int(-200 / math.pow(2, len(path))))
                else:
                    path.append(-200)

            else:
                if len(path) >= 1:
                    path.append(int(-200 / math.pow(2, len(path))))
                else:
                    path.append(-200)

                insert(path, root.left, node)
    return path, root, node


def clear():
    global text
    global data
    global pointer
    global f
    global wait
    global c
    global path
    global important
    global root
    global node
    global last_f
    global done

    text = ""
    data = []
    pointer = -1
    f = 0
    wait = True
    c = 0
    path = []
    important = []
    root = None
    node = None
    last_f = False
    pygame.display.update()


""" VISVALISATIOn"""


"""       INITILIZATION       """
x = 0
pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
light_red = (155, 0, 0)
yellow = (255, 239, 0)
my_color = (255, 255, 115)
text = ""
data = []
pointer = -1
f = 0
wait = True
c = 0
path = []
important = []
last_f = False
pointer_update = False

"""          FONTS       """
outroFont = pygame.font.SysFont("trebuchetms", 36)
to_check = pygame.font.Font("freesansbold.ttf", 50)
mediumText = pygame.font.Font("freesansbold.ttf", 20)
LargeText = pygame.font.Font("freesansbold.ttf", 30)
SmallText = pygame.font.Font("freesansbold.ttf", 15)
moreSmallText = pygame.font.Font("freesansbold.ttf", 13)


"""         DISPLAY           """
gameDisplay = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("BINARY SEARCH TREE")
active = False
input_box = pygame.Rect(100, 30, 250, 40)
gameExit = False
introExit = False
outroExit = False
fps = 15
"""  TEXT OBJ CREATION """


def text_object(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


root = None
node = None
start_node = (500, 100)


"""       ALDREADY CREATED NODE    """


def already_present(important):
    for key, point in important:

        length = len(point) - 1

        key.Gpos = (start_node[0] + sum(point), start_node[1] + length * 100)

        if key.papa != None:
            pygame.draw.line(gameDisplay, yellow, key.papa.Gpos, key.Gpos, 1)

        pygame.draw.circle(
            gameDisplay,
            yellow,
            [start_node[0] + sum(point), start_node[1] + length * 100],
            20,
        )
        TextSurf_node, TextRect_node = text_object(str(key.val), mediumText, black)

        if len(str(key.val)) == 1:
            gameDisplay.blit(
                TextSurf_node,
                (start_node[0] - 6 + sum(point), start_node[1] - 10 + length * 100),
            )
        if len(str(key.val)) == 2:
            gameDisplay.blit(
                TextSurf_node,
                (start_node[0] - 10 + sum(point), start_node[1] - 10 + length * 100),
            )
        if len(str(key.val)) == 3:
            gameDisplay.blit(
                TextSurf_node,
                (start_node[0] - 16 + sum(point), start_node[1] - 10 + length * 100),
            )


"""           INTRO            """


i = 0
change = 0
retro = [(200, 0, 0), (100, 0, 100), (0, 0, 200), (0, 100, 100), (0, 200, 0)]
while not introExit:

    gameDisplay.fill(white)
    change = (change + 1) % 3

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                introExit = True

    TextSurf, TextRect = text_object("Press Space", mediumText, black)
    TextRect.center = (500, 200)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_object("B S T", to_check, retro[change])
    TextRect.center = (500, 350)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

"""          GAME LOOP               """


while not gameExit:
    change = (change + 1) % 3

    """        POSITION OF MOUSE AND STATUS OF CLICK          """

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    """ EVENT LOOP """

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                gameExit = True

            if event.key == pygame.K_c:
                clear()
            if active:

                """                TAKE INPUT          """

                if event.key == 8 or 265 >= event.key >= 256:
                    if event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
                        if len(text) == 4:
                            text = text[:-1]
                        if event.key == pygame.K_RETURN:
                            text = text[:-1]

    gameDisplay.fill(white)  # BACKGROUND COLOR

    """         ONLY WHENN HOVERING     """

    if 900 + 80 > mouse[0] > 900 and 30 + 40 > mouse[1] > 30:
        pygame.draw.rect(gameDisplay, light_red, (900, 30, 80, 40))

        """        WHEN PUSH     """

        if click[0] == 1 and text != "":
            data.append(int(text))
            f = 1
            wait = False
            walk = 0
            pushed = False
            lead_x = 0
    else:
        pygame.draw.rect(gameDisplay, red, (900, 30, 80, 40))

    if not active:
        TextSurf, TextRect = text_object("PROCESS NUMBER", moreSmallText, black)
        TextRect.center = (200, 20)
        gameDisplay.blit(TextSurf, TextRect)

    """         INPUT BOX      """

    TextSurf, TextRect = text_object("Press C to Clear", SmallText, retro[change])
    TextRect.center = (500, 10)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_object(
        "Press Q to Quit", SmallText, retro[(change + 1) % 3]
    )
    TextRect.center = (500, 30)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf_input, TextRect_input = text_object(text, LargeText, black)
    width = max(200, TextSurf_input.get_width() + 10)
    input_box.w = width
    gameDisplay.blit(TextSurf_input, (input_box.x + 5, input_box.y + 5))

    """          BUTTON         """

    TextSurf, TextRect = text_object("PUSH", mediumText, black)
    TextRect.center = ((900 + (80) / 2), (30 + (40) / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.draw.rect(gameDisplay, black, input_box, 8)

    """      PROGRAM LOGIC      """

    if wait == False:
        if root is None:
            path, root, node = insert([], root, Node(int(text)))
        else:
            path, root, node = insert([0], root, Node(int(text)))
        path = path[::-1]
        important.append([node, path])
        pointer += 1

        text = ""
        wait = True

    if pointer >= 0:
        if pushed:
            already_present(important)
        else:

            last_f = True
            already_present(important[:-1])
            key = important[pointer][0].val
            road = important[pointer][1][::-1]
            lead_y = walk * 100
            print(f"{start_node[0]+lead_x,start_node[1]+lead_y}")
            print(f"      {road}    ")
            pygame.draw.circle(
                gameDisplay, red, [start_node[0] + lead_x, start_node[1] + lead_y], 20
            )
            pygame.draw.line(
                gameDisplay,
                yellow,
                [start_node[0] + lead_x, start_node[1] + lead_y - 100],
                [start_node[0] + lead_x, start_node[1] + lead_y],
                1,
            )

            lead_x += road[walk]
            walk += 1

            if walk == len(road):
                pushed = True
                walk = 0

    pygame.time.Clock().tick(fps)
    pygame.display.update()
    if last_f == True:
        time.sleep(1)
    last_f = False


while not outroExit:

    gameDisplay.fill(white)
    change = (change + 1) % 3

    TextSurf, TextRect = text_object("OUTRODUCTION PRESS", SmallText, black)
    TextRect.center = (100, 25)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_object("ESC", SmallText, red)
    TextRect.center = (100, 50)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_object("|", SmallText, retro[(change) % 3])
    TextRect.center = (500, 200)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_object("|", LargeText, retro[(change + 1) % 3])
    TextRect.center = (500, 250)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_object("COOL!", mediumText, retro[(change + 2) % 3])
    TextRect.center = (500, 350)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_object("|", SmallText, retro[(change + 3) % 3])
    TextRect.center = (500, 450)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_object("|", LargeText, retro[(change + 4) % 3])
    TextRect.center = (500, 500)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_object("PranshuL KaushiK", SmallText, black)
    TextRect.center = (900, 670)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_object("SIGNING", SmallText, black)
    TextRect.center = (870, 690)
    gameDisplay.blit(TextSurf, TextRect)

    TextSurf, TextRect = text_object("OFF", SmallText, red)
    TextRect.center = (940, 690)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                outroExit = True

pygame.quit()
quit()
