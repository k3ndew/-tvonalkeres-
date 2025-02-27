matrix = []

with open("térképező.txt", "r") as file:
    for line in file:
        matrix.append(list(line.strip()))
map = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]

class geo:
    def __init__(self, x, y, map, matrix):
        self.x = x
        self.y = y
        self.map = map
        self.matrix = matrix

    def move(self, direction):
        if direction == "up":
            if self.y > 0 and self.matrix[self.y-1][self.x] != "#":
                self.y -= 1
                self.map[self.y][self.x] = self.matrix[self.y][self.x]
            elif self.matrix[self.y-1][self.x] == "#":
                self.map[self.y-1][self.x] = "#"
        elif direction == "down":
            if self.y < len(self.matrix)-1 and self.matrix[self.y+1][self.x] != "#":
                self.y += 1
                self.map[self.y][self.x] = self.matrix[self.y][self.x]
            elif self.matrix[self.y+1][self.x] == "#":
                self.map[self.y+1][self.x] = "#"
        elif direction == "left":
            if self.x > 0 and self.matrix[self.y][self.x-1] != "#":
                self.x -= 1
                self.map[self.y][self.x] = self.matrix[self.y][self.x]
            elif self.matrix[self.y][self.x-1] == "#":
                self.map[self.y][self.x-1] = "#"
        elif direction == "right":
            if self.x < len(self.matrix[0])-1 and self.matrix[self.y][self.x+1] != "#":
                self.x += 1
                self.map[self.y][self.x] = self.matrix[self.y][self.x]
            elif self.matrix[self.y][self.x+1] == "#":
                self.map[self.y][self.x+1] = "#"
