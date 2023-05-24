import unittest
from src.entity.User import User


class UserTest(unittest.TestCase):
    userToTest = User(4, "testNom", "testPrenom", "testMail@gmail.com", "testLogin", "testPassword", "testAdresse",
                      "testTypeUser")

    def testType(self):
        self.assertIsInstance(self.userToTest, User)

    def testAffectationValue(self):
        self.userToTest = User(4, "testNom", "testPrenom", "testMail@gmail.com", "testLogin", "testPassword",
                               "testAdresse", "testTypeUser")
        self.assertEqual(self.userToTest.id, 4)
        self.assertEqual(self.userToTest.nom, "testNom")
        self.assertEqual(self.userToTest.prenom, "testPrenom")
        self.assertEqual(self.userToTest.mail, "testMail@gmail.com")
        self.assertEqual(self.userToTest.login, "testLogin")
        self.assertEqual(self.userToTest.password, "testPassword")
        self.assertEqual(self.userToTest.adresse, "testAdresse")
        self.assertEqual(self.userToTest.typeUser, "testTypeUser")

    def testEditionValue(self):
        self.userToTest.typeUser = "newEditedValue"
        self.assertNotEqual(self.userToTest.typeUser, "testTypeUser")
        self.assertEqual(self.userToTest.typeUser, "newEditedValue")


if __name__ == '__main__':
    unittest.main()
