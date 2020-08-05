## Steps for running the program
- `python main2.py`

## Algorithm used.
- Converting to CNF.
    - Remove the Double Implication.
    - Remove the Single Implication.
    - Generate the Truth Table
    - Evalute each expression using truth table and Find out the CNF using truth table method.
- Resolution Steps.
    - maintain two set 1 clouse and the second is new set to keep track of the cnfs.
    - Running a do while loop:
    - choose a pair of claues and find resolvent.
    - if resolvent is empty then return True else add this resolvent and union to new set.
    - if new set is a subset of clause set then return false else union clause set and new set.