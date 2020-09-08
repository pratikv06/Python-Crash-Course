'''
Unit Test: verifies one specific aspect of a functions behaviour is correct.
Test Case: collection od unit test that together prove that a function 
           behavesas it suppose to.
'''

# Text case with one method
# create a class that inherit unittest.TestCase

import unittest
from module1_name_formatting import get_formatted_name

class NameTestCase(unittest.TestCase):
    '''Test for 'module1_name_formatting.py'.'''

    def test_first_last_name(self):
        ''' Passing Test Case
        Do names like 'Pratik Vishwakarma' work?'''
        formatted_name = get_formatted_name('pratik', 'vishwakarma')
        self.assertEqual(formatted_name, 'Pratik Vishwakarma')



    
unittest.main()



# Note:
# 1. Any method start with 'test_' will run automatically
# 2. Assert method - compare expected result with output of the function
# 
# Output:
# 1. firstline - dot [.], represent the pass test case
# 2. secondline - total number of test case runs
# 3. Lastline - 'ok' all testcase pass
