from collections import deque

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    input_list = ['A1', 'A2', 'A3', 'A4', 'B1', 'B2', 'B3', 'C1', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6']
    group = []
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

    output = []
    while group:
        inner_list = []
        for dq in group[:]:
            if dq:
                inner_list.append(dq.popleft())
            else:
                group.remove(dq)
        if inner_list:
            output.append(inner_list)
    print(output)  # [['A1', 'B1', 'C1', 'E1'], ['A2', 'B2', 'E2'], ['A3', 'B3', 'E3'], ['A4', 'E4'], ['E5'], ['E6']]
