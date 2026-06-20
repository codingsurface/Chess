from const import *
from draw import *
from move import *
class Main:
    run = True
    sq_selected = ()
    player_moves = []
    while run:
        #calling drawing functions
        draw_rect()
        draw_pieces()
        # check if it is the first square selected
        if len(player_moves) == 1:
            piece = Piece(player_moves[0],gs.board)
            if gs.whitetomove == True and gs.board[player_moves[0][0]][player_moves[0][1]][0] == 'w':
                piece.possible_moves()
                for move in piece.possible:
                    row, col = move[0],move[1]
                    p.draw.rect(screen,(255,0,0),p.Rect(col * SQ_size,row * SQ_size,SQ_size,SQ_size),3)
            elif gs.whitetomove == False and gs.board[player_moves[0][0]][player_moves[0][1]][0] == 'b':
                piece.possible_moves()
                for move in piece.possible:
                    row, col = move[0],move[1]
                    p.draw.rect(screen,(255,0,0),p.Rect(col * SQ_size,row * SQ_size,SQ_size,SQ_size),3)
            else:
                sq_selected = ()
                player_moves = []
        #checking if it is the second square selected
        elif len(player_moves) == 2:
            motion = Move(player_moves[0],player_moves[1],gs.board)
            if player_moves[1] in piece.possible:
                if gs.whitetomove == True and gs.board[player_moves[0][0]][player_moves[0][1]][0] == 'w':
                    move_uci = alpha_num[player_moves[0]] + alpha_num[player_moves[1]]
                    move = chess.Move.from_uci(move_uci)
                    if move in gs.board2.legal_moves:
                        gs.make_move(motion)
                        gs.board2.push(move)
                        sound_sfx.play()
                    sq_selected = ()
                    player_moves = []
                elif gs.whitetomove == False and gs.board[player_moves[0][0]][player_moves[0][1]][0] == 'b':
                    move_uci = alpha_num[player_moves[0]] + alpha_num[player_moves[1]]
                    move = chess.Move.from_uci(move_uci)
                    if move in gs.board2.legal_moves:
                        gs.board2.push(move)
                        print(gs.board2)
                        gs.make_move(motion)
                        sound_sfx.play()
                    sq_selected = ()
                    player_moves = []
                else:
                    sq_selected = ()
                    player_moves = []
            elif player_moves[1] not in piece.possible and gs.board[player_moves[1][0]][player_moves[1][1]] != '--':
                player_moves[0] = player_moves[1]
                player_moves.pop()
            else:
                player_moves.pop()
            if gs.board2.is_checkmate():
                if gs.whitetomove == True:
                    gs.black_wins = True
                else:
                    gs.white_wins = True
        #click event
        for e in p.event.get():
            if e.type == p.QUIT:
                run = False
            elif e.type == p.MOUSEBUTTONDOWN:
                location = p.mouse.get_pos()
                #sq_pos
                col = location[0] // SQ_size
                row = location[1] // SQ_size
                #checking if it is the same square
                if sq_selected == (row,col):
                    sq_selected = ()
                    player_moves = []
                #checking if square is empty and no piece is selected before it
                elif gs.board[row][col] == '--' and player_moves == []:
                    sq_selected = ()
                    player_moves == []
                else:
                    sq_selected = (row,col)
                    player_moves.append(sq_selected)
            #if the player clicked r and wining state redo everything
            if gs.white_wins or gs.black_wins:
                if e.type == p.KEYDOWN:
                    if e.key == p.K_r:
                        gs.board = [
                            ['bR','bN','bB','bQ','bK','bB','bN','bR'],
                            ['bP','bP','bP','bP','bP','bP','bP','bP'],
                            ['--','--','--','--','--','--','--','--'],
                            ['--','--','--','--','--','--','--','--'],
                            ['--','--','--','--','--','--','--','--'],
                            ['--','--','--','--','--','--','--','--'],
                            ['wP','wP','wP','wP','wP','wP','wP','wP'],
                            ['wR','wN','wB','wQ','wK','wB','wN','wR']
                        ]
                        gs.whitetomove = True
                        gs.white_wins = False
                        gs.black_wins = False
        #win message
        if gs.white_wins:
            panel = p.Surface((Width, Hieght), p.SRCALPHA)
            panel.fill((255, 255, 255))  # RGBA (last value is transparency)
            screen.blit(panel, (Width//2 - 240, Hieght//2 - 240))
            text = font.render("WHITE WINS ! press R to restart", True, (0,0,0))
            screen.blit(text, (Width//2-180, Width//2))
        if gs.black_wins:
            panel = p.Surface((Width, Hieght), p.SRCALPHA)
            panel.fill((0, 0, 0))  # RGBA (last value is transparency)

            screen.blit(panel, (Width//2 - 240, Hieght//2 - 240))
            text = font.render("Black WINS ! press R to restart", True, (255,255,255))
            screen.blit(text, (Width//2-180, Width//2))
        p.display.flip()
    p.quit()
Main()