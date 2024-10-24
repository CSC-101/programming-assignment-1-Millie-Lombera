import data
import math
from data import Price, Rectangle, Book


# Write your functions for each part in the space below.

# Part 1
def vowel_count(s:str)->int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

#Design Recipe
#Purpose: To count the number of vowels in a given string
#Input:  A string s   Output: An integer representing the total number of vowels

# Part 2
def short_lists(input_list:list[list[int]])->list[list[int]]:
    return [nested_list for nested_list in input_list if len(nested_list) == 2]
#Design Recipe
#Purpose: To filter and return a new list containing only those nested lists from the input list that have exactly two elements
#Input:  A list of nested lists   Output: A new list consisting of only the nested lists from the input that have a length of 2

# Part 3
def ascending_pairs(input_list:list[list[int]])->list[list[int]]:
    return [sorted(nested_list) if len(nested_list) == 2 else nested_list
        for nested_list in input_list]
#Design Recipe
#Purpose: to take a list of lists (nested lists) and return a new list where any nested
# list containing exactly two elements is sorted in non-descending order. Nested lists with lengths other than
# two remain unchanged.
#Input: A list of lists   Output:  new list of lists where nested lists of length 2 are sorted, and all other nested lists are included unchanged

# Part 4
def add_prices(price1:Price,price2:Price)->Price:
    total_dollars = price1.dollars + price2.dollars
    total_cents = price1.cents + price2.cents

    if total_cents >= 100:
        total_dollars += total_cents // 100
        total_cents = total_cents % 100

    return Price(total_dollars, total_cents)

#Design Recipe
#Purpose: To get the sum of two Price objects, ensuring that the total cents do not exceed 99
#Input:  Two Price objects (price1 and price2)  Output: A new Price object that represents the total price

# Part 5
def rectangle_area(rect:Rectangle)->float:
    width = rect.bottom_right.x - rect.top_left.x
    height = rect.top_left.y - rect.bottom_right.y
    return width * height
#Design Recipe
#Purpose: To get the area of a given rectangle.
#Input: two corner points   Output: area of the rectangle:float

# Part 6
def books_by_author(author_name: str, books: list[Book]) -> list[Book]:
    return [book for book in books if author_name in book.authors]
#Design Recipe
#Purpose: To filter and return a list of books written by a specific author
#Input:  string representing the name of the author whose books are to be found & list of Book objects, where each Book has a list of authors and a title
# Output: list of Book objects that have the specified author in their authors list

# Part 7
def circle_bound(rectangle: Rectangle) -> data.Circle:
    center = data.Point(
        (rectangle.top_left.x + rectangle.bottom_right.x) / 2,
        (rectangle.top_left.y + rectangle.bottom_right.y) / 2
    )
    radius = math.sqrt(
        (rectangle.top_left.x - center.x) ** 2 +
        (rectangle.top_left.y - center.y) ** 2
    )
    return data.Circle(center, radius)
#Design Recipe
#Purpose:To do the math and return a bounding circle that encapsulates a given rectangle. This circle
# is centered at the midpoint of the rectangle and has a radius equal to the distance from the center
# to one of the rectangle’s corners
#Input:  A Rectangle object, which has a top_left corner and a bottom_right corner, both represented as Point objects
# Output: A Circle object representing the smallest circle that encloses the rectangle

# Part 8
def below_pay_average(employees: list[data.Employee]) -> list[str]:
    if not employees:
        return []
    average_pay = sum(employee.pay_rate for employee in employees) / len(employees)
    return [employee.name for employee in employees if employee.pay_rate < average_pay]

#Design Recipe
#Purpose: to find and return a list of employee names whose pay rates are below the average
# pay rate of all employees in the given list
#Input:  List of Employee objects, where each object has a name and a pay rate
# Output: List of strings representing the names of employees who earn less than the average pay rate