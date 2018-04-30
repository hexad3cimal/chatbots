from chatterbot import ChatBot
from flask import Flask,make_response
from flask_restful import Resource, Api


# Create a new chat bot named Charlie
chatbot = ChatBot(
    'Charlie',
    logic_adapters=[
        {
            'import_path': 'chat.MyLogicAdapter'
        }
    ])



app = Flask(__name__)
api = Api(app)

class Accounts(Resource):
    def get(self):

        return "{"+str(chatbot.get_response('get all from 2016-08-16 to 2018-04-30'))+"}"

api.add_resource(Accounts, '/')

if __name__ == '__main__':
    app.run(debug=True)

