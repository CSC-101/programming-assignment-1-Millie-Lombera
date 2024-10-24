import data
from data import Price, Rectangle, Book


# Write your functions for each part in the space below.

# Part 1
def vowel_count(s:str)->int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# Part 2
def short_lists(input_list):
    return [nested_list for nested_list in input_list if len(nested_list) == 2]

# Part 3
def ascending_pairs(input_list):
    return [sorted(nested_list) if len(nested_list) == 2 else nested_list
        for nested_list in input_list]

# Part 4
def add_prices(price1:Price,price2:Price)->Price:
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents

    if total_cents >= 100:
        total_dollars += total_cents // 100
        total_cents = total_cents % 100

    return Price(total_dollars, total_cents)
# Part 5
def rectangle_area(rect:Rectangle)->float:
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.top_left.y - rect.bottom_right.y
    return width * height
# Part 6
def books_by_author(author_name: str, books: list[Book]) -> list[Book]:
    return [book for book in books if author_name in book.authors]

# Part 7


# Part 8


