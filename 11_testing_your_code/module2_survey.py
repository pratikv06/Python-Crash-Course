class AnonymousSurvey():
    '''colleect anonymous answers to a survey questions'''

    def __init__(self, question):
        '''store a question, and prepare to store a response'''
        self.question = question
        self.responses = []

    def show_question(self):
        '''show the survey question'''
        print(self.question)

    def store_reponse(self, new_response):
        '''store a single response to the survey'''
        self.responses.append(new_response)

    def show_responses(self):
        '''show all the responses that have been given'''
        print("Survey Result:")
        for response in self.responses:
            print(response)