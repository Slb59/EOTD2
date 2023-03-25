import unittest
from eotd2.models import Zombi, Zombis

class Test_Zombis(unittest.TestCase):
    def test_select(self):
        # GIVEN
        zombis = Zombis()
        # WHEN
        zombi = zombis.select()
        # THEN
        self.assertEqual(isinstance(zombi,Zombi),True)

if __name__ == '__main__':
    unittest.main()