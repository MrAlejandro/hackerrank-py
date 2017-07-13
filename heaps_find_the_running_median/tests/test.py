import unittest
from solution import *

class HeapsSolutionTests(unittest.TestCase):

    def test_find_mid_index(self):
        lst = []
        self.assertEqual(find_mid_index(lst, None, None), None)

        # odd items number
        lst1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        self.assertEqual(find_mid_index(lst1, None, None), 7)

        self.assertEqual(find_mid_index(lst1, None, 100), 7)
        self.assertEqual(find_mid_index(lst1, None, 14), 7)
        self.assertEqual(find_mid_index(lst1, None, 10), 5)
        self.assertEqual(find_mid_index(lst1, None, 6), 3)
        self.assertEqual(find_mid_index(lst1, None, 5), 2)
        self.assertEqual(find_mid_index(lst1, None, 4), 2)
        self.assertEqual(find_mid_index(lst1, None, 3), 1)
        self.assertEqual(find_mid_index(lst1, None, 2), 1)
        self.assertEqual(find_mid_index(lst1, None, 1), 0)
        self.assertEqual(find_mid_index(lst1, None, 0), 0)

        self.assertEqual(find_mid_index(lst1, 100, None), 14)
        self.assertEqual(find_mid_index(lst1, 14, None), 14)
        self.assertEqual(find_mid_index(lst1, 13, None), 13)
        self.assertEqual(find_mid_index(lst1, 12, None), 13)
        self.assertEqual(find_mid_index(lst1, 11, None), 12)
        self.assertEqual(find_mid_index(lst1, 10, None), 12)

        lst2 = [1]
        self.assertEqual(find_mid_index(lst2, None, None), 0)
        # end odd items number

        # even items number
        lst3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
        self.assertEqual(find_mid_index(lst3, None, None), 6)
        self.assertEqual(find_mid_index(lst3, None, 100), 6)
        self.assertEqual(find_mid_index(lst3, None, 13), 6)
        self.assertEqual(find_mid_index(lst3, None, 12), 6)
        self.assertEqual(find_mid_index(lst3, None, 11), 5)
        self.assertEqual(find_mid_index(lst3, None, 10), 5)
        self.assertEqual(find_mid_index(lst3, None, 9), 4)
        self.assertEqual(find_mid_index(lst3, None, 8), 4)
        self.assertEqual(find_mid_index(lst3, None, 7), 3)
        self.assertEqual(find_mid_index(lst3, None, 6), 3)

        lst4 = [1,2]
        self.assertEqual(find_mid_index(lst4, None, None), 0)
        self.assertEqual(find_mid_index(lst4, None, 15), 0)
        self.assertEqual(find_mid_index(lst4, None, 1), 0)
        self.assertEqual(find_mid_index(lst4, None, 0), 0)
        # end even items number

    def test_get_list_size(self):
        lst1 = [1,2,3,4,5]
        lst2 = [1,2,3]
        self.assertEqual(get_list_size(lst1), 5)
        self.assertEqual(get_list_size(lst2), 3)

    def test_list_has_even_items(self):
        lst1 = [1,2,3,5]
        lst2 = [1,2,3]
        self.assertTrue(list_has_even_items(lst1));
        self.assertFalse(list_has_even_items(lst2));


if __name__ == '__main__':
    unittest.main()
