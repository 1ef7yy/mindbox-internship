import unittest
import area_calculator as ac


class TestCalculator(unittest.TestCase):
    def test_area(self):
        mock_data = {
            (1, ): 3.141592653589793,
            (3, ): 28.274333882308138,
            (3.5, ): 38.48451000647496,
            (2, 5): 10,
            (10, 20): 200,
            (2.1, 2.5): 5.25,
            (3, 4, 5): 6.0,
            (3, 4, 6): 5.332682251925386,
            (2, 2, 2): 1.7320508075688772
        }

        for key in mock_data:
            self.assertEqual(ac.calculate_area(*key), mock_data[key])

# тест прямоугольный ли треугольник
    def test_is_right(self):
        mock_data = {
            (3, 4, 5): True,
            (2, 2, 2): False
        }

        for key in mock_data:
            self.assertEqual(ac.Triangle([*key]).is_right(), mock_data[key])

# тест на существование такого треугольника
    def test_is_triangle(self):
        mock_data = [
            (12, 1, 1),
            (13, -1, 1)
        ]

        for params in mock_data:
            with self.assertRaises(ValueError):
                ac.calculate_area(*params)
                

# проверка на существование этой фигуры в area_calculator
    def test_no_shape(self):
        params = [
            (1, 1, 1, 1, 1),
            (5, 1, 2, 4)
        ]


        for param in params:
            with self.assertRaises(Exception):
                ac.calculate_area(*param)


if __name__ == "__main__":
    unittest.main()