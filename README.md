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

## 1.4 NQueens 
This puzzle consists of placing a number of queens on the board in which none of them are able to "see" each other based on chess rules (a queen can see everything horizontall, vertically, and diagonally). To solve this, a CSP-Backtracking algorithm was implemented. This algorithm uses a depth first search to start creating solutions and "backtracking" (undoing the last move and testing another move) whenever a constraint is violated. In addition, in part 2, a separate puzzle was provided giving a flawed initial board and backtracking was also used to solve this.
> Main Files (Ignore the other test files)
> - Yung_Alex_NQueensPart1WithPrint.py: Prints out processing of solving NQueens for the first puzzle given (number of queens and size of board)
> - Yung_Alex_NQueensPart2.py: Given a flawed board, solves it using backtracking

## 1.5 Sudoku
This puzzle consists of solving a sudoku board. To solve this, a similar backtracking algorithm was used as in NQueens, albeit a bit more complicated due to the nature of the sudoku board. In part 2, the boards are harder to solve, so forward looking is applied to the backtracking algorithm for optimization. This allows the backtracking to detect errors earlier and thus go down correct paths earlier.
> Main Files:
> - sudoku.py: For solving the easier sudoku puzzles. Main algorithm method is csp_backtracking
> - sudoku2.py: For solving the harder sudoku puzzles with forward looking. Main algorithm method is csp_backtracking and futureSight
> - .txt files: They are the example puzzles given that we must solve

## 1.6 TicTacToe
This is a 2-player game in which we are trying to find the optimal move given the fact that the opponent will also choose the optimal move. Thus, we use the minimax algorithm, in which we recurse as far as possible through the game tree in a given time to find the optimal move. In part 2, instead of using minimax, I use the alternative version negamax, which simplifies the n-player algorithm minimax to a strict 2-player algorithm.
> Main Files:
> - tictactoe.py: uses minimax to find optimal moves thorugh a tictactoe game. The main methods are minimax, min_step, max_step, min_move, and max_move
> - tictactoe2.py: uses negamax to find optimal moves throughout a tictactoe game. The main methods are negamax and negamax_helper

## 1.7 and 1.8: Othello
This is a much harder 2-player game in which you are trying have the most number of spaces marked by your color. The game is a bit complicated for a brief description, so please watch this short video: https://www.youtube.com/watch?v=xDnYEOsjZnM&ab_channel=TripleSGames. Please skip the 1.7 folder, the testing folder, and look only at the 1.8 folder. To help find a objectively "good" move with our AI, we again use minimax. However, the weighting system is much more complicated than TicTacToe. There are several strategies implemented into the algorithm, such as marking corners and edges as a crucial point, as well as keeping balanced edges and avoiding the "danger" zone.
> Main Files:
> - server.py: Used to submit the TJ's Othello competition site to compete against other AIs. You will note both the manual weighting of each part of the board, and the minimax algorithm that takes the weighting into account. The main method is find_next_move and the methods implemented within it. The weighting can be found in the goal_test method.

## 1.9: Crosswords

# 1.9 - 3.2 Explanations TBD


