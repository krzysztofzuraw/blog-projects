import graphene
from graphene_django.types import DjangoObjectType

from film_database.actors.schema import ActorType

from .models import Film


class FilmType(DjangoObjectType):
    actors = graphene.List(ActorType)

    class Meta:
        model = Film

    @graphene.resolve_only_args
    def resolve_actors(self):
        return self.actors.all()


class Query(graphene.AbstractType):
    all_films = graphene.List(FilmType)
    film = graphene.Field(
        FilmType,
        id=graphene.Int(),
    )

    def resolve_all_films(self, args, context, info):
        return Film.objects.all()

    def resolve_film(self, args, context, info):
        id = args.get('id')
        return Film.objects.get(id=id)
