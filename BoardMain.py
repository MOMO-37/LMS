import Board as b
import time

if __name__ == '__main__':
    board = b.Board(t=1e5, dt=1e-2, l=100)
    board.RunSim()
