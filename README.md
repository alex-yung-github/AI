# AI
These are the labs done over the course of my AI class. Most unique puzzles have a unique algorithm used to solve it.

## 1.0 Sliding Puzzle BFS
For this puzzle, I had to move the dot to the end while putting every part of the puzzle in either number or alphabetical order. To solve this, I used the BFS algorithm. In addition, you can how slow the BFS algorithm is when you run the main py file.

## 1.1 Word Ladders BFS
For this puzzle I had to go from the start point of the first word in the text puzzle file (e.g. puzzles_all.txt) to the second word in the same line by only changing the word one letter at a time using the given words in words_all.txt. 
> There are two main parts
> - wordladder.py: Main file for solving word ladder puzzles. It takes in the user input by asking which file the user wants it to solve. Then it solves the file and records the time taken
> - wordladder2.py: Duplicate file of wordladder2.py but used mainly for testing individual hard word combinations

## 1.2 Sliding Puzzle 2 
This puzzle is the same as the previous sliding puzzle, but with much harder "boards." Instead of using BFS, which would be way too slow, we use the inversion count and calculate it using that number

## 1.3 Train Routes 
This puzzle required creating an algorithm that would find the shortest and least costly path from one train station to another given train station costs and distances. Within this puzzle, we compared 3 different algorithms: A*, Djikstra, and BFS. A* and Djikstra tended to perform well.
> There is one main file to run this
> - The demos are not to be run, they were useful hints given to us
> - The main file is trainroutes.py: it creates a canvas that contains train routes, and the user can input what start and end they would like to find the shortest and cost efficient path

# 1.4 - 3.2 Explanations TBD


