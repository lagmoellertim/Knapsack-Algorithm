def knapsack(value_weight_set, max_weight):
    length = len(value_weight_set)
    array = [[0 for _ in range(max_weight + 1)] for _ in range(length)]
    keep = [[False for _ in range(max_weight + 1)] for _ in range(length)]
    for i in range(length):
        for j in range(max_weight + 1):
            param = (value_weight_set[i][0] + array[i - 1][j - value_weight_set[i][0]], array[i - 1][j])
            if value_weight_set[i][1] <= j and param[0] > param[1]:
                array[i][j] = param[0]
                keep[i][j] = True
            else:
                array[i][j] = param[1]

    current_value = 0
    current_weight = 0
    items = []
    for i in range(length-1, -1, -1):
        if keep[i][max_weight]:
            items.append(i)
            current_value += value_weight_set[i][0]
            current_weight += value_weight_set[i][1]
            max_weight -= value_weight_set[i][1]
    return current_value, current_weight, items
