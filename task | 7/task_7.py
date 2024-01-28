import random
import matplotlib.pyplot as plt

from consts import NUMBER_SIMULATIONS, NUMBER_DICES


def simulate_dice_rolls(num_simulations, num_dice):
    results = {}

    for _ in range(num_simulations):
        dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]
        total_sum = sum(dice_rolls)

        if total_sum in results:
            results[total_sum] += 1
        else:
            results[total_sum] = 1

    probabilities = {k: v / num_simulations for k, v in results.items()}

    return probabilities


if __name__ == '__main__':
    probabilities = simulate_dice_rolls(NUMBER_SIMULATIONS, NUMBER_DICES)

    sums = list(probabilities.keys())
    probabilities_values = list(probabilities.values())

    plt.bar(sums, probabilities_values, align='center', alpha=0.7)
    plt.xlabel('Sum of dice rolls')
    plt.ylabel('Probability')
    plt.title('Probability of getting certain sum using Monte Carlo simulation')
    plt.show()
