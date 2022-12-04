import lib.AoC_lib as AoC
from collections import deque
from itertools import islice

@AoC.timer
def first_part(input_file):
    result = 0
    rucksacks = []
    with open(input_file, 'r') as input:
        for line in input:
            ass1, ass2 = line.rstrip('\n').split(',')
            min1, max1 = map(int, ass1.split('-'))
            min2, max2 = map(int, ass2.split('-'))

            range1 = set([*range(min1, max1+1)])
            range2 = set([*range(min2, max2+1)])
            overlap = set(range1).intersection(range2)

            if range1.issubset(overlap):
                result = result + 1
            elif range2.issubset(overlap):
                result = result + 1

    return result


@AoC.timer
def second_part(input_file):
    result = 0
    rucksacks = []
    with open(input_file, 'r') as input:
        for line in input:
            ass1, ass2 = line.rstrip('\n').split(',')
            min1, max1 = map(int, ass1.split('-'))
            min2, max2 = map(int, ass2.split('-'))

            range1 = set([*range(min1, max1+1)])
            range2 = set([*range(min2, max2+1)])
            overlap = set(range1).intersection(range2)

            if len(overlap) > 0:
                result = result + 1

    return result


if __name__ == '__main__':
    DAY = '04'

    print('First solution for day' + DAY + ': ')
    print('Result: ' + str(first_part('../input/input04.txt')))

    print('Second solution for day' + DAY + ': ')
    print('Result: ' + str(second_part('../input/input04.txt')))