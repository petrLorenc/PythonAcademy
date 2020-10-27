import pygame, os


class Piece(object):
    def __init__(self, x: int, y: int, side: str):
        self.x = x
        self.y = y
        self.side = side
        self.moved = False

    def possible_moves(self):
        result = poss_moves(self.x, self.y, self.side, self.one_step, self.name)
        return result


class Pawn(Piece):
    def __str__(self):
        return ' ' + str(letters[self.x]) + str(8 - self.y) + ' '

    worth = 1

    def draw(self, win: object):
        if self.side == 'w':
            picture = pygame.image.load(os.path.join(image_dir, 'w_pawn_png_128px.png'))
        else:
            picture = pygame.image.load(os.path.join(image_dir, 'b_pawn_png_128px.png'))
        picture = pygame.transform.scale(picture, (53, 64))
        win.blit(picture, (square_size * self.x + 13, square_size * self.y + 8))

    def possible_moves(self):
        side = -1 if self.side == 'w' else 1
        result = []
        # possible_steps [[0,1 * side]]
        # if not self.moved: possible_steps.append([0,2*side])

        take_moves = [[self.x + 1, self.y + 1 * side, 'take'], [self.x - 1, self.y + 1 * side, 'take']]
        if is_on_board(self.x, self.y + 1 * side):
            if not board[self.y + 1 * side][self.x]:
                result.append([self.x, self.y + 1 * side, 'free'])
        if not self.moved:
            if not board[self.y + 2 * side][self.x] and not board[self.y + 1 * side][self.x]:
                result.append([self.x, self.y + 2 * side, 'free'])
        for move in take_moves:
            if is_on_board(move[0], move[1]):
                if board[move[1]][move[0]]:
                    result.append(move)

        return result


class Rook(Piece):
    name = 'rook'
    one_step = 0

    def __str__(self):
        return self.side + ' ' + 'R' + ' '

    worth = 5

    def draw(self, win):
        if self.side == 'w':
            picture = pygame.image.load(os.path.join(image_dir, 'w_rook_png_128px.png'))
        else:
            picture = pygame.image.load(os.path.join(image_dir, 'b_rook_png_128px.png'))
        picture = pygame.transform.scale(picture, (58, 64))
        win.blit(picture, (square_size * self.x + 11, square_size * self.y + 8))


class Knight(Piece):
    name = 'knight'
    one_step = 1

    def __str__(self):
        return self.side + ' ' + 'N' + ' '

    worth = 3

    def draw(self, win):
        if self.side == 'w':
            picture = pygame.image.load(os.path.join(image_dir, 'w_knight_png_128px.png'))
        else:
            picture = pygame.image.load(os.path.join(image_dir, 'b_knight_png_128px.png'))
        picture = pygame.transform.scale(picture, (58, 64))
        win.blit(picture, (square_size * self.x + 11, square_size * self.y + 8))


class Bishop(Piece):
    name = 'bishop'
    one_step = 0

    def __str__(self):
        return self.side + ' ' + 'B' + ' '

    worth = 3

    def draw(self, win):
        if self.side == 'w':
            picture = pygame.image.load(os.path.join(image_dir, 'w_bishop_png_128px.png'))
        else:
            picture = pygame.image.load(os.path.join(image_dir, 'b_bishop_png_128px.png'))
        picture = pygame.transform.scale(picture, (64, 64))
        win.blit(picture, (square_size * self.x + 8, square_size * self.y + 8))


class Queen(Piece):
    name = 'queen'
    one_step = 0

    def __str__(self):
        return self.side + ' ' + 'Q' + ' '

    worth = 10

    def draw(self, win):
        if self.side == 'w':
            picture = pygame.image.load(os.path.join(image_dir, 'w_queen_png_128px.png'))
        else:
            picture = pygame.image.load(os.path.join(image_dir, 'b_queen_png_128px.png'))
        picture = pygame.transform.scale(picture, (70, 64))
        win.blit(picture, (square_size * self.x + 5, square_size * self.y + 8))


class King(Piece):
    name = 'queen'
    one_step = 1

    def __str__(self):
        return self.side + ' ' + 'K' + ' '

    def draw(self, win):
        if self.side == 'w':
            picture = pygame.image.load(os.path.join(image_dir, 'w_king_png_128px.png'))
        else:
            picture = pygame.image.load(os.path.join(image_dir, 'b_king_png_128px.png'))
        picture = pygame.transform.scale(picture, (64, 64))
        win.blit(picture, (square_size * self.x + 8, square_size * self.y + 8))