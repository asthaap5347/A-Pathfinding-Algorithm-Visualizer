import pygame
from queue import PriorityQueue

pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("A* Pathfinding Visualizer")

# --- COLORS ---
WHITE = (255, 255, 255)
GREY = (200, 200, 200)
RED = (255, 0, 0)          # End Point
GREEN = (0, 255, 0)        # Start Point
BLACK = (0, 0, 0)          # Wall Obstacles
YELLOW = (255, 255, 0)     # Checked Nodes
CYAN = (0, 255, 255)       # Scheduled Nodes
PURPLE = (128, 0, 128)     # Final Path

ROWS = 30
SQUARE_SIZE = 20

class Node:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.x = row * SQUARE_SIZE
        self.y = col * SQUARE_SIZE
        self.color = WHITE
        self.neighbors = []

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, SQUARE_SIZE, SQUARE_SIZE))

    def update_neighbors(self, grid):
        self.neighbors = []
        # DOWN
        if self.row < ROWS - 1 and grid[self.row + 1][self.col].color != BLACK:
            self.neighbors.append(grid[self.row + 1][self.col])
        # UP
        if self.row > 0 and grid[self.row - 1][self.col].color != BLACK:
            self.neighbors.append(grid[self.row - 1][self.col])
        # RIGHT
        if self.col < ROWS - 1 and grid[self.row][self.col + 1].color != BLACK:
            self.neighbors.append(grid[self.row][self.col + 1])
        # LEFT
        if self.col > 0 and grid[self.row][self.col - 1].color != BLACK:
            self.neighbors.append(grid[self.row][self.col - 1])

def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)

def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        if current.color != GREEN and current.color != RED:
            current.color = PURPLE
        draw()

def algorithm(draw, grid, start, end):
    count = 0
    open_set = PriorityQueue()
    open_set.put((0, count, start))
    came_from = {}

    g_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0

    f_score = {node: float("inf") for row in grid for node in row}
    f_score[start] = h((start.row, start.col), (end.row, end.col))

    open_set_hash = {start}

    while not open_set.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.color = RED
            start.color = GREEN
            return True

        for neighbor in current.neighbors:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = temp_g_score + h((neighbor.row, neighbor.col), (end.row, end.col))
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    if neighbor != end and neighbor != start:
                        neighbor.color = CYAN

        draw()

        if current != start and current != end:
            current.color = YELLOW

    return False

def make_grid():
    grid = []
    for i in range(ROWS):
        grid.append([])
        for j in range(ROWS):
            node = Node(i, j)
            grid[i].append(node)
    return grid

def draw_nodes(screen, grid):
    for row in grid:
        for node in row:
            node.draw(screen)

def draw_grid():
    for i in range(ROWS):
        pygame.draw.line(screen, GREY, (0, i * SQUARE_SIZE), (600, i * SQUARE_SIZE))
        pygame.draw.line(screen, GREY, (i * SQUARE_SIZE, 0), (i * SQUARE_SIZE, 600))

def draw_all(screen, grid):
    screen.fill(WHITE)
    draw_nodes(screen, grid)
    draw_grid()
    pygame.display.update()

def get_clicked_pos(pos):
    x, y = pos
    row = x // SQUARE_SIZE
    col = y // SQUARE_SIZE
    return row, col

grid = make_grid()
start = None
end = None

running = True
while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if pygame.mouse.get_pressed()[0]:  # LEFT CLICK
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos)

            if 0 <= row < ROWS and 0 <= col < ROWS:
                node = grid[row][col]

                if not start and node != end:
                    start = node
                    node.color = GREEN

                elif not end and node != start:
                    end = node
                    node.color = RED

                elif node != start and node != end:
                    node.color = BLACK

        elif pygame.mouse.get_pressed()[2]:  # RIGHT CLICK
            pos = pygame.mouse.get_pos()
            row, col = get_clicked_pos(pos)

            if 0 <= row < ROWS and 0 <= col < ROWS:
                node = grid[row][col]
                node.color = WHITE
                if node == start:
                    start = None
                elif node == end:
                    end = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and start and end:
                for row in grid:
                    for node in row:
                        node.update_neighbors(grid)

                algorithm(lambda: draw_all(screen, grid), grid, start, end)

            if event.key == pygame.K_c:
                start = None
                end = None
                grid = make_grid()

    draw_all(screen, grid)

pygame.quit()