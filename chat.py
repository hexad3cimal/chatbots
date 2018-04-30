from chatterbot.logic import LogicAdapter


class MyLogicAdapter(LogicAdapter):
    def __init__(self, **kwargs):
        super(MyLogicAdapter, self).__init__(**kwargs)

    def can_process(self, statement):
        return True

    def process(self, statement):
        from chatterbot.conversation import Statement
        import requests
        confidence = 0
        listOfWords = statement.text.split()

        # Make a request to the temperature API
        if(("all" in statement.text) and ("from" in statement.text) and "to" in statement.text):
            response = requests.get('http://localhost:8080/accounts/all=all/'+listOfWords[listOfWords.index("from") + 1]
                                    + "=" + listOfWords[listOfWords.index("to") + 1])
            data = response.json()

        elif(("all" in statement.text) and ("from" in statement.text)):
            response = requests.get(
                'http://localhost:8080/accounts/all=all/' + listOfWords[listOfWords.index("from") + 1]
                + "=")
            data = response.json()

        elif("account-no" in statement.text and "from" in statement.text and "to" in statement.text):
            response = requests.get(
                'http://localhost:8080/accounts/acc='+ listOfWords[listOfWords.index("account-no") + 1]+ "/"+ listOfWords[listOfWords.index("from") + 1]
                + "=" + listOfWords[listOfWords.index("to") + 1])
            data = response.json()

        # Let's base the confidence value on if the request was successful
        if response.status_code == 200:
            confidence = 1

        response_statement = Statement(data)
        response_statement.confidence = confidence
        return response_statement
