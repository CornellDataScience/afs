import unittest
import json
import time



class TestFileMethods(unittest.TestCase):
    with open('parameter.json') as f:
        data = json.load(f)
    HEADER_LENGTH = data['HEADER_LENGTH']
    IP = data["IP"]
    PORT = data['PORT']
    TIME_OUT = data['TIME_OUT']


    def test_header(self):
        t_end = time.time() + 60 * TIME_OUT
        while time.time() < t_end:
            # test whether the header is correct

    def test_message(self):
        t_end = time.time() + 60 * TIME_OUT
        while time.time() < t_end:
        #test whether the message was sent correctly

    def test_split(self):
       

if __name__ == '__main__':
    unittest.main()
