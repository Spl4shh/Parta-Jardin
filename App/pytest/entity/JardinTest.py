import unittest
from src.entity.Jardin import Jardin


class JardinTest(unittest.TestCase):
    jardinToTest = Jardin(4, 1, "testDescription", "testRue, 99999 TestVille", "testLinkImage")

    def testType(self):
        self.assertIsInstance(self.jardinToTest, Jardin)

    def testAffectationValue(self):
        self.assertEqual(self.jardinToTest.id, 4)
        self.assertEqual(self.jardinToTest.idProprietaire, 1)
        self.assertEqual(self.jardinToTest.description, "testDescription")
        self.assertEqual(self.jardinToTest.adresseJardin, "testRue, 99999 TestVille")
        self.assertEqual(self.jardinToTest.image, "testLinkImage")


    def testEditionValue(self):
        self.jardinToTest.description = "newEditedValue"
        self.assertNotEqual(self.jardinToTest.description, "testDescription")
        self.assertEqual(self.jardinToTest.description, "newEditedValue")


if __name__ == '__main__':
    unittest.main()
