from django.db import models
from playhouse.djpeewee import translate

class Word(models.Model):
    infinite_en = models.CharField(max_length=255)
    infinite_es = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

PWord = translate(Word).Word

class Tense(models.Model):
    name = models.CharField(max_length=255)

PTense = translate(Tense).Tense

class Person(models.Model):
    name = models.CharField(max_length=255)

PPerson = translate(Person).Person

class Conjugation(models.Model):
    form = models.CharField(max_length=255)
    person = models.ForeignKey(Person)
    tense = models.ForeignKey(Tense)

PConjugation = translate(Conjugation).Conjugation
# Create your models here.
