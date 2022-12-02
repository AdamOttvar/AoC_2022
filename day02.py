import lib.AoC_lib as AoC
from collections import deque

@AoC.timer
def first_part(input_file):
    result = 0

    with open(input_file, 'r') as input:
        for line in input:
            opponent, response = line.rstrip('\n').split(' ')
            if 'A' in opponent:
                if 'X' in response:
                    result = result + 3 + 1
                elif 'Y' in response:
                    result = result + 6 + 2
                elif 'Z' in response:
                    result = result + 0 + 3
                else:
                    print("Unknown response")
            elif 'B' in opponent:
                if 'X' in response:
                    result = result + 0 + 1
                elif 'Y' in response:
                    result = result + 3 + 2
                elif 'Z' in response:
                    result = result + 6 + 3
                else:
                    print("Unknown response")

            elif 'C' in opponent:
                if 'X' in response:
                    result = result + 6 + 1
                elif 'Y' in response:
                    result = result + 0 + 2
                elif 'Z' in response:
                    result = result + 3 + 3
                else:
                    print("Unknown response")
            else:
                print("Unknown opponent move")
    return result


@AoC.timer
def second_part(input_file):
    result = 0
    horisontal = 0
    depth = 0
    aim = 0

    with open(input_file, 'r') as input:
        for line in input:
            result = result + 1
    return result


if __name__ == '__main__':
    DAY = '02'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('inputs/input02.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('inputs/input02.txt')))