from flask import Flask, jsonify, make_response
from flask_graphql import GraphQLView
import graphene

app = Flask(__name__)

class Query(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value="World!"))

    def resolve_hello(self, info, argument):
        return 'Hello ' + argument

schema = graphene.Schema(query=Query)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

@app.route('/')
def hello_world():
    result = schema.execute('{ hello }')
    return result.data['hello']

@app.route('/restapi')
def restapi():
    result = { "greeting": "Hellow World!" }
    return make_response(jsonify(result))

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
