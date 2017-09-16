# Winning Texas Hold'em Strategy

This project was created to help me demonstrate several skills I've acquired during my past several jobs.

## Program Overview

This is a No Limit Texas Hold'em (NLTH) Pre-flop Range Trainer. It gives a player random cards and a random position at the table. Then, the player has to decide if they would open or fold their hand. Finally, the application compares the player's decision to the mathematically correct decision based off of the selected hand range (which is customizable by the user).

Several examples of correct and incorrect hand range layouts are included in the hand_ranges folder. The Unimproved Range.txt is the most basic and a good one to start using in the game if you aren't very familiar with hand ranges.

## Licensing

Please see the file called LICENSE.

## Program Technical Information
* Developed in Python.
* Test cases in py.test.

### Programming principles used:
* Variables
* Conditions / Decisions
* Functions
* Loops
* Classes / Objects
* Test Driven Development (TDD)

### Testing concepts demonstrated:
* Automated testing
  * 49 independent test cases are in their own package.
* System testing
  * There is a module under app.app_systems_test that has more details.
  * This runs in a 'live' environment and touches all of the critical functionality of the application.
* Performance testing

### Design features demonstrated:
* The most important game instruction information is shown to the user inside the game at the point in time it is most relevant (context specific documentation).
* Problem input is handled behind the scenes inside the code. The user is shown a message at the specific point in time it occurs and the program continues if possible. Note: Many of the errors require the user to fix bad data; so the program stops and then has to be rerun again. Some error checking is done to look for if an incorrect:
  * file name is enter; i.e. rage instead of range.
  * hand type is entered; i.e. Ad5h instead of A5o.
  * number of hand types is entered; anything besides 169.
* Report Writing
  * Comma Separated Values (csv) or Text (txt) files.
  * Reports can be used later for data analysis.
* Directory / Folder Navigation (Windows Only)

### Limitations of the game:
* The user has to have Python installed on their computer.
* The user has to know how to clone the repository from GitHub onto their computer.
* The program only works for the Windows operating system.
* There is no graphical user interface. Input is only accepted through the keyboard.

## Future Releases
This game will not be updated in this project here. However, an improved version of this game is one of my candidates to be released in the future as an Android application. Also, the code / information is available for anyone to modify as they desire.

