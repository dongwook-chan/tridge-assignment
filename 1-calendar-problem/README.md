# Calendar Problem
Count the day of the week on which each month in the given century starts.  

## Usage and Examples
Basic solution for the assignment.
```bash
(env) $ cd 1-calendar-problem
(env) $ python3 dow_counter.py
```
You can also specify target `century` and `mode` to choose from 4 solutions described below.  
```bash
(env) $ python3 dow_counter.py --century [0-9999] --mode [0-3]
```
| keyword | required | choices | default |
| :-: | :-: | :-: | :-: |
| mode | False | [0-3] | 0 |
| century | False | [0-9999] | 20 |


## Solutions

### 0. Tabular
The day of the week on which each month starts has a cycle of 4 centuries.  
`TabularDowCounter.dow_for_century_modulo_4` holds all possible for each century within the cycle.

### 1. Formula
Implemented [Sakamoto's_methods](https://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Sakamoto's_methods).  

### 2. Brute Force 
Counts day offset of first day in each month from the beginning day.
Remainder of day offset divided by 7 equals the day of the week.

### 3. Standard Library
Use `datetime` built-in datatype to get the day of week.  
All the other solutions are tested against this solution in `test_dow_counter.py`

### Complexity Comparison

| Solution # | Solution Name | Time Complexity |
| :-: | :-: | :-: |
| 0 | Tabular          | O(constant) |
| 1 | Formula          | O(# of days in given century) |
| 2 | Brute Force      | " |
| 3 | Standard Library | " |
