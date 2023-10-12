"""
average_scores.py
Jennifer Larsen
10/10/2023
This module contains functions to explore tuples, arbitrary args and keyword args
and returns an average of scores entered.
"""


def average_scores(*scores, **string_items):
    # Use *args for average calculation
    if not scores:
        raise ValueError("No scores provided. Cannot calculate average.")

    total = sum(scores)
    count = len(scores)
    average = total / count

    f_name = string_items.get("first_name", "Unknown")
    l_name = string_items.get("last_name", "Unknown")
    gpa = string_items.get("gpa", "Unknown")
    course = string_items.get("course", "Unknown")

    for key, value in string_items.items():
        print("%s == %s" % (key, value))

    return f"Result: name = {f_name} {l_name} gpa = {gpa} course = {course} with current average {average:.2f}"


if __name__ == '__main__':
    print(average_scores(4, 3, 2, 4, first_name='Michelle', last_name='Ruse', major='World_domination'))
    print(average_scores(99, 85, 77, 100, 89, first_name='Sally', last_name='Jones', gpa=3.8, major='CIS'))
    print(average_scores(77, 55, 66, 99, first_name='John', last_name='Dillinger', gpa=2.5, major='Criminal Justice'))
    print(average_scores(88, 99, 100, first_name='Lucy', last_name='Lane', fav_book='None', gpa=3.9, major='English'))

