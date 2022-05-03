from abc import ABC, abstractmethod
from Game import Game
class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        pass

    def run(self):
        game= Game()
        self.turn(game)

    def turn(self,game):
        turnNo = game.TurnNo() +1
        print(game.__repr__())
        print(f"Player {turnNo} turn")
        while True:
            col = int(input("Enter column of move:"))
            if col >=0 and col <= 2:
                break
        while True:
            row  = int(input("Enter row of move:"))
            if col >=0 and col <= 2:
                break
        game.play(row,col)
        winner = game.winner()
        if winner ==True:
            print(f"Player {game.TurnNo()} won")
            exit()
        game.incrementTurn()

        drw = game.draw()
        if drw == True:
            print("the game ended in a draw")
            exit()

        


            

        self.turn(game)
    






       