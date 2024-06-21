import unittest
from trailRun import append_dict


class TestTrailRun(unittest.TestCase):

    def setUp(self):
        self.dictionary = {
            'name': [],
            'result_info': [],
            'starting_at': []
        }

        self.mock_list_data = [
            {'id': 216268, 'name': 'Esbjerg vs OB', 'starting_at': '2006-03-25 16:00:00', 'result_info': 'Esbjerg won after full-time.'},
            {'id': 216269, 'name': 'AaB vs København', 'starting_at': '2005-11-27 16:30:00', 'result_info': 'FC Copenhagen won after full-time.'}
        ]

    def test_appending_to_dictionary(self):
        emptyDict = {
            'name': [],
            'result_info': [],
            'starting_at': []
        }
        self.assertEqual(self.dictionary, emptyDict)
        
        append_dict(self.dictionary, self.mock_list_data)  # Call the function directly
        
        filledDict = {
            'name': ['Esbjerg vs OB', 'AaB vs København'],
            'result_info': ['Esbjerg won after full-time.', 'FC Copenhagen won after full-time.'],
            'starting_at': ['2006-03-25 16:00:00', '2005-11-27 16:30:00']
        }
        self.assertEqual(self.dictionary, filledDict)


if __name__ == '__main__':
    unittest.main()
