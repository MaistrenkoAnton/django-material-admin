from modeltranslation.translator import translator, TranslationOptions
from .models import Country, Person


class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)


class PersonTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Country, CountryTranslationOptions)
translator.register(Person, PersonTranslationOptions)
