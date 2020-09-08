'''
If test case fail,
don't change the testcase, instead fix the code that caused the error
'''
import unittest
from module1_name_formatting import get_formatted_name3

class NameTestCase(unittest.TestCase):
    '''Test for 'module1_name_formatting.py'.'''

    def test_first_last_name(self):
        '''Do names like 'Pratik Vishwakarma' work?'''
        formatted_name = get_formatted_name3('pratik', 'vishwakarma')
        self.assertEqual(formatted_name, 'Pratik Vishwakarma')

    
    # Adding new method for middle name
    def test_first_last_middle_name(self):
        '''Do names like 'Nilesh Suresh Yadav' work?'''
        formatted_name = get_formatted_name3('nilesh', 'yadav', 'suresh')
        self.assertEqual(formatted_name, 'Nilesh Suresh Yadav')


    
unittest.main()


'''
Assert Method available in unittest.TestCase Module
1. assertEqual(a, b)        - a==b 
2. assertNotEqual(a, b)     - a!=b
3. assertTrue(a)            - a is True
4. assertFalse(a)           - a is False
5. assertIn(item, list)     - item is in list
6. assertNotIn(item, list)  - item is not in list
'''