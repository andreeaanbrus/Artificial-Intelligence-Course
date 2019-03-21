from Controller import Controller
from State import State
from Sudoku import Sudoku
from UI import UI

ctrl = Controller("input1.txt")
ui = UI(ctrl)
ui.mainMenu()
