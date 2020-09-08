import unittest
from module2_survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    '''Test for the class AnonymousSurvey'''

    def test_store_single_response(self):
        '''test that a single response is stored properly'''
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_reponse('English')
        self.assertIn('English', my_survey.responses)

    def test_store_three_response(self):
        '''test that a three response is stored properly'''
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Hindi', 'Marathi']
        for response in responses:
            my_survey.store_reponse(response)
        
        for response in responses:
            self.assertIn(response, my_survey.responses)


unittest.main()