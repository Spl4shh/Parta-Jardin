import unittest

from src.entity.ProduitDisponible import ProduitDisponible


class ProduitDisponibleTest(unittest.TestCase):
    produitDisponibleToTest = ProduitDisponible(4, 1, "testProduit", 1)

    def test_Type(self):
        self.assertIsInstance(self.produitDisponibleToTest, ProduitDisponible)

    def testAffectationValue(self):
        self.assertEqual(self.produitDisponibleToTest.id, 4)
        self.assertEqual(self.produitDisponibleToTest.idJardin, 1)
        self.assertEqual(self.produitDisponibleToTest.produit, "testProduit")
        self.assertEqual(self.produitDisponibleToTest.quantite, 1)


    def testEditionValue(self):
        self.produitDisponibleToTest.quantite = "newEditedValue"
        self.assertNotEqual(self.produitDisponibleToTest.quantite, "testQuantite 1kg")
        self.assertEqual(self.produitDisponibleToTest.quantite, "newEditedValue")


if __name__ == '__main__':
    unittest.main()
