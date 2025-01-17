import unittest
from emotion_detection import emotion_detector

dict_test = {'I am glad this happened':'joy',
            'I am really mad about this':'anger',
            'I feel disgusted just hearing about this':'disgust',
            'I am so sad about this':'sadness',
            'I am really afraid that this will happen':'fear'
            }

class TestMyModule(unittest.TestCase):
    def test_emotion_detector(self):
        for test_case in dict_test.keys():
            self.assertEqual(emotion_detector(test_case)['dominant_emotion'], dict_test[test_case])

if __name__ == '__main__':
    unittest.main()