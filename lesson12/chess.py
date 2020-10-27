import os, pygame
from lesson12.chess.figurky import *

pygame.init()
square_size = 80
board_size = 8
win_size = square_size * board_size
win = pygame.display.set_mode((win_size, win_size + 40))
pygame.display.set_caption('Chess by Mates')
counter_font = pygame.font.SysFont('arial', 20, True)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  # not really in use - just for terminal view
board = []
cwd = os.path.dirname(__file__)
image_dir = os.path.join(cwd, 'pieces')

pressed_key = False
pos_counter = 0  # Tracking of position cursor
run = True
score = [0, 0]
move_counter = 1
sides = ['b', 'w']



class My_cursor(object):
    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.selected = False
        self.kind = kind

    def draw(self, win):
        if self.kind == 'main':
            if self.selected:
                color = (0, 255, 0)
            else:
                color = (255, 0, 0)
        else:
            color = (255, 255, 0)
        position = (self.x * square_size + 2, self.y * square_size + 2, square_size - 6, square_size - 6)
        pygame.draw.rect(win, color, position, 2)


def draw_board(board_size: int, win: object):
    count = 1
    for y in range(board_size):
        for x in range(board_size):
            if count % 2:
                color = (200, 200, 200)
            else:
                color = (55, 55, 55)
            pygame.draw.rect(win, color, (x * square_size, y * square_size, square_size, square_size))
            count += 1
        count += 1


# Create an empty list in proper size
def create_board(board_size: int):
    global board
    for _i in range(board_size):
        line = []
        for _j in range(board_size):
            line.append('')
        board.append(line)


# Fill the board with pieces according to normal chess rules
def fill_with_pieces(board: list):
    side = 'b'
    global white_pieces, black_pieces
    piece_list = black_pieces
    for i in [0, 1, 6, 7]:
        if i == 6:
            side = 'w'
            piece_list = white_pieces
        if i in [1, 6]:
            for j in range(8):
                board[i][j] = Pawn(j, i, side)
        if i in [0, 7]:
            board[i][0], board[i][7] = Rook(0, i, side), Rook(7, i, side)
            board[i][1], board[i][6] = Knight(1, i, side), Knight(6, i, side)
            board[i][2], board[i][5] = Bishop(2, i, side), Bishop(5, i, side)
            board[i][3] = Queen(3, i, side)
            board[i][4] = King(4, i, side)
        for cell in board[i]:
            piece_list.append(cell)


# Checking if the move is possible and what type of move it is (not very good name for it though)
def line_move(x: int, y: int, side: str):
    if not is_on_board(x, y):
        return False, False

    if board[y][x]:
        if board[y][x].side == side:
            return False, False
        else:
            return [x, y, 'take'], False
    else:
        return [x, y, 'free'], True


def is_on_board(x: int, y: int) -> bool:
    if x >= 8 or y >= 8: return False
    if x < 0 or y < 0: return False
    return True





def is_check():
    global white_king, black_king, move_counter, white_pieces, black_pieces
    king = white_king if sides[move_counter % 2] == 'w' else black_king
    piece_list = white_pieces if sides[(move_counter + 1) % 2] == 'w' else black_pieces
    print(king)
    print(piece_list[0].side)

    for piece in piece_list:
        all_moves = piece.possible_moves()
        for move in all_moves:
            if move[2] == 'take':
                if move[0] == king.x and move[1] == king.y:
                    return True
    return False


# print board in terminal (not in use anymore)
def print_board(board):
    template_lst = ['']
    for _cell in board:
        template_lst.append('{}')
    template_lst.append('')
    template = '|'.join(template_lst)
    print('-' * len(board) * 5)
    for line in board:
        print(template.format(*line))
        print('-' * len(board) * 5)


def piece_move():
    global move_counter
    if cursor.x != pos_cursor.x or cursor.y != pos_cursor.y:
        if board[pos_cursor.y][pos_cursor.x]:
            score[move_counter % 2] += board[pos_cursor.y][pos_cursor.x].worth
            deleted_obj = board[pos_cursor.y][pos_cursor.x]
            board[pos_cursor.y][pos_cursor.x] = ''
            del deleted_obj
        board[cursor.y][cursor.x].moved = True
        board[pos_cursor.y][pos_cursor.x] = board[cursor.y][cursor.x]
        board[cursor.y][cursor.x].x = pos_cursor.x
        board[cursor.y][cursor.x].y = pos_cursor.y
        board[cursor.y][cursor.x] = ''
        move_counter += 1
        if is_check():
            print('this is a check')


def redraw_window(board_size, board, win):
    win.fill((0, 0, 0))
    draw_board(board_size, win)
    cursor.draw(win)
    for line in board:
        for square in line:
            try:
                square.draw(win)
            except:
                pass
    # possible moves
    if cursor.selected:
        poss_mov = board[cursor.y][cursor.x].possible_moves()
        for move in poss_mov:
            color = (0, 255, 255) if move[2] == 'free' else (255, 0, 0)
            position = (move[0] * square_size + 2, move[1] * square_size + 2, square_size - 6, square_size - 6)
            pygame.draw.rect(win, color, position, 2)
        try:
            pos_cursor.draw(win)
        except:
            pass

    move_text = counter_font.render('Move: ' + str(move_counter), 1, (255, 255, 255))
    score_text = counter_font.render('Score: ' + str(score[1]) + ' | ' + str(score[0]), 1, (255, 255, 255))
    win.blit(move_text, (10, win_size + 10))
    win.blit(score_text, (win_size // 2, win_size + 10))
    pygame.display.update()


create_board(8)
white_pieces, black_pieces = [], []
fill_with_pieces(board)
# fill_with_pieces(board)
cursor = My_cursor(5, 3, 'main')

# board[2][2] = rook(2,2,'w')
# board[3][5] = bishop(5,3,'w')
# board[1][3] = ''

redraw_window(board_size, board, win)
white_king = board[7][4]
black_king = board[0][4]
while run:

    keys = pygame.key.get_pressed()
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Cursor movement
    if not cursor.selected:
        if keys[pygame.K_RIGHT]:
            pressed_key = True
            if cursor.x < board_size - 1:
                cursor.x += 1
        if keys[pygame.K_LEFT]:
            pressed_key = True
            if cursor.x > 0:
                cursor.x -= 1
        if keys[pygame.K_UP]:
            pressed_key = True
            if cursor.y > 0:
                cursor.y -= 1
        if keys[pygame.K_DOWN]:
            pressed_key = True
            if cursor.y < board_size - 1:
                cursor.y += 1
    else:  # movement when selected
        if keys[pygame.K_RIGHT]:
            pressed_key = True
            pos_counter += 1
        if keys[pygame.K_LEFT]:
            pressed_key = True
            pos_counter -= 1
        if pressed_key:
            pos_cursor.x = poss_mov[pos_counter % len(poss_mov)][0]
            pos_cursor.y = poss_mov[pos_counter % len(poss_mov)][1]

    if board[cursor.y][cursor.x]:
        if board[cursor.y][cursor.x].side == sides[move_counter % 2]:
            if keys[pygame.K_KP_ENTER] or keys[pygame.K_SPACE] or keys[pygame.K_RETURN]:
                pressed_key = True
                if cursor.selected:
                    piece_move()
                    cursor.selected = False
                    pos_counter = 0
                    del pos_cursor
                else:
                    cursor.selected = True
                    poss_mov = board[cursor.y][cursor.x].possible_moves()
                    poss_mov.insert(0, [cursor.x, cursor.y, 'possition'])
                    pos_cursor = My_cursor(cursor.x, cursor.y, 'possition')
    if pressed_key:
        redraw_window(board_size, board, win)
        pressed_key = False

pygame.quit()