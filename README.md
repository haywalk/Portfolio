# Hayden's Python Portfolio

This is a portfolio of some of my favourite programs I've written in Python since the summer of 2019.

**Note: Collatz Conjecture requires the MatPlotLib library, and Conway's Game of Life and the aquarium require PyGame.**

*Programs will be listed with a date, a description, and the skills involved in making them.*

---

## Aquarium (19 August 2019) *requires PyGame*

A simple aquarium. A random number of fish are spawned, each being an instance of the Fish class. Each is randomly assigned one of four breeds, and each has a randomly assigned speed. The fish will change directions when they come in contact with the screen's edge. Furthermore, each 50 millisecond cycle, each fish has a 1% chance (for each axis) of changing direction on its own, regardless of its position.

- Pygame
  - Importing sprites
- Random library
- Object-oriented programming
  - Multiple instances of a class
  - Each instance is unique and randomized

## Binary Search Algorithm (21 July 2020)

A binary search algorithm. A sorted array of numbers is given along with a number to search for. The function will return the position of the target number in the array, or None if it isn't there. Uses recursion.

- Recursion
- Conditionals
- Exception handling

## Binary to Decimal Converter (18 August 2019)

A simple binary to decimal converter; will accept an arbitrtary amount of bytes of arbitrary lengths.

- String slicing
  - Reversing
  - Concatenation
- Iterables
- Conditionals
- Math operators
  - Powers

## Caesar Cypher (25 July 2019)

Takes an encryption key (n) from 0-25 and moves each character ahead n spaces in the alphabet. If the letter reaches z, it wraps back to a.

- Iterables
- Conditionals
- For loops
- List wrapping
- Functions

## Cash register (3 August 2019)

Takes a sales total and amount tendered, then calculates change and lists the amount of each denomination of change to return.

- Rounding
- While Loops
- Conditionals
- Functions

## Collatz Conjecture (7 August 2019) *requires Matplotlib*

Takes a positive integer (n), and depending on its parity, will either divide it by 2 or multiply it by 3 then add 1, and repeat the whole process until the integer is equal to 1. It will then display a graph where x is the number of steps and y is the value of n.

- A Classic Algorithm
- While loops
- Conditionals
- Math operators
  - Modulus
  - Floor division
  - Addition
- Matplotlib Graphing Library

## Conway's Game of Life (22 August 2019) *requires Pygame*

Generates 100 squares that can each be either living or dead; each 1-second "generation," if a living square has less than two or more than three living neighbours, it will die from either underpopulation or crowding. If a dead square has exactly three living neighbours, it will become living, via reproduction.

- A cellular automaton
- Random library
- PyGame
  - Rectangles
- Conditionals
- Iteration
- Object-oriented programming
- Functions
- Methods
- Game loop

## Line/square drawing (27 July 2019)

A GUI application that takes a number (n) and, depending on which button is pressed, will generate either n lines or n rectangles, all of random size, position, and colour. It will display the last action completed in a status bar at the bottom.

- Tkinter GUI Library
  - Canvas
  - Buttons
  - Inputs
- Random library
- Object-Oriented Programming
- For Loops
- Functions
- Methods

## Hangman (5 August 2019)

A game of hangman that pulls words from a 100-word text file.

- Random library
- Reading from a text file
- For loops
- Game loop
- Conditionals
- Iterables
- Functions

## Insertion Sort (1 August 2020)

Basic insertion sort algorithm

- Iteration
- Lists
- For loops
- Algorithms

## Minefield/Minesweeper (20 July 2019)

A game that draws a 5x5 grid, in which a random number of randomly placed mines are hidden. The goal is to clear the board without hitting a mine.

- System commands
- Random library
- Wrapping
- Iterables
- Conditionals
- Functions
- Game loop

## Pig Latin (19 July)

Converts a word into "Pig Latin," i.e. if the word begins with a vowel, it will add "ay" to the end, and if it begins with a consonant, it will move the first letter to the end of the word and then add "ay."

- String slicing
- String concatenation
- Conditionals

## Recursive Guessing Game (24 August 2019)

The user chooses a number between 0 and 100 (unknown to the computer), and the computer will guess it. A light project that I included because of recursion.

- Recursion
- Conditionals
- Math operators
  - Floor division
  - Addition

## Roman Numerals to Integer (19 January 2020)

The user inputs a number in Roman numerals and it is returned as an integer.

- Dictionary data type
- Conditional
- For loop
  - Continue
- Lists/using indexes
- Iteration

## Monty Python's Python Soundboard (31 July 2019)

A just-for-fun soundboard of clips from Monty Python's Life of Brian. Fun Fact: The Python Programming Language is named after Monty Python!

- Tkinter GUI Library
  - Buttons
- Lambda Expressions
- Object-oriented programming
- Playing audio files



