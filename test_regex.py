from unittest import TestCase
from regex import RegexFSM
import re


class TestRegexFSM(TestCase):


    def test_simple_pattern0(self):
        pattern = "a"
        fsm = RegexFSM(pattern)
        test_string = "a"
        result = fsm.check_string(test_string)
        self.assertTrue(result, f"Expected True for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)

    def test_simplest_pattern0(self):
        pattern = "a"
        fsm = RegexFSM(pattern)
        test_string = "b"
        result = fsm.check_string(test_string)
        self.assertFalse(result, f"Expected False for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)
    def test_simplest_pattern1(self):
        pattern = "a"
        fsm = RegexFSM(pattern)
        test_string = "aa"
        result = fsm.check_string(test_string)
        self.assertTrue(result, f"Expected True for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)
    def test_simplest_pattern2(self):
        pattern = "a"
        fsm = RegexFSM(pattern)
        test_string = "baa"
        result = fsm.check_string(test_string)
        self.assertFalse(result, f"Expected False for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)


    def test_simple_pattern1(self):
        pattern = "a*b"
        fsm = RegexFSM(pattern)
        test_string = "aaab"
        result = fsm.check_string(test_string)
        self.assertTrue(result, f"Expected True for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)


    def test_no_match(self):
        pattern = "a*b"
        fsm = RegexFSM(pattern)
        test_string = "aaac"
        result = fsm.check_string(test_string)
        self.assertFalse(result, f"Expected False for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)

    def test_complex_pattern1_1(self):
        pattern = "a*b.c+"
        fsm = RegexFSM(pattern)
        test_string = "aaabxc"
        result = fsm.check_string(test_string)
        self.assertTrue(result, f"Expected True for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)
    def test_complex_pattern1_2(self):
        pattern = "a*b.c+"
        fsm = RegexFSM(pattern)
        test_string = "aaabxccx"
        result = fsm.check_string(test_string)
        self.assertTrue(result, f"Expected True for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)

    def test_stars_pattern1_1(self):
        pattern = "a*a*a*"
        fsm = RegexFSM(pattern)
        test_string = "aaaa"
        result = fsm.check_string(test_string)
        self.assertTrue(result, f"Expected True for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)
    def test_stars_pattern1_2(self):
        pattern = "a*a*a*"
        fsm = RegexFSM(pattern)
        test_string = "bbbbb"
        result = fsm.check_string(test_string)
        self.assertTrue(result, f"Expected True for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)
    def test_plus_pattern1_1(self):
        pattern = "a+b+c+"
        fsm = RegexFSM(pattern)
        test_string = "aaabbbccc"
        result = fsm.check_string(test_string)
        self.assertTrue(result, f"Expected True for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)
    def test_plus_pattern1_1_no_match(self):
        pattern = "a+b+c+"
        fsm = RegexFSM(pattern)
        test_string = "aaacc"
        result = fsm.check_string(test_string)
        self.assertFalse(result, f"Expected False for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)

    def test_plus_pattern1_2(self):
        pattern = "a+kb+c+"
        fsm = RegexFSM(pattern)
        test_string = "akbbbccccccckaskd"
        result = fsm.check_string(test_string)
        self.assertTrue(result, f"Expected True for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)

    def test_dot_pattern1_1(self):
        pattern = "a*b.+ch+"
        fsm = RegexFSM(pattern)
        test_string = "aaabxccchhhhasd"
        result = fsm.check_string(test_string)
        self.assertTrue(result, f"Expected True for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)

    def test_dot_pattern1_1_no_match(self):
        pattern = "a*b.+ch+"
        fsm = RegexFSM(pattern)
        test_string = "aaabxxxxhhhhasd"
        result = fsm.check_string(test_string)
        self.assertFalse(result, f"Expected False for pattern '{pattern}' and string '{test_string}'")
        self.assertEqual(result, re.match(pattern, test_string) is not None)

if __name__ == "__main__":
    import unittest
    unittest.main()