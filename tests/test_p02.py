import io
import unittest
import unittest.mock

from p02 import print_depth, person_b


class TestProblem02(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, data, expected_output, mock_stdout):
        print_depth(data)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_01(self):

        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": person_b,
                    "key6": {
                        "key7": 4
                    }
                }
            }
        }

        self.assert_stdout(a, 'key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nuser: 3\nfirst_name: 4\nlast_name: 4\n'
                           + 'father: 4\nfirst_name: 5\nlast_name: 5\nfather: 5\nkey6 3\nkey7 4\n')

    def test_02(self):
        a = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }
        self.assert_stdout(a, 'key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\n')

    def test_03(self):
        a = {
            "key1": 1,
            "key2": 2,
            "key3": {
                "key4": 3
            }
        }

        self.assert_stdout(a, 'key1 1\nkey2 1\nkey3 1\nkey4 2\n')


if __name__ == '__main__':
    unittest.main()
