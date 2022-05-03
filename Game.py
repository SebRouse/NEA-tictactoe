


class Game:

    def __init__(self):
        self._board = [[None,None,None],[None,None,None],[None,None,None]]
        self._turn = 0
        self._noOfTurns = 0
        self.__icons = {0:"X",1:"O"}

    def __repr__(self):
        return repr(self._board)

    def incrementTurn(self):
        self._noOfTurns +=1
        self._turn = self._noOfTurns % 2

    def play(self,col,row):
        if self._board[col][row] == None:
            self._board[col][row] = self.__icons[self._turn]
        else:
            raise ValueError

    
    def TurnNo(self):
        return self._turn
                
    
    
    def winner(self):
        win = False
        for i in range(3):
            if self._board[i][0] == self._board._[i][1] and self._board[i][0]== self._board[i][2] and self._board[i][0] != None:
                win = True
            elif self._board[0][i] == self._board[1][i] and self._board[0][i] == self._board[2][i] and self._board[0][i] != None:
                win = True
        if self._board[0][0] == self._board[1][1] and self._board[0][0] == self._board[2][2] and self._board[1][1] != None:
            win = True
        elif self._board[0][2] == self._board[1][1] and self._board[1][1] == self._board[2][0] and self._board[1][1] != None:
            win = True
        return win

    def draw(self):
        drw = False
        if self._noOfTurns == 9:
            drw = True
        return drw





if __name__ == "__main__":
    pass

