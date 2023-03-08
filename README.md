# Setup

Before running the project, you will need:

1. A code editor. I use [VS code](https://code.visualstudio.com/), though you can use whatever you're comfortable with.
2. A command line. I work on Mac OS/Linux, and I recommend [WSL](https://docs.microsoft.com/en-us/windows/wsl/install) if you're on Windows because it will allow you to use Linux commands. That said, you can use native Windows if you choose, you may just have to convert some commands on your own.
3. [Python 3 installed](https://www.python.org/downloads/).
4. You dont't need to install any dependencies for this, the graphical [Tkinter](https://docs.python.org/3/library/tkinter.html) package we'll be using comes bundled with Python 3.

# What the project looks like

![maze](https://i.imgur.com/RehzDga.gif)

# Flow Chart

![maze](/image/Maze-Adventure-Flowchart.png)

# How to run the project

In your terminal, cd to the root of your project and type: python main.py

# Project charter

## Project Title: Maze Adventure Project

## Project Objectives:

The objective of the project is to develop a software program that can solve mazes of varying complexity. The software should be able to take input in the form of a maze and output the solution in the form of a path from the start to the end of the maze.

## Project Scope:

The project will involve developing a maze adventure program that can take input in the form of a maze image or a text file and output the solution in the form of a path image or a text file. The maze adventure program will be designed to solve mazes of varying complexity, including mazes with multiple solutions.

## Project Deliverables:

Functional maze adventure program that takes input in the form of a maze image or a text file and outputs the solution in the form of a path image or a text file
User documentation and installation instructions
Technical documentation
Project Milestones:

Milestone 1: Requirements gathering and analysis
Milestone 2: Design and development of the maze adventure algorithm
Milestone 3: Integration and testing of the maze adventure program
Milestone 4: Documentation and finalization of the project

## Project Risks:

The maze adventure algorithm may not be able to handle mazes with complex paths or dead ends.
The software may not be able to read and process all types of maze images or text files.
The program may have compatibility issues with certain operating systems or hardware configurations.
Project Budget:
The project budget is $3,000, which includes the cost of software development, documentation, and testing.

## Project Stakeholders:

Project Manager: Responsible for overall project management and ensuring project objectives are met within the given timeline and budget.
Software Developers: Responsible for designing, developing, and testing the maze adventure program.
Quality Assurance Team: Responsible for ensuring that the program meets the functional and non-functional requirements and is free from defects.
End-users: The target audience for the maze adventure program who will be using the software to solve and explore mazes.

## Project Timeline:

The project is expected to take 1 week to complete, with the following timeline:

Milestone 1: 2 day
Milestone 2: 2 days
Milestone 3: 2 days
Milestone 4: 1 day

## Approval:

Approval of this project charter indicates agreement with the project objectives, scope, deliverables, milestones, risks, budget, stakeholders, and timeline. Any changes to these parameters must be approved by the project manager.

# Ideas for extending the project

- Add other solving algorithms, like breadth first search or A\*
- Make the visuals prettier, change the colors, etc
- Mess with the animation settings to make it faster/slower. Maybe make backtracking slow and blazing new paths faster?
- Add configurations in the app itself using Tkinter buttons and inputs to allow users to change maze size, speed, etc
- Make much larger mazes to solve
- Make it a game where users could chooses directions
- If we made it a game, allow the user to race an algorithm
- Make it 3 dimensional
- Time the various algorithms, see which ones are fastest
