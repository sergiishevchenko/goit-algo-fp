import random
import matplotlib.pyplot as plt


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
    number_simulations = 100000
    number_dice = 2

    probabilities = simulate_dice_rolls(number_simulations, number_dice)

    sums = list(probabilities.keys())
    probabilities_values = list(probabilities.values())

    plt.bar(sums, probabilities_values, align='center', alpha=0.7)
    plt.xlabel('Sum of dice rolls')
    plt.ylabel('Probability')
    plt.title('Probability of getting certain sum using Monte Carlo simulation')
    plt.show()
