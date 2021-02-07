# Turing Machine
Python implementation of the turing machine.

## Info
This program is able to run programs in a turing machine and to visualize all steps to the result.

![Turing GUI](images/turing.jpg)

The program can be started from the commandline. Just pass the turing program as an argument to the program call. Example:

`python turing.py turing_programs/double_ones.txt`

## Installation
The program does not need to be installed. You just need to install PyQt5 by executing the following command.

```bash
python -m pip install -r requirements.txt
```

And then, run the program:

```bash
cd src
python turing.py
```

Info: You need to use Python 3. Depending on your Python installation, you have to use the command `python3` instead of `python`.

## Alphabet
You can use an alphabet of all letters or numbers. Internally, they are handled as strings.

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
