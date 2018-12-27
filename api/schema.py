import graphene
from graphene import relay

class HelloWorld(graphene.ObjectType):
    hello = graphene.String(argument=graphene.String(default_value="World!"))

    def resolve_hello(self, info, argument):
        return 'Hello ' + argument

class HelloWorldConnection(relay.Connection):
    class Meta:
        node = HelloWorld

class Query(graphene.ObjectType):
    node = relay.Node.Field()
    hello_world = relay.ConnectionField(HelloWorldConnection)

schema = graphene.Schema(query=Query)
hello_world_schema = graphene.Schema(query=HelloWorld)
