class Practise():
    def __init__(self, question):
        """Stores a question, and prepare to store responses."""

        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""

        print(self.question)

    def store_response(self):
        """Store a single response to the survey"""

        response = input("Language: ")
        self.responses.append(new_response)

    def show_result(self):
        """Show all the responses given"""

        print("Survey result")
        for response in self.responses:
            print('- ' + response)
