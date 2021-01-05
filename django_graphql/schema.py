import graphene
from graphene_django import DjangoObjectType
from user.graphql.queries import UserQuery
from user.graphql.mutations import CreateUserMutation


class RootQuery(UserQuery, graphene.ObjectType):
    pass


class RootMutation(graphene.ObjectType):
    create_user = CreateUserMutation.Field()
    pass


schema = graphene.Schema(query=RootQuery, mutation=RootMutation)
