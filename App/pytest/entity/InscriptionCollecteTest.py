import unittest

from src.entity.InscriptionCollecte import InscriptionCollecte


class InscriptionCollecteTest(unittest.TestCase):
    inscriptionCollecteToTest = InscriptionCollecte(4, 1)

    def testType(self):
        self.assertIsInstance(self.inscriptionCollecteToTest, InscriptionCollecte)

    def testAffectationValue(self):
        self.assertEqual(self.inscriptionCollecteToTest.idCollecte, 4)
        self.assertEqual(self.inscriptionCollecteToTest.idEtudiant, 1)

    def testEditionValue(self):
        self.inscriptionCollecteToTest.idEtudiant = 5
        self.assertNotEqual(self.inscriptionCollecteToTest.idEtudiant, 2)
        self.assertEqual(self.inscriptionCollecteToTest.idEtudiant, 5)


if __name__ == '__main__':
    unittest.main()
