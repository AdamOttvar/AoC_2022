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
    winning_move = {'A': 'B', 'B': 'C', 'C': 'A'}
    loosing_move = {'A': 'C', 'B': 'A', 'C': 'B'}
    move_points = {'A': 1, 'B': 2, 'C': 3}

    with open(input_file, 'r') as input:
        for line in input:
            opponent, response = line.rstrip('\n').split(' ')
            if 'X' in response:
                result = result + move_points[loosing_move[opponent]] + 0
            elif 'Y' in response:
                result = result + move_points[opponent] + 3
            elif 'Z' in response:
                result = result + move_points[winning_move[opponent]] + 6
            else:
                print("Wrong")
    return result


if __name__ == '__main__':
    DAY = '02'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('../input/input02.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('../input/input02.txt')))