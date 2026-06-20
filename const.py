import pygame as p
import chess
p.init()
Dimension = 8
Width = Hieght = 480
SQ_size = Hieght // 8
sound_sfx = p.mixer.Sound('chess/freesound_community-chess-pieces-60890.mp3')
class Game_Stats:
    def __init__(self):
        self.board = [['bR','bN','bB','bQ','bK','bB','bN','bR'],
                ['bP','bP','bP','bP','bP','bP','bP','bP'],
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['wP','wP','wP','wP','wP','wP','wP','wP'],
                ['wR','wN','wB','wQ','wK','wB','wN','wR']]
        self.whitetomove = True
        self.white_wins = False
        self.black_wins = False
        self.board2 = chess.Board()
    def make_move(self,move):
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.whitetomove = not self.whitetomove
gs = Game_Stats()
images = {}
pieces = ['bB','bK','bN','bP','bQ','bR','wB','wN','wK','wN','wP','wQ','wR']
for P in pieces:
    images[P] = p.image.load('chess/images/'+P+'.png')

alpha = ["a","b","c","d","e","f","g","h"]
num = []
for i in range(0,8):
    for j in range(0,8):
        num.append((i,j))
alpha_num = {
    (row, col): f"{alpha[col]}{8-row}"
    for row in range(8)
    for col in range(8)
}
print(alpha_num)
screen = p.display.set_mode([Width, Hieght])
font = p.font.Font('freesansbold.ttf', 20)
fps = 60
captured_pieces_White = []
captured_pieces_Black = []
track_move = []
distance = []