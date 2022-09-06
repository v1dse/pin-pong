import os
from turtle import screensize

screensize = (700,500)
# путь игрового материала
ROOTDIR = os.getcwd()
PLATFORM = [os.path.join(ROOTDIR, 'resources/image/platform.png')]
BALL = [os.path.join(ROOTDIR, 'resources/image/ball.png')]
GAME_BG_IMAGEPATH = os.path.join(ROOTDIR, 'resources/image/background.png')

BGM_SOUND = [os.path.join(ROOTDIR, 'resources/sound/ballandplatfom.mp3')]
FONT_PATH = os.path.join(ROOTDIR, 'resources/font/Gabriola.ttf')

HOLE_POSITIONS = [(90, 290), (720, 290)]
# устанавливаем цвета для текста внутри игры
BROWN = (150, 75, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
# директория для записи очков–
RECORD_PATH = 'score.rec'