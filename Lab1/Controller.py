from Sudoku import Sudoku


class Controller:
    def __init__(self, filename):
        self.instance = Sudoku(filename)

    def orderStates(self, listOfStates):
        # returns the ordered list of states
        pass

    def dfs(self):
        queue = [self.instance]
        while len(queue) != 0:
            current_state = queue.pop(0)
            if current_state.completed() is True:
                return current_state
            next_states = current_state.expand()
        #     check if some of the next states are already in the queue
            for next_state in next_states:
                do_not_add = False
                for states in queue:
                    if next_state == states:
                        do_not_add = True
                        break
                if not do_not_add:
                    queue.append(next_state)

    def gbfs(self):
        queue = [self.instance]
        while len(queue) != 0:
            current_state = queue.pop(0)
            if current_state.completed() is True:
                return current_state
            next_states = current_state.expand_best()
            #     check if some of the next states are already in the queue
            for next_state in next_states:
                do_not_add = False
                for states in queue:
                    if next_state == states:
                        do_not_add = True
                        break
                if not do_not_add:
                    queue.append(next_state)


