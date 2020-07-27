import io
import unittest
import unittest.mock

from p01 import print_depth


class TestProblem01(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, data, expected_output, mock_stdout):
        print_depth(data)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test01(self):
        a = {
            "key1": 1,
            "key2": 2,
            "key3": {
                "key4": 3
            }
        }
        self.assert_stdout(a, 'key1 1\nkey2 1\nkey3 1\nkey4 2\n')

    def test02(self):
        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }
        self.assert_stdout(a, "key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\n")


if __name__ == '__main__':
    unittest.main()
