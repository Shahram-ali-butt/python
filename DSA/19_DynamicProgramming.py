# 0/1 Knapsack Problem
# weights = [2,3,4,5]
# values = [3,4,5,6]
# capacity = 5

def maximum_profit(weights, values, capacity):
    n1 = len(weights)
    n2 = len(values)
    if n1 < 1 or n2 < 1: return 0
    if n1 != n2: return

    arr = [[0]*(capacity + 1) for _ in range(n1 + 1)]

    for i in range(1, len(arr)):
        for w in range(1, len(arr[0])):
            if(weights[i-1] > w):
                arr[i][w] = arr[i - 1][w]
            else:
                emptyCurrentWeight = arr[i - 1][w - weights[i-1]]
                maxProfit = max(emptyCurrentWeight + values[i-1], arr[i-1][w])
                arr[i][w] = maxProfit

    return arr[len(arr) - 1][len(arr[0]) - 1]

print(maximum_profit([2,3,4,5], [3,4,5,6], 5))