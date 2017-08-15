from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    nick_name = models.CharField(max_length=50)
    not_a_name = models.CharField(max_length=50)
    age = models.IntegerField()
    looks = models.BigIntegerField()

    def __str__(self):
        return self.name


class FamilyMember(models.Model):
    class Meta:
        abstract= True

    person = models.OneToOneField(Person, primary_key=True)
    job = models.CharField(max_length=100)


class Mother(FamilyMember):
    pass


class Father(FamilyMember):
    pass


class Sister(FamilyMember):
    pass


class Brother(FamilyMember):
    pass
