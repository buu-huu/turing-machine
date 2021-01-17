

def read_program(path):
    with open(path) as f:
        instructions = f.readlines()
    instructions = [x.strip() for x in instructions]

    return instructions


def main():
    program = read_program('turing_programs/double_ones.txt')


if __name__ == '__main__':
    main()