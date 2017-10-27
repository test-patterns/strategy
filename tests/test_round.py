""" Sample problem featuring the strategy pattern. """

import unittest

from test_context import Round

class TestRound(unittest.TestCase):
    """ Tests the Round class """

    def test_init(self):
        """ Tests the constructor of the Round class """
        test_round = Round(8)
        self.assertEqual(test_round.get_amount(), 4.4466919372480005)

if __name__ == '__main__':
    unittest.main()
