import unittest
from module2_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''Test for the class AnonymousSurvey'''

    def setUp(self):
        '''Create a survey and a set a responses for all test modules'''
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Hindi', 'Marathi']

    def test_store_single_response(self):
        '''test that a single response is stored properly'''
        self.my_survey.store_reponse(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        '''test that a three response is stored properly'''
        for response in self.responses:
            self.my_survey.store_reponse(response)
        
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


unittest.main()


# Note:
# setUp()
# run before all the test_ method
# if we create object or variable in setup method 
# it will be available to all the test_ method