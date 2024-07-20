import unittest
from area import area_heron, area_circle

class TestArea(unittest.TestCase):

    # test of normal function of area_circle
    def test_circle(self):
        self.assertEqual(area_circle(5), 78.53750000000001)

    # test of normal function of test_heron
    def test_heron(self):
        self.assertEqual(area_heron(3,4,5),(6.0, True))

        # test of normal function of test_heron with not right triangle
    def test_heron_rt(self):
            self.assertEqual(area_heron(6, 7, 11), (18.973665961010276, False))

    # test if value is not number
    def test_heron_wv(self):
        self.assertEqual(area_heron("a",4,5),"Error. Value is not integer or float")

    # test if triangle doesnt exist
    def test_heron_te(self):
        self.assertEqual(area_heron(15,4,5), "Error. This Triangle doesnt exist")


if __name__ == "__main__":
  unittest.main()