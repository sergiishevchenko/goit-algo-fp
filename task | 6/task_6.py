from consts import ITEMS


def greedy_alg(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_calories = 0

    selected_items = []
    for item, info in sorted_items:
        if budget >= info['cost']:
            budget -= info['cost']
            total_calories += info['calories']
            selected_items.append(item)

    return selected_items, total_calories


def dynamic_programming_alg(items, budget):
    if not items or budget <= 0:
        return [], 0

    names = list(items.keys())
    costs = [items[name]['cost'] for name in names]
    calories = [items[name]['calories'] for name in names]

    dp = [[0 for _ in range(budget + 1)] for _ in range(len(items) + 1)]

    for i in range(1, len(items) + 1):
        for j in range(1, budget + 1):
            if costs[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - costs[i - 1]] + calories[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]

    selected_items = []
    for i in range(len(items), 0, -1):
        if dp[i][budget] != dp[i - 1][budget]:
            selected_items.append(names[i - 1])
            budget -= costs[i - 1]

    total_calories = dp[len(items)][budget]
    return selected_items[::-1], total_calories


if __name__ == '__main__':
    greedy_algorithm_result = greedy_alg(ITEMS, budget=50)
    dynamic_algorithm_result = dynamic_programming_alg(ITEMS, budget=50)

    print("Selected items:", greedy_algorithm_result[0])
    print("Total calories:", greedy_algorithm_result[1])

    print("Selected items:", dynamic_algorithm_result[0])
    print("Total calories:", dynamic_algorithm_result[1])