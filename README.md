# Chess
Hello This chess game is built in Python I Hope you Like it :
_initializing the game_const.py:

  before we start we have to declare some variables:
  like Dimensions, Width & Hieght, SQ_size, sound_sfx, images, alpha_num, screen, font, fps:
  
  import pygame as p 
  import chess
  p.init() #initializing pygame
  Dimension = 8
  Width = Hieght = 480
  SQ_size = Hieght // 8
  sound_sfx = p.mixer.Sound('freesound_community-chess-pieces-60890.mp3') #sound of moving pieces
  images = {} # images dictionary that will hold the name of pieces and attribute them to the function of loading images
  
  pieces = ['bB','bK','bN','bP','bQ','bR','wB','wN','wK','wN','wP','wQ','wR'] #names list of pieces
  for P in pieces:
      images[P] = p.image.load('images/'+P+'.png') #attributing piece name to the function of dowloading it's image
      
alpha = ["a","b","c","d","e","f","g","h"] #lettres of chess board
num = [] # cordinates list of board squares 
for i in range(0,8):
    for j in range(0,8):
        num.append((i,j)) 
alpha_num = {
    (row, col): f"{alpha[col]}{8-row}"
    for row in range(8)
    for col in range(8)
} # filling the alpha_num with the association of board cordinates to the real chess board cordinates
screen = p.display.set_mode([Width, Hieght]) #pygame screen
font = p.font.Font('freesansbold.ttf', 20) # font of the text
fps = 60 #frame rate
#one important thing is the initial game state wich we made a specific class to it
class Game_Stats:
    def __init__(self):
        self.board = [['bR','bN','bB','bQ','bK','bB','bN','bR'],
                ['bP','bP','bP','bP','bP','bP','bP','bP'],
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['--','--','--','--','--','--','--','--'],
                ['wP','wP','wP','wP','wP','wP','wP','wP'],
                ['wR','wN','wB','wQ','wK','wB','wN','wR']] # the full board
        self.whitetomove = True # first piece to move is white piece
        self.white_wins = False # none of white or black have wined yet
        self.black_wins = False
        self.board2 = chess.Board() # this is a second board for validating moves in chekmate state
    def make_move(self,move): #this is a function of making moves in the board the move parameter is a class that we will creat later
        self.board[move.startRow][move.startCol] = '--'
        self.board[move.endRow][move.endCol] = move.pieceMoved
        self.whitetomove = not self.whitetomove
gs = Game_Stats()
