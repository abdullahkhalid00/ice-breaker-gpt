def load_instructions(file):
    instructions = []
    with open(file, 'rb') as f:
        for line in f:
            instructions.append(line.decode().strip())
    return '\n'.join(instructions)
