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
This utilizes forward looking and backtracking in order to solve difficult crossword puzzles. Given a X by Y board by the user, it places random blocking squares, squares where there aren't supposed to be letters, and then attempts to solve the board. These blocking squares must be 3 or more squares, and the number of them can be specified. After that, the algorithm attempts to fill in the crossword with the given words in the wordlist.txt and twentyk.txt. In the end, the algorithm is versatile enough to solve boards that aren't squares (rectangular boards) and also able to solve most boards with size 13x13 or under easily.
> Main File:
>  - crosswordspt2.py: Able to solve larger boards than crosswords.py. The other files are txt files for the possible words to use and asedf.py, a file which an unrelated calculation was made.
> Main method explanations:
>  - addBlockingSquares() adds blocking squares
>  - getInput() gets board size, possible words from text files, and number of blocking squares
>  - csp_backtracking(): main algorithm that attempts to solve the crossword
  >  - connectedCheck(): check that checks if the board is valid; if so, return true
>    - possiblePlaces(): returns the possible places to place a new character
>    - placeBlock(): places a letter
>    - fillInImpossibles(): removes possible places to place a new letter after placing a letter
>    - getScore(): gets the score of the board, and within the backtracking it uses the best possible board and chooses that as the next move for each iteration of placing the next letter

## 2.0: Regex
This project was creating different regex strings that would work towards different requirements. the specifications are listed on TJ's AI grader site: https://ai.sites.tjhsst.edu/. The main files are regexpt1.py to regexp4.py, and they incrementally get harder in terms of the specifications of the strings.

## 2.1 Genetic Algorithms
Testing with genetic algorithms to help decode encoded strings of text. Though this was a test, the uses of genetic algorithms becomes more useful with the future projects.

## 2.2 Genetic Algorithms and Tetris
Using genetic algorithms, an algorithm was created to reach over 65000 score in a game of Tetris. Ignore the poor naming conventions and lack of file organization. The main files are listed below--please ignore the other files. Here, the genetic algorithm initializes weights for the strategy parameters, which are the defining parameters that tell the algorithm where to place the next piece. The genetic algorithm then runs on weights and continues until desired accuracies are obtained. The genetic algorithm process is described more below in the main file.
> Main Files
> - tetrispt2.py: In this file, there are a multitude of helper methods and a main method that runs the genetic algorithm to train a strong Tetris solver. At the bottom in the userInput() method, it asks the user to either create a new algorithm for Tetris or to continue with an existing one. After the user chooses to either create a new algorithm or use an existing one, it prompts the user to either train the algorithm or to use it to play Tetris.
> - Training the algorithm prompts it to create new random weights and run the genetic algorithm. In this genetic algorithm, it uses the weights from one generation, runs them on Tetris and records their scores. The algorithms are sorted from best to worst, and then they are run through many tournaments to create the next generation. The tournament chooses 2 algorithms through a selection process: starting from algorithm 1 (the best algorithm), it has a 75% chance of being a parent. Otherwise, the selection moves to the next parent which also has 75% chance of being chosen (percentage can be changed). This selection continues until a parent is found and repeats a second time. This selection method allows for the best children to be created from the highest scoring parents, while also allowing for variation because the worse algorithms still have a chance to be a parent algorithm. A child is then breeded from the 2 parents by selectively incorporating traits from both parent algorithms. Finally, a mutation is added to the child to add variation. This selection, breeding, and mutation process creates 1 child, and this repeats for however many algorithms are desired per generation. As the algorithms improve, such as after 3 generations, very high scores can be seen when playing Tetris.
> - Playing tetris tests the algorithm in an actual Tetris game, which can be watched through the fancy boards printed in the terminal.

## 3.0 - 3.2: Machine Learning Algorithms
These machine learning algorithms are described within the ML repository on this account. 

