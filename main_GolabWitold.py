import resourceChecker_GolabWitold as rc
import unittest

class testResource(unittest.TestCase):
    def test_single_asterisk_file(self):
        self.assertEqual(rc.checkResourceFieldInJsonFile("data_single_asterisk_GolabWitold.json"), False)
    def test_single_dot_file(self):
        self.assertEqual(rc.checkResourceFieldInJsonFile("data_single_dot_GolabWitold.json"), False)
    def test_wrong_policy(self):
        self.assertEqual(rc.checkResourceFieldInJsonFile("data_wrong_policy_GolabWitold.json"), False)
    def test_no_file(self):
        self.assertEqual(rc.checkResourceFieldInJsonFile("data_file_does_not_exist.json"), False)

print("This method will return False if JSON Resource field contains a single asterisk and True in any other case.")
print("This method returned:", rc.checkResourceFieldInJsonFile("data_single_asterisk_GolabWitold.json"))

unittest.main()