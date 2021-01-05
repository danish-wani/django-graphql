import graphene

from django.contrib.auth.models import User
from .types import UserType


class CreateUserMutation(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        username = graphene.String()
        email = graphene.String()
    
    @classmethod
    def mutate(cls, root, info, username, email, *args, **kwargs):

        user_obj = User.objects.create(username=username, email=email)

        return CreateUserMutation(user=user_obj)