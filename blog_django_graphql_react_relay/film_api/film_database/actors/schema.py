import graphene
from graphene_django.types import DjangoObjectType

from .models import Actor


class ActorType(DjangoObjectType):
    class Meta:
        model = Actor


class Query(graphene.AbstractType):
    all_actors = graphene.List(ActorType)
    actor = graphene.Field(
        ActorType,
        id=graphene.Int(),
    )

    def resolve_all_actors(self, args, context, info):
        return Actor.objects.all()

    def resolve_actor(self, args, context, info):
        id = args.get('id')
        return Actor.objects.get(id=id)
