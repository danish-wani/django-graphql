import graphene
from django.contrib.auth.models import User
from .types import UserType


class UserQuery(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):
        # We can easily optimize query count in the resolve method
        return User.objects.all()
