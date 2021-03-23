# Turing Machine
Python implementation of the turing machine.

## Info
This program is able to run programs in a turing machine and to visualize all steps to the result. I coded this small project quick and dirty during my degree in cyber security to make life easier for me - don't expect a beauty.

![Turing GUI](images/turing.jpg)

Call the program via the command line and pass the turing program as an argument:

`python turing.py turing_programs/double_ones.txt`

## Installation
Installation is not required. Just make sure, you habe PyQt5 installed or do it by executing the following command.

```bash
python -m pip install -r requirements.txt
```

The program is written in Python 3.

## Alphabet
You can use a turing alphabet of all letters or numbers. Internally, they are obviously handled as strings.

## Configuration
### Initial State
The initial state of the tape can be configured in the file `initial_state.txt`. When the program starts it uses the elements in this file as the initial tape state. All elements have to be separated by commas. Example:

`1, 1, 0, 1`

### Turing Programs
Turing programs are stored in textfiles. Examples are already included. Turing programs follow the structure

\<STATE TO BE CHECKED>, \<LETTER TO BE CHECKED> > \<NEW STATE>, \<LETTER TO BE WRITTEN>, \<MOVEMENT (LEFT/RIGHT)>

Example:

`z0, 1, > z0, 0, R`

When starting the program, the turing machine is in state 0 (z0).
