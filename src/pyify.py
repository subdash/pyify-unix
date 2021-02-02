#!/usr/bin/env python3

import sys


def make_subprocess(args, idx):
    input_str = f" input=process_{idx - 1}.stdout," if idx > 0 else ""
    return f"process_{idx} = subprocess.run(" + \
           f"{args},{input_str} capture_output=True)"


if len(sys.argv) != 2:
    print('Error: Provide commands in a single string argument.')
    exit(1)

# Handle statements between pipes as separate commands
commands = sys.argv[1].split('|')
# For each "command", split up by spaces
parsed_commands = list(map(lambda x: x.split(' '), commands))

for i in range(len(parsed_commands)):
    # Lambda function filters out spaces
    parsed_commands[i] = list(filter(lambda x: x, parsed_commands[i]))
    print(make_subprocess(parsed_commands[i], i))
