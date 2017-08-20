import graphene
from film_database.actors import schema as actors_schema
from film_database.films import schema as films_schema
from film_database.movies_database import schema as external_api


class Query(actors_schema.Query, films_schema.Query, external_api.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
