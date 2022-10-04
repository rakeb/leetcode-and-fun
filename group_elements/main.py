import copy
import random
import string
from collections import deque
import datetime


def removal(group):
    a = datetime.datetime.now()
    output = []
    while group:
        for dq in group[:]:
            if dq:
                output.append(dq.popleft())
            else:
                group.remove(dq)
    b = datetime.datetime.now()
    print((b - a).microseconds)
    # print(output)


def non_removal(group):
    a = datetime.datetime.now()
    output = []
    input_len = len(input_list)
    while input_len > 0:
        for dq in group:
            if dq:
                output.append(dq.popleft())
                input_len -= 1
    b = datetime.datetime.now()
    print((b - a).microseconds)
    # print(output)


if __name__ == '__main__':
    # input_list = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'C1', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6']
    INPUT_LEN = 1000000
    group = []
    input_list = set()
    for _ in range(INPUT_LEN):
        input_list.add(random.choice(string.ascii_uppercase) + str(random.randint(0, 10000)))
    input_list = list(input_list)
    input_list.sort()

    i = 0
    unique_group_identifier = input_list[i][0]
    for elem in input_list:
        if unique_group_identifier != elem[0]:
            unique_group_identifier = elem[0]
            i += 1
        if len(group) > i:
            dq = group[i]
        else:
            dq = deque()
            group.append(dq)
        dq.append(elem)

    removal(copy.deepcopy(group))
    non_removal(copy.deepcopy(group))
