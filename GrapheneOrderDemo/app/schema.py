import graphene
from graphene_django import DjangoObjectType

from .models import Person, Mother, Father, Sister, Brother


class PersonObject(DjangoObjectType):
    class Meta:
        model = Person
        name = "Person"


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


class Query2(graphene.ObjectType):
    mother = graphene.Field(MotherObject)
    father = graphene.Field(FatherObject)
    sister = graphene.Field(SisterObject)
    brother = graphene.Field(BrotherObject)

schema = graphene.Schema(query=Query2)
