from const import *
class Move:
    def __init__(self,start_sq,end_sq,board):
        self.startRow = start_sq[0]
        self.startCol = start_sq[1]
        self.endRow = end_sq[0]
        self.endCol = end_sq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]

class Piece:
    def __init__(self,start_sq,board):
            self.startRow = start_sq[0]
            self.startCol = start_sq[1]
            self.pieceMoved = board[self.startRow][self.startCol]
            self.board = board
            self.possible = set()
    def possible_moves(self):
        #white pawn        
        if self.pieceMoved == 'wP':
            #one square forward
            if self.board[self.startRow - 1][self.startCol] == '--':
                self.possible.add((self.startRow - 1, self.startCol))
                # two squares forward from starting position
                if self.startRow == 6 and self.board[self.startRow - 2][self.startCol] == '--':
                    self.possible.add((self.startRow - 2, self.startCol))
            # capture right
            if self.startCol < 7:
                target = self.board[self.startRow - 1][self.startCol + 1]
                if target != '--' and target[0] == 'b':
                    self.possible.add((self.startRow - 1, self.startCol + 1))
            # capture left
            if self.startCol > 0:
                target = self.board[self.startRow - 1][self.startCol - 1]

                if target != '--' and target[0] == 'b':
                    self.possible.add((self.startRow - 1, self.startCol - 1))
        #black pawn
        if self.pieceMoved == 'bP':
             #one square forward
            if self.board[self.startRow + 1][self.startCol] == '--':
                self.possible.add((self.startRow + 1, self.startCol))
                # two squares forward from starting position
                if self.startRow == 1 and self.board[self.startRow + 2][self.startCol] == '--':
                        self.possible.add((self.startRow + 2, self.startCol))
             # capture right
            if self.startCol < 7:
                target = self.board[self.startRow + 1][self.startCol + 1]
                if target != '--' and target[0] == 'w':
                    self.possible.add((self.startRow + 1, self.startCol + 1))
            # capture left
            if self.startCol > 0:
                target = self.board[self.startRow+1][self.startCol-1]
                if target != '--' and target[0] == 'w':
                    self.possible.add((self.startRow+1,self.startCol-1))
        #Night
        if self.pieceMoved[1] == 'N':
            directions = [(2,1),(2,-1),(-2,-1),(-2,1),(1,2),(-1,2),(1,-2),(-1,-2)]
            for dr,dc in directions:
                r,c = self.startRow+dr, self.startCol+dc
                if 0<=r<8 and 0<=c<8:
                    if self.board[r][c] == '--':
                        self.possible.add((r,c))
                    elif self.pieceMoved[0] != self.board[r][c][0]:
                        self.possible.add((r,c))
        #Rook
        if self.pieceMoved[1] == 'R':
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            for dr,dc in directions:
                row = self.startRow + dr
                col = self.startCol + dc
                while 0 <= row<8 and 0<= col<8:
                    if self.board[row][col] == '--':
                        self.possible.add((row,col))
                    elif self.pieceMoved[0] != self.board[r][c][0]:
                        self.possible.add((row,col))
                        break
                    else:
                        break
                    row += dr
                    col += dc
        #Bishop
        if self.pieceMoved[1] == 'B':
            directions = [(-1,-1),(-1,1),(1,-1),(1,1)]
            for dr,dc in directions:
                r,c = self.startRow+dr , self.startCol+dc
                while 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r][c] == '--':
                        self.possible.add((r,c))
                    elif self.pieceMoved[0] != self.board[r][c][0]:
                        self.possible.add((r,c))
                        break
                    else:
                        break
                    r += dr
                    c += dc
        #Queen
        if self.pieceMoved[1] == 'Q':
            directions2 = [(-1,-1),(-1,1),(1,-1),(1,1),(1,0),(0,1),(-1,0),(0,-1)]
            for dr,dc in directions2:
                r,c = self.startRow+dr , self.startCol+dc
                while 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r][c] == '--':
                        self.possible.add((r,c))
                    elif self.pieceMoved[0] != self.board[r][c][0]:
                        self.possible.add((r,c))
                        break
                    else:
                        break
                    r += dr
                    c += dc
        #the King
        if self.pieceMoved[1] == 'K':
            directions = [(-1,-1),(-1,1),(1,-1),(1,1),(1,0),(0,1),(-1,0),(0,-1)]
            for dr,dc in directions:
                r, c = self.startRow+dr ,self.startCol+dc
                if 0 <= r < 8 and 0 <= c < 8:
                    if self.board[r][c] == '--':
                        self.possible.add((r,c))
                    elif self.pieceMoved[0] != self.board[r][c][0]:
                        self.possible.add((r,c))