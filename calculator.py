"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

from functools import reduce

quit_cal = False
while not quit_cal:
    user_input = input('\n write your equqation here \n')
    tokenized_input = user_input.split(' ')

    if tokenized_input[0] == 'q':
        print('\n you are about to quit the program \n')
        quit_cal = True

    elif tokenized_input[0] == 'pow':
        pow_cal = power(float(tokenized_input[1]), float(tokenized_input[2]))
        print(pow_cal)

    # elif tokenized_input[0] == '+':
    #     add_cal = add(float(tokenized_input[1]), float(tokenized_input[2]))
    #     print(add_cal)

    elif tokenized_input[0] == '+':
        # exam = float(tokenized_input)
        # total = reduce(add, tokenized_input)
        add_cal = (float(tokenized_input[1]), float(tokenized_input[2]))
        total = reduce(add, tokenized_input)
        print(total)
        # add_cal = reduce(
        # add(float(tokenized_input[1]), float(tokenized_input[2])))

    elif tokenized_input[0] == '-':
        subtract_cal = subtract(
            float(tokenized_input[1]), float(tokenized_input[2]))
        print(subtract_cal)

    elif tokenized_input[0] == '*':
        multiply_cal = multiply(
            float(tokenized_input[1]), float(tokenized_input[2]))
        print(multiply_cal)

    elif tokenized_input[0] == '/':
        divide_cal = divide(
            float(tokenized_input[1]), float(tokenized_input[2]))
        print(divide_cal)

    elif tokenized_input[0] == 'square':
        square_cal = square(
            float(tokenized_input[1]))
        print(square_cal)

    elif tokenized_input[0] == 'cube':
        cube_cal = cube(float(tokenized_input[1]))
        print(cube_cal)

    elif tokenized_input[0] == 'mod':
        mod_cal = mod(float(tokenized_input[1]), float(tokenized_input[2]))
        print(mod_cal)
