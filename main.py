

import pygame, sys
from stack import *
import copy

VECTOR = pygame.math.Vector2
WIDTH, HEIGHT = 300, 300
ICONS = ['x', 'o']
end = False
win = None

class Window():
    def __init__(self, width, height):

        pygame.init()

        self.screen = pygame.display.set_mode([WIDTH, HEIGHT])
        self.clock = pygame.time.Clock()

        pygame.display.set_caption("Example Use of a Stack")

    def draw_board(self, board):
        for row in range(3):
            for col in range(3):

                rect = pygame.Rect(row*100, col*100, 100, 100)

                pygame.draw.rect(self.screen, (255, 255, 255), rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

                self.draw_contents(board)

    def draw_contents(self, board):
        for row in range(3):
            for col in range(3):

                if board[row][col] == 'x':

                    self.draw_x(VECTOR(col*100, row*100))

                elif board[row][col] == 'o':
                    self.draw_o(VECTOR(col*100, row*100))

    def draw_x(self, pos):

        start = pos
        end2 = VECTOR (start.x+100, start.y + 100)

        pygame.draw.line(self.screen, (255, 0, 0), start+VECTOR(10, 10), end2 - VECTOR(10, 10), 10)
        start = start + VECTOR(100, 0)
        end2 = end2 - VECTOR(100, 0)
        pygame.draw.line(self.screen, (255, 0, 0), start + VECTOR(-10, 10), end2 + VECTOR(10, -10), 10)

    def draw_o(self, pos):
        pygame.draw.circle(self.screen, (0,255,0), pos + VECTOR(50, 50), 45, 10)

class Game:

    def initialise_board(self):
        for x in range(3):
            self.board.append(['-']*3)
    
    def __init__(self,):

        self.window = Window(HEIGHT, WIDTH)
        self.active = True
        self.icon = 0
        self.board = []
        self.move = False
        self.move_pos = None
        self.stack = Stack(10)
        self.undo = False
        self.initialise_board()

    def update_board(self, row, col):

        self.board[row][col] = ICONS[self.icon]



    def event_listener(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.active = False
                pygame.quit()
                sys.exit()

            if end:
                continue

            if event.type == pygame.MOUSEBUTTONDOWN:
                
                pos = pygame.mouse.get_pos()
                if pos [0] > 0 and pos[0] < 350:
                    if pos[1] > 0 and pos[1] < 450:

                        
                        col = pos[0] // 100
                        row = pos[1] // 100

                        print (self.board, col, row)
                        
                        if self.board[row][col] == '-':
                            self.move = True
                            self.move_pos = [row, col]

            if event.type == pygame.KEYDOWN:

                self.undo = True


    def update_board(self, row, col):
        global end

        self.stack.push(copy.deepcopy(self.board))

        self.board[row][col] = ICONS[self.icon]

        if all([i!='-' for i in self.board[0]+self.board[1]+self.board[2]]):
            end = True

        for icon in ICONS:
            
            if self.board[0][0] == icon and self.board[0][1] == icon and self.board[0][2] == icon:
                end = True
            if self.board[1][0] == icon and self.board[1][1] == icon and self.board[1][2] == icon:
                end = True
            if self.board[2][0] == icon and self.board[2][1] == icon and self.board[2][2] == icon:
                end = True

            if self.board[0][0] == icon and self.board[1][0] == icon and self.board[2][0] == icon:
                end = True
            if self.board[0][1] == icon and self.board[1][1] == icon and self.board[2][1] == icon:
                end = True
            if self.board[0][2] == icon and self.board[1][2] == icon and self.board[2][2] == icon:
                end = True

            if self.board[0][0] == icon and self.board[1][1] == icon and self.board[2][2] == icon:
                end = True
            if self.board[0][2] == icon and self.board[1][1] == icon and self.board[2][0] == icon:
                end = True

            if end:
                win = icon
                print (f'{icon} wins')
                break
                



        

    def run(self):
        

        while self.active:
            self.window.draw_board(self.board)
            self.event_listener()

            if self.move == True:
                self.move = False
                self.update_board(*self.move_pos)

                self.icon = (self.icon + 1) % 2

            if self.undo == True:
                print ('u has been pressed')
                self.undo = False
                self.undo_move()



                self.icon = (self.icon + 1) % 2

            pygame.display.flip()

    def undo_move(self):

        self.board = self.stack.pop()

g = Game()

g.run()
            
        


