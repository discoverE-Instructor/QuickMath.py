# QuickMath
This QuickMath game asks the player to guess a target number using a combination of basic arithmetic operations:&emsp;+&emsp;*&emsp;(&emsp;)&emsp;applied to a set of randomly shuffled numbers given by the player.

Heres a quick breakdown: 
1. The player is asked to input 5 small numbers (this can be changed with the HOW_MANY_NUMBERS variable in the script). The player can type in any number it is just recommended that they choose smaller numbers.
2. The game shuffles the numbers and creates a random equation using the basic arithmetic operations which the player has to guess.
3. If the player guesses wrong they are asked if they want to continue. If they choose not to then they are shown the solution and the game quits.
4. If the player chooses to continue they are asked if they want a hint. If the player does not want a hint then the game continues normally asking the player to input their guess again.
5. If the player asks for a hint, then the game prints the values of numbers in the shuffled order but does not show the arithmetic solution. This will help them know what order the numbers should be placed in.
6. Once the player guesses the right solution the game shows its solution (since there can be many) and quits.


To run this program type: python3 QuickMath.py
(if python3 is not installed try: python QuickMath.py)

If you wish to run this on the iPads you can use the CodeSandbox app.
