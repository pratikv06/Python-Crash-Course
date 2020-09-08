import unittest
from module1_name_formatting import get_formatted_name2

class NameTestCase(unittest.TestCase):
    '''Test for 'module1_name_formatting.py'.'''

    def test_first_last_name(self):
        '''Do names like 'Pratik Vishwakarma' work?'''
        formatted_name = get_formatted_name2('pratik', 'vishwakarma')
        self.assertEqual(formatted_name, 'Pratik Vishwakarma')

    # both method name is same, thats why only one method is executed
    def test_first_last_name(self):
        '''Do names like 'Pratik Vishwakarma' work?'''
        formatted_name = get_formatted_name2('pratik', 'vishwakarma')
        self.assertEqual(formatted_name, 'Pratik Vishwakarma')


    
unittest.main()



# Note:
# Output:
# 1. firstline - E , represent the Error in test case
# 2. secondline - method that cause error
# 3. thirdline - trackback to error
# 4. fourthline - total test run
# 5. lastline - Falied [number of error]
