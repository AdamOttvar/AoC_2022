import lib.AoC_lib as AoC
from collections import deque
from itertools import islice

prio_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

@AoC.timer
def first_part(input_file):
    result = 0
    rucksacks = []
    with open(input_file, 'r') as input:
        for line in input:
            str_line = line.rstrip('\n')
            compartment1 = str_line[0:int(len(str_line)/2)]
            compartment2 = str_line[int(len(str_line)/2):]
            result = result + prio_list.index(set(compartment1).intersection(compartment2).pop())+1
    return result


@AoC.timer
def second_part(input_file):
    result = 0
    with open(input_file, 'r') as input:
        while True:
            next_three_lines = list(islice(input, 3))
            if not next_three_lines:
                break

            in_all_rucksacks = set(next_three_lines[0].rstrip('\n')).intersection(next_three_lines[1].rstrip('\n')).intersection(next_three_lines[2].rstrip('\n')).pop()
            result = result + prio_list.index(in_all_rucksacks) + 1

    return result


if __name__ == '__main__':
    DAY = '03'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('../input/input03.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('../input/input03.txt')))