import unittest
import BMLib


class TestBoxMaker(unittest.TestCase):

    def test_genHorizontalLinePoints(self):
        expected = [
            (0, 0),
            (5, 0),
            (5, 1),
            (10, 1),
            (10, 0),
            (15, 0),
            (15, 1),
            (20, 1),
            (20, 0),
        ]
        actual = list(BMLib.genHorizontalLinePoints(0, 0, 5, 5, 1, 0))
        self.assertEquals(expected, actual)

    def test_genFrontPoints(self):
        expected = [
            (0, 0),
            (4, 0),
            (4, 1),
            (7, 0),
            (7, 3),
            (8, 3),
            (7, 5),
            (4, 5),
            (4, 6),
            (0, 5),
            (0, 3),
            (1, 3),
        ]
        actual = list(BMLib.genFrontPoints(8, 6, 4, 1, 2))
        self.assertEquals(expected, actual)

    def test_genBackPoints(self):
        expected = [
            (0, 0),
            (4, 0),
            (4, 1),
            (7, 0),
            (7, 3),
            (8, 3),
            (7, 5),
            (4, 5),
            (4, 6),
            (0, 5),
            (0, 3),
            (1, 3),
        ]
        actual = list(BMLib.genBackPoints(8, 6, 4, 1, 2))
        self.assertEquals(expected, actual)

    def test_genLeftPoints(self):
        expected = [
            (-1, 0),
            (-2, 0),
            (-2, 1),
            (-3, 0),
            (-3, 3),
            (-4, 3),
            (-3, 5),
            (-2, 5),
            (-2, 6),
            (-1, 5),
            (-1, 3),
            (0, 3),
        ]
        actual = list(BMLib.genLeftPoints(8, 6, 4, 1, 2))
        self.assertEquals(expected, actual)

    def test_genRightPoints(self):
        expected = [
            (0, 0),
            (-2, 0),
            (-2, 1),
            (-4, 0),
            (-4, 3),
            (-3, 3),
            (-4, 5),
            (-2, 5),
            (-2, 6),
            (0, 5),
            (0, 3),
            (-1, 3),
        ]
        actual = list(BMLib.genRightPoints(8, 6, 4, 1, 2))
        self.assertEquals(expected, actual)

    def test_genBottomPoints(self):
        expected = [
            (1, -1),
            (4, -1),
            (4, 0),
            (7, -1),
            (7, -2),
            (8, -2),
            (7, -3),
            (4, -3),
            (4, -4),
            (1, -3),
            (1, -2),
            (0, -2),
        ]
        actual = list(BMLib.genBottomPoints(8, 6, 4, 1, 2))
        self.assertEquals(expected, actual)

    def test_genTopPoints(self):
        expected = [
            (0, 0),
            (4, 0),
            (4, -1),
            (8, 0),
            (8, -2),
            (7, -2),
            (8, -4),
            (4, -4),
            (4, -3),
            (0, -4),
            (0, -2),
            (1, -2),
        ]
        actual = list(BMLib.genTopPoints(8, 6, 4, 1, 2))
        self.assertEquals(expected, actual)
