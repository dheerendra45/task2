mport numpy as np

class RobotWorkspace:
    def _init_(self, rows, cols):
        self.workspace = np.ones((rows, cols), dtype=int)
        self.robot_row = 0
        self.robot_col = 0

    def insert_obstacle(self, row, col):
        if 0 <= row < self.workspace.shape[0] and 0 <= col < self.workspace.shape[1]:
            self.workspace[row, col] = 0

    def move_left(self):
        if self.robot_col > 0 and self.workspace[self.robot_row, self.robot_col - 1] != 0:
            self.robot_col -= 1

    def move_right(self):
        if self.robot_col < self.workspace.shape[1] - 1 and self.workspace[self.robot_row, self.robot_col + 1] != 0:
            self.robot_col += 1

    def move_up(self):
        if self.robot_row > 0 and self.workspace[self.robot_row - 1, self.robot_col] != 0:
            self.robot_row -= 1

    def move_down(self):  
        if self.robot_row < self.workspace.shape[0] - 1 and self.workspace[self.robot_row + 1, self.robot_col] != 0:
            self.robot_row += 1

    def visualize(self):
        workspace_copy = self.workspace.copy()
        workspace_copy[self.robot_row, self.robot_col] = 2
        for row in workspace_copy:
            for col in row:
                print(col, end=" ")
            print()
#test case
workspace = RobotWorkspace(3, 2)
workspace.insert_obstacle(5, 10)
workspace.insert_obstacle(4, 6)
workspace.move_right()
workspace.move_down()
workspace.move_left()
workspace.move_up()
workspace.visualize()
