import requests
import arrow
import graphene
from graphene import relay
from graphene.types import datetime as graphene_datetime
from graphql_relay.node.node import from_global_id, to_global_id

from film_database.actors.schema import Actor

FILMS_ENDPOINT = 'http://127.0.0.1:8000/api/films/{id}/'
ALL_FILMS_ENDPOINT = 'http://127.0.0.1:8000/api/films/'


class Film(graphene.ObjectType):

    class Meta:
        interfaces = (relay.Node, )

    title = graphene.String()
    actors = graphene.List(Actor, description='List of actors that play in the film')    
    air_date = graphene_datetime.DateTime()
    rating = graphene.Int()

    @classmethod
    def create_from_data(cls, data, id_):
        return cls(
            id=id_,
            title=data['title'],
            air_date=arrow.get(data['air_date']).date(),
            rating=data['rating'],
        )


    @classmethod
    def get_node(cls, id, context, info):
        response = requests.get(FILMS_ENDPOINT.format(id=id))
        data = response.json()
        return Film.create_from_data(data, id)

    def resolve_actors(self, args, context, info):
        response = requests.get(FILMS_ENDPOINT.format(id=self.id))
        data = response.json()
        return [relay.Node.get_node_from_global_id(
            to_global_id('Actor', actor_id),
            context,
            info
        ) for actor_id in data['actors']]


class Query(graphene.AbstractType):
    film = graphene.relay.Node.Field(Film)
    films = graphene.List(Film)

    def resolve_films(self, args, context, info):
        response = requests.get(ALL_FILMS_ENDPOINT)
        data = response.json()
        return [Film.create_from_data(film, film['id']) for film in data]


class ActorInput(graphene.InputObjectType):
    actor_id = graphene.ID(required=True)

class CreateFilm(relay.ClientIDMutation):

    class Input:
        title = graphene.String(required=True)
        actors = graphene.List(ActorInput)
        air_date = graphene_datetime.DateTime(required=True)
        rating = graphene.Int(required=True)

    film = graphene.Field(Film)
    
    @classmethod
    def mutate_and_get_payload(cls, args, context, info):
        actors_ids = [from_global_id(actor['actor_id'])[1] for actor in args['actors']]
        date = arrow.get(args['air_date']).date(),
        data_to_sent = {
            'title': args['title'],
            'actors': actors_ids,
            'air_date': date,
            'rating': args['rating'],
        }
        response = requests.post(ALL_FILMS_ENDPOINT, data=data_to_sent)
        data_from_server = response.json()
        film = Film.create_from_data(data_from_server, data_from_server['id'])
        return CreateFilm(film=film)


class Mutation(graphene.AbstractType):
    create_film = CreateFilm.Field()
