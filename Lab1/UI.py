class UI:
    def __init__(self, controller):
        self.controller = controller

    def mainMenu(self):
        print("dfs")
        print(self.controller.dfs())
        print("gbfs")
        print(self.controller.gbfs())



