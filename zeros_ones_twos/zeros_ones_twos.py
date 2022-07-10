from copy import copy

from termcolor import colored


def parse_input():
    with open('in.txt') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines if line.strip()]
        try:
            lines = [[int(x) for x in line.split(" ")] for line in lines]
        except ValueError as e:
            print("Invalid input: {}".format(e))
            exit(1)
    for line in lines:
        for x in line:
            if x not in {0, 1, 2}:
                print("Invalid input: {} in line: {}. Input should be either 0, 1 or 2.".format(x, line))
                exit(1)
    return lines


def sort_0_1_2(nums):
    low = mid = 0
    high = len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[mid], nums[low] = nums[low], nums[mid]
            mid += 1
            low += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:
            mid += 1


def solve(input_array):
    sort_0_1_2(input_array)


def validate_output(input_line):
    if not input_line:
        return True
    curr_elem = input_line[0]
    for next_elem in input_line[1:]:
        if curr_elem == next_elem:
            continue
        elif next_elem == curr_elem + 1:
            curr_elem = next_elem
            continue
        else:
            return False
    return True


if __name__ == '__main__':
    lines = parse_input()
    for input_line in lines:

        test_case = copy(input_line)
        print("Test case:   {}".format(test_case))
        solve(input_line)
        print("Output:      {}".format(input_line))
        try:
            assert validate_output(input_line)
        except:
            print("Failed for test case: {}, output: {}".format(test_case, input_line))
            exit(1)
    print(colored("Accepted!", "green"))
