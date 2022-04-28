
class Game:

    def __init__(self):
        self._board = [[None,None,None],[None,None,None],[None,None,None]]
        self._turn = 0
        self.__icons = {0:"X",1:"O"}

    def __repr__(self):
        pass

    def play(self,row,col):
        try self._board[row][col]=None
            self._board[row][col] = self.__icons[self._turn]
            incrementTurn()
        except ValueError: 
    
    def incrementTurn(self):
        self._turn +=//2
        
    
    @property
    def winner(self):
        pass


if __name__ == "__main__":
    pass

