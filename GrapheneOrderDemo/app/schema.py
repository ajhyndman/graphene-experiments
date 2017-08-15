import graphene


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


class Query(graphene.ObjectType):
    person = graphene.Field(Person)
    reverse = graphene.String(word=graphene.String())

    def resolve_reverse(self, args, context, info):
        word = args.get('word')
        return word[::-1]


schema = graphene.Schema(query=Query, mutation=Mutations)
