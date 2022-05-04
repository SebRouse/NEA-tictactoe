from abc import ABC, abstractmethod
from Game import Game
import tkinter as tk
from tkinter import X
class Ui(ABC):

    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = tk.Tk()
        root.title("Tic Tac Toe")
        frame = tk.Frame(root)
        frame.pack()

        tk.Button(
            frame,
            text='Show Help').pack(fill=X)


        tk.Button(
            frame,
            text='Play Game').pack(fill=X)


        tk.Button(
            frame,
            text='Quit').pack(fill=X)
        self._root = root

    def run(self):
        self._root.mainloop()

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
            print(f"Player {turnNo} won")
            exit()
        game.incrementTurn()

        drw = game.draw()
        if drw == True:
            print("the game ended in a draw")
            exit()

        


            

        self.turn(game)
    






       