"""
Jennifer Larsen
10/17/2023
This program prompts the user for test scores, stores them in a dictionary, and averages the scores.
"""


def get_test_scores():
    scores_dict = {}
    num_scores = int(input("Enter the number of test scores: "))

    for i in range(1, num_scores + 1):
        while True:
            try:
                score = float(input(f"Enter the test score #{i}: "))
                scores_dict.update({i: score})  # Use the update() method to add the score
                break
            except ValueError:
                print("Invalid input. Please enter a valid test score: ")

    return scores_dict


def average_scores(scores_dict):
    num_scores = len(scores_dict)
    if num_scores == 0:
        raise ValueError("Cannot calculate the average of an empty scores dictionary.")

    total_score = sum(scores_dict.values())
    return total_score / num_scores


def main():
    scores_dict = get_test_scores()
    avg = average_scores(scores_dict)
    print("Test scores and their average: ")
    for test_number, score in scores_dict.items():
        print(f"Test {test_number}: {score}")
    print(f"Average Score: {avg}")


if __name__ == "__main__":
    main()
