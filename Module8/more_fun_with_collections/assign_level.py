"""
Jennifer Larsen
10/17/2023
This program uses a dictionary like a switch case and returns a
level and assigned points.
"""


def switch_level(level):
    points_dict = {
        'N': 50,  # Novice
        'B': 150,  # Beginner
        'E': 300,  # Experienced
        'A': 500,  # Advanced
    }

    points = points_dict.get(level, 'Invalid level')
    return points


def main():
    levels_to_test = ['N', 'B', 'E', 'A', 'S']  # 'S' for an invalid level

    for level in levels_to_test:
        points = switch_level(level)
        if points == 'Invalid level':
            print(f"Invalid level: '{level}'")
        else:
            print(f"Level: {level}, Points: {points}")


if __name__ == "__main__":
    main()
