import requests
import graphene
from graphene import relay

ACTORS_ENDPOINT = 'http://127.0.0.1:8000/api/actors/{id}/'
ALL_ACTORS_ENDPOINT = 'http://127.0.0.1:8000/api/actors/'


class Actor(graphene.ObjectType):

    first_name = graphene.String()
    last_name = graphene.String()
    age = graphene.Int()
    rating = graphene.Int()

    class Meta:
        interfaces = (relay.Node, )

    @classmethod
    def get_node(cls, id, context, info):
        response = requests.get(ACTORS_ENDPOINT.format(id=id))
        data = response.json()
        return Actor.create_from_data(data, id)

    @classmethod
    def create_from_data(cls, data, id_):
        return cls(
            id=id_,
            first_name=data['first_name'],
            last_name=data['last_name'],
            age=data['age'],
            rating=data['rating'],
        )


class Query(graphene.AbstractType):
    actor = graphene.relay.Node.Field(Actor)
    actors = graphene.List(Actor)

    def resolve_actors(self, args, context, info):
        response = requests.get(ALL_ACTORS_ENDPOINT)
        data = response.json()
        return [Actor.create_from_data(actor, actor['id']) for actor in data]


class CreateActor(relay.ClientIDMutation):

    class Input:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        age = graphene.Int(required=True)
        rating = graphene.Int(required=True)

    actor = graphene.Field(Actor)
    
    @classmethod
    def mutate_and_get_payload(cls, args, context, info):
        data_to_sent = {
            'first_name': args['first_name'],
            'last_name': args['last_name'],
            'age': args['age'],
            'rating': args['rating'],
        }
        response = requests.post(ALL_ACTORS_ENDPOINT, data=data_to_sent)
        data_from_server = response.json()
        actor = Actor.create_from_data(data_from_server, data_from_server['id'])
        return CreateActor(actor=actor)


class Mutation(graphene.AbstractType):
    create_actor = CreateActor.Field()
