import graphene

from .external_api import ExternalMovie


class Query(graphene.AbstractType):
    description = graphene.String(title=graphene.String())

    def resolve_description(self, args, context, info):
        title = args.get('title')
        external_movie = ExternalMovie(title=title)
        return external_movie.description
