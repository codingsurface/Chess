from const import *
def draw_rect():
    for r in range(Dimension):
        for c in range(Dimension):
            colors = [(74, 155, 255),(255, 255, 255)]
            p.draw.rect(screen,colors[(r+c)%2],p.Rect(c*SQ_size,r*SQ_size,SQ_size,SQ_size))
def draw_pieces():
    for r in range(Dimension):
        for c in range(Dimension):
            piece = gs.board[r][c]
            if piece != '--':
                screen.blit(images[piece],p.Rect(c*SQ_size,r*SQ_size,SQ_size,SQ_size))
