import numpy as np
import sys
class field(object):

    def __init__(self):
        self.field = np.empty((3,3))
        self.player = 2
        for i in range(9):
            self.field[int(i/3),i%3]=0

    def winning(self):
        row = np.array([self.player,self.player,self.player])
        if np.all(self.field[:,0] == row) or np.all(self.field[:,1] == row) or np.all(self.field[:,2] == row)\
        or np.all(self.field[0,:] == row) or np.all(self.field[1,:] == row) or np.all(self.field[2,:] == row)\
        or (self.field[0,0] == self.player and self.field[1,1] == self.player and self.field[2,2] == self.player)\
        or (self.field[0,2] == self.player and self.field[1,1] == self.player and self.field[2,0] == self.player):
            print(f'Player {self.player} wins')
            return True
        for i in range(9):
            if(self.field[int(i/3),i%3]==0):
                return False
        print('Unentschieden')
        return True

    def player_change(self):
        self.player = self.player%2+1

    def print_field(self):
        x = [[0,0,0], [0,0,0], [0,0,0]]
        for i in range(3):
            for j in range(3):
                if self.field[i,j] == 0:
                    p = ' '
                elif self.field[i,j] == 1:
                    p = 'x'
                else:
                    p = 'o'
                x[i][j] = p
            print(x[i])
        print('\n')


    def makestep(self):
        while(True):
            try:
                x = int(input('Eingabe\n'))
                if (x <0 or 8<x) or self.field[int(x/3),x%3] != 0::
                    raise ValueError
                self.field[int(x/3),x%3] = self.player
                break
            except ValueError:
                print('Ungültige Eingabe')

if __name__ == 'main':
    field = field()
    while(not field.winning()):
        field.player_change()
        field.print_field()
        field.makestep()
    field.print_field()
