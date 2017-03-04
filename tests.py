import unittest
import BMLib


class TestBoxMaker(unittest.TestCase):

    def test_genHorizontalLinePoints(self):
        expected = [
            (0, 0),
            (4, 0),
            (4, 1),
            (8, 1),
            (8, 0),
            (12, 0),
            (12, 1),
            (16, 1),
            (16, 0),
        ]
        actual = list(BMLib.genHorizontalLinePoints(0, 0, 20, 1, 0))
        self.assertEquals(expected, actual)

    def test_genFrontPoints(self):
        expected = [
            (1.0, 1.0),
            (4.0, 1.0),
            (4.0, 0.0),
            (8.0, 0.0),
            (8.0, 1.0),
            (11.0, 1.0),
            (11.0, 4.0),
            (12.0, 4.0),
            (12.0, 8.0),
            (11.0, 8.0),
            (11.0, 11.0),
            (8.0, 11.0),
            (8.0, 12.0),
            (4.0, 12.0),
            (4.0, 11.0),
            (1.0, 11.0),
            (1.0, 8.0),
            (0.0, 8.0),
            (0.0, 4.0),
            (1.0, 4.0),
        ]
        actual = list(BMLib.genFrontPoints(12, 12, 12, 1))
        self.assertEquals(expected, actual)

    def test_genBackPoints(self):
        expected = [
            (0, 0),
            (4, 0),
            (4, 1),
            (8, 1),
            (8, 0),
            (12, 0),
            (12, 4),
            (11, 4),
            (11, 8),
            (12, 8),
            (12, 11),
            (8, 11),
            (8, 12),
            (4, 12),
            (4, 11),
            (0, 11),
            (0, 8),
            (1, 8),
            (1, 4),
            (0, 4),
        ]
        actual = list(BMLib.genBackPoints(12, 12, 12, 1))
        self.assertEquals(expected, actual)

    def test_genLeftPoints(self):
        expected = [
            (-1, 0),
            (-4, 0),
            (-4, 1),
            (-8, 1),
            (-8, 0),
            (-11, 0),
            (-11, 4),
            (-12, 4),
            (-12, 8),
            (-11, 8),
            (-11, 11),
            (-8, 11),
            (-8, 12),
            (-4, 12),
            (-4, 11),
            (-1, 11),
            (-1, 8),
            (0, 8),
            (0, 4),
            (-1, 4),
        ]
        actual = list(BMLib.genLeftPoints(12, 12, 12, 1))
        self.assertEquals(expected, actual)

    def test_genRightPoints(self):
        expected = [
            (-1, 0),
            (-4, 0),
            (-4, 1),
            (-8, 1),
            (-8, 0),
            (-11, 0),
            (-11, 4),
            (-12, 4),
            (-12, 8),
            (-11, 8),
            (-11, 11),
            (-8, 11),
            (-8, 12),
            (-4, 12),
            (-4, 11),
            (-1, 11),
            (-1, 8),
            (0, 8),
            (0, 4),
            (-1, 4),
        ]
        actual = list(BMLib.genRightPoints(12, 12, 12, 1))
        self.assertEquals(expected, actual)

    def test_genBottomPoints(self):
        expected = [
            (1, -1),
            (4, -1),
            (4, 0),
            (8, 0),
            (8, -1),
            (11, -1),
            (11, -4),
            (12, -4),
            (12, -8),
            (11, -8),
            (11, -11),
            (8, -11),
            (8, -12),
            (4, -12),
            (4, -11),
            (1, -11),
            (1, -8),
            (0, -8),
            (0, -4),
            (1, -4),
        ]
        actual = list(BMLib.genBottomPoints(12, 12, 12, 1))
        self.assertEquals(expected, actual)

    def test_genTopPoints(self):
        expected = [
            (0, 0),
            (4, 0),
            (4, -1),
            (8, -1),
            (8, 0),
            (12, 0),
            (12, -4),
            (11, -4),
            (11, -8),
            (12, -8),
            (12, -12),
            (8, -12),
            (8, -11),
            (4, -11),
            (4, -12),
            (0, -12),
            (0, -8),
            (1, -8),
            (1, -4),
            (0, -4),
        ]
        actual = list(BMLib.genTopPoints(12, 12, 12, 1))
        self.assertEquals(expected, actual)
