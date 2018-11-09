#!/usr/bin/env python
import random

class Board:
    # initialize the Board object, and play the Tic-Tac-Toe with the computer
    # or your friend using the object's tictac function.  Enjoy!
    #
    # Example:
    #
    #    > import board.py
    #    > b = Board(dimension=3, nplayers=1)
    #    movement by computer
    #    -------
    #    | | | |
    #    -------
    #    | |O| |
    #    -------
    #    | | | |
    #    -------
    #
    # Now it's your turn.
    #
    #    > b.tictac(1,1)
    #    -------
    #    |X| | |
    #    -------
    #    | |O| |
    #    -------
    #    | | | |
    #    -------
    #
    #    movement by computer: (2, 1)
    #    -------
    #    |X| | |
    #    -------
    #    |O|O| |
    #    -------
    #    | | | |
    #    -------
    #
    # Keep moving until there is a winner.
    #
    def __init__(self, dimension=3, nplayers=1, beginBlock=None):
        self.dimension = dimension
        self.nplayers = nplayers
        self.players = ['O','X']
        self.__refreshBoard__()

        # initializing the first movement
        if beginBlock:
            # player 1 made the first movement
            self.computerPlayer = 1
            self.tictac(beginBlock[0], beginBlock[1])
        elif nplayers == 1:
            # computer made the first movement
            (x,y) = self.__calculateBestMovement__()
            print("movement by computer: (%d, %d)" % (x,y))
            self.tictac(x,y)
    
    def tictac(self, x, y):
        playerId = self.counter % 2
        self.__move__(x,y, self.players[playerId])
        print(self)
        if self.isToe():
            print("Toe!!")
            if self.nplayers == 1 and playerId == self.computerPlayer:
                print("Computer win!!")
            elif self.nplayers == 1:
                print("You win!!")
            else:
                print("Player %d win!!", playerId+1)
            # refresh the board
            self.__refreshBoard__()
        elif self.counter == self.dimension * self.dimension:
            print("Game over")
            self.__refreshBoard__()
        elif self.nplayers == 1 and playerId != self.computerPlayer:
            (xc,yc) = self.__calculateBestMovement__()
            print("movement by computer: (%d, %d)" % (xc,yc))
            self.tictac(xc,yc)
        else:
            pass

    def isToe(self):

        # toes contains strings of winning conditions
        toes = map(lambda x:x*self.dimension, self.players)

        # check row
        for i in xrange(self.dimension):
            if ''.join(self.blocks[i]) in toes:
                return True

        # check colume
        for i in xrange(self.dimension):
            bcol = map(lambda x:x[i], self.blocks)
            if ''.join( bcol ) in toes:
                return True

        # check diagnoal
        bdiagf = []
        bdiagb = []
        for i in xrange(self.dimension):
            bdiagf.append(self.blocks[i][i])
            bdiagb.append(self.blocks[i][self.dimension-i-1])
        if ''.join( bdiagf ) in toes:
            return True

        if ''.join( bdiagb ) in toes:
            return True

        return False

    def __refreshBoard__(self):
        self.blocks = []
        self.counter = 0
        self.computerPlayer = 0
        for i in xrange(self.dimension):
            self.blocks.append([" "] * self.dimension)

    def __move__(self, x, y, symbol):
        if self.blocks[x-1][y-1] != " ":
            print("Error: block (%d,%d) has been taken." % (x,y))
        else:
            self.blocks[x-1][y-1] = symbol
            self.counter += 1

    def __calculateBestMovement__(self):
        # identify blocks not being taken yet
        bavails = []
        for i in xrange(self.dimension):
            for j in xrange(self.dimension):
                if self.blocks[i][j] == " ":
                    bavails.append((i+1,j+1))
        # TODO: implement a smarter algorithm to determin the best movement
        return bavails[random.randint(0,len(bavails)-1)]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        s = "-" * (2*self.dimension + 1) + "\n"
        for i in xrange(self.dimension):
            s += "|" + "|".join(self.blocks[i]) + "|\n"
            s += "-" * (2*self.dimension + 1) + "\n"
        return s
