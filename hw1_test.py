import data
import hw1
import unittest
import math
from hw1 import vowel_count, ascending_pairs, short_lists, add_prices, rectangle_area, books_by_author


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count(self):
        test1 = vowel_count("Millie")
        test2 = vowel_count("MILLIE")
        self.assertEqual(3,test1)
        self.assertEqual(3,test2)
    # Part 2
    def test_short_list(self):
        test1 = short_lists([[1, 2], [3, 4, 5], [6,4,1], [7, 8]])
        self.assertEqual([[1,2],[7,8]],test1)

    # Part 3
    def test_ascending_pairs(self):
        test1 = ascending_pairs([[5,9],[9,2,8],[1,1],[4,5]])
        self.assertEqual([[5,9],[9,2,8],[1,1],[4,5]],test1)

    # Part 4
    def test_add_prices(self):
        test1 = add_prices(data.Price(4,50),data.Price(9,70))
        self.assertEqual(data.Price(14,20),test1)

    # Part 5
    def test_rectangle_area(self):
        top_left = data.Point(1, 5)
        bottom_right = data.Point(4, 1)
        rect = data.Rectangle(top_left, bottom_right)
        self.assertEqual(rectangle_area(rect), 12.0)

    # Part 6
    def test_books_by_author(self):
        book1 = data.Book(authors=["Author A", "Author B"], title="Book One")
        book2 = data.Book(authors=["Author C"], title="Book Two")
        book3 = data.Book(authors=["Author A", "Author D"], title="Book Three")
        self.assertEqual(books_by_author("Author A", [book1, book2, book3]), [book1, book3])

    # Part 7
    def test_circle_bound(self):
        # Create a rectangle
        rect = data.Rectangle(data.Point(0, 2), data.Point(2, 0))
        bounding_circle = hw1.circle_bound(rect)
        expected_center = data.Point(1.0, 1.0)
        expected_radius = math.sqrt((rect.top_left.x - expected_center.x) ** 2 +
                                    (rect.top_left.y - expected_center.y) ** 2)
        self.assertEqual(bounding_circle.center, expected_center)
        self.assertEqual(bounding_circle.radius, expected_radius)
    # Part 8
    def test_below_average(self):
        employees = [data.Employee("Alice", 50000),
            data.Employee("Bob", 40000),
            data.Employee("Charlie", 30000),
            data.Employee("Diana", 60000)
        ]
        result = hw1.below_pay_average(employees)
        self.assertEqual(result, ["Bob", "Charlie"])

if __name__ == '__main__':
    unittest.main()
