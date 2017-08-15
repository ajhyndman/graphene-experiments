import graphene
from graphene_django import DjangoObjectType

from .models import Person as DjangoPerson, Mother, Father, Sister, Brother


# Issue 1 stuff
class Person(graphene.ObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    full_name = graphene.String()
    age = graphene.Int()

    def resolve_full_name(self, args, context, info):
        return '{} {}'.format(self.first_name, self.last_name)


class PersonInput(graphene.InputObjectType):
    first_name = graphene.String()
    age = graphene.Int()


class CreatePerson(graphene.Mutation):
    class Input:
        person_data = graphene.Argument(PersonInput)
        more_person_data = graphene.Argument(PersonInput)
        even_more_person_data = graphene.Argument(PersonInput)

    person = graphene.Field(lambda: Person)

    @staticmethod
    def mutate(root, args, context, info):
        p_data = args.get('person_data')

        first_name = p_data.get('first_name')
        age = p_data.get('age')

        person = Person(first_name=first_name, age=age)
        return CreatePerson(person=person)


class Mutations(graphene.ObjectType):
    create_person = CreatePerson.Field()


# Issue 2
class PersonObject(DjangoObjectType):
    class Meta:
        model = DjangoPerson
        name = "DjangoPerson"


class MotherObject(DjangoObjectType):
    class Meta:
        model = Mother
        name = "Mother"


class FatherObject(DjangoObjectType):
    class Meta:
        model = Father
        name = "Father"


class SisterObject(DjangoObjectType):
    class Meta:
        model = Sister
        name = "Sister"


class BrotherObject(DjangoObjectType):
    class Meta:
        model = Brother
        name = "Brother"


class Query(graphene.ObjectType):
    person = graphene.Field(Person)

    mother = graphene.Field(MotherObject)
    father = graphene.Field(FatherObject)
    sister = graphene.Field(SisterObject)
    brother = graphene.Field(BrotherObject)

schema = graphene.Schema(query=Query, mutation=Mutations)
