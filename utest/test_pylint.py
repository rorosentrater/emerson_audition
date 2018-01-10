from unittest import TestCase
from pylint.lint import Run as Test


class LintTest(TestCase):

    def test_library(self):
        with self.assertRaises(SystemExit) as lint_check:
            Test(['library'])

        self.assertEqual(lint_check.exception.code, 0)

    def test_atest(self):
        with self.assertRaises(SystemExit) as lint_check:
            Test(['atest'])

        self.assertEqual(lint_check.exception.code, 0)

    def test_utest(self):
        with self.assertRaises(SystemExit) as lint_check:
            Test(['utest'])

        self.assertEqual(lint_check.exception.code, 0)
