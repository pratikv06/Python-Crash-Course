from module2_survey import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()

print("Enter 'q' to quit the survey.\n")
while True:
    response = input(">> Langugage - ")
    if response.lower() == 'q':
        break
    my_survey.store_reponse(response)


print("Thank you for taking the survey")
my_survey.show_responses()