from unittest import TestCase
from pylint.lint import Run as Test


class LintTest(TestCase):

    def setUp(self):
        disabled_rules = (
            'missing-docstring',
            'no-self-use',
            'relative-import',
            'no-member',
            'duplicate-code',
            'unused-import'
        )
        self.default_filter = '--disable={rules}'.format(rules=','.join(disabled_rules))

    def test_library(self):
        with self.assertRaises(SystemExit) as lint_check:
            Test([self.default_filter, 'library'])

            self.assertEqual(lint_check.exception.code, 0)

    def test_tests(self):
        with self.assertRaises(SystemExit) as lint_check:
            Test(['--errors-only', 'atest'])

        self.assertEqual(lint_check.exception.code, 0)
