import unittest
from datetime import date

from src.entity.Collecte import Collecte


class CollecteTest(unittest.TestCase):
    collecteToTest = Collecte(4, 1, date(21, 4, 2001), 2)

    def test_Type(self):
        self.assertIsInstance(self.collecteToTest, Collecte)

    def testAffectationValue(self):
        self.assertEqual(self.collecteToTest.id, 4)
        self.assertEqual(self.collecteToTest.idJardin, 1)
        self.assertEqual(self.collecteToTest.date, date(21, 4, 2001))
        self.assertEqual(self.collecteToTest.nombreMaxEtudiants, 2)

    def testEditionValue(self):
        self.collecteToTest.nombreMaxEtudiants = 5
        self.assertNotEqual(self.collecteToTest.nombreMaxEtudiants, 2)
        self.assertEqual(self.collecteToTest.nombreMaxEtudiants, 5)


if __name__ == '__main__':
    unittest.main()
