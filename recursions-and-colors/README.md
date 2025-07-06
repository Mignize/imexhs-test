This project implements a recursive solution to the next problem

### Problem Description

You are given n disks of different sizes and colors stacked on a source rod. The goal is to transfer all
the disks to a target rod using an auxiliary rod

### Rules

1. Only one disk can be moved at a time.
2. A larger disk cannot be placed on top of a smaller disk.
3. Disks of the same color cannot be placed directly on top of each other, even if they differ in
   size.
4. You must use recursion to solve the problem.
5. You must use python to solve the problem.

### Definition

def moveDiskByRecursion(disks: list[tuple[int, str]]) -> list[tuple[int, str, str]] | int

### Start

1. Make sure you have Python installed.
2. Run it from the terminal: python index.py or run it using the run button or shortcut in your preferred IDE

### Examples to test

disks = [(3, "red"), (2, "blue"), (1, "green")]
result = moveDiskByRecursion(disks)
print(result)

Expected result: [(1, 'A', 'C'), (2, 'A', 'B'), (1, 'C', 'B'), (3, 'A', 'C'), (1, 'B', 'A'), (2, 'B', 'C'), (1, 'A', 'C')]
