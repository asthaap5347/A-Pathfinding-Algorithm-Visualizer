# A* Pathfinding Algorithm Visualizer

An interactive, real-time Python application built with Pygame that visualizes how the A* Search Algorithm finds the shortest path between two points while dynamically navigating user-built obstacles.

---

## Overview

This project provides an intuitive graphical interface to observe graph traversal in action. Users can design custom mazes, place start and end targets, and watch the A* algorithm evaluate nodes based on distance heuristics to guarantee the optimal path.

---

## Features

- **Interactive Canvas:** Draw start positions, destination targets, and wall barriers dynamically with left-click drags.
- **Real-Time Frontier Expansion:** Visualize open evaluation nodes versus already-inspected nodes frame by frame.
- **Optimal Path Reconstruction:** Automatically traces and highlights the shortest path backward once the target is reached.
- **Instant Controls:** Quickly trigger the algorithm run or clear the grid with dedicated hotkeys.

---

## How It Works

The visualizer implements the A* Search Algorithm, which picks the next node to explore by computing:

f(n) = g(n) + h(n)

- **g(n):** The exact step count or distance from the Start node to current node n.
- **h(n) (Heuristic):** The estimated distance from node n to the End target using Manhattan Distance:
  h(n) = |x1 - x2| + |y1 - y2|
- **f(n):** Total estimated cost of path through node n.

By utilizing a Priority Queue (Min-Heap), the visualizer efficiently inspects nodes with the lowest f(n) value first.

---

## Color Legend

| Color | Component | Description |
| :--- | :--- | :--- |
| Green | Start Node | Origin point of the pathfinder. |
| Red | End Node | Target destination node. |
| Black | Wall / Barrier | Impassable grid blocks. |
| Cyan | Open Set | Frontier nodes discovered and scheduled for evaluation. |
| Yellow | Closed Set | Nodes already inspected and finalized. |
| Purple | Optimal Path | The final reconstructed shortest path. |

---

## Controls

| Action | Input |
| :--- | :--- |
| Place Start Node | Left-Click (1st Click) |
| Place Target Node | Left-Click (2nd Click) |
| Draw Wall Barriers | Left-Click & Drag (3rd+ Click) |
| Erase Node | Right-Click |
| Run Visualizer | SPACEBAR |
| Clear Grid | C key |

---

## Getting Started

### Prerequisites

Ensure you have Python 3 installed along with Pygame:

pip install pygame


### How to Run

1. Open your terminal in the project directory.
2. Run the application:

python "Autonomous Grid Pathfinding Visualizer.py"

---

## Tech Stack

* Language: Python 3
* GUI Engine: Pygame
* Data Structure: queue.PriorityQueue (Min-Heap)
