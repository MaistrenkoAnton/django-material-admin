from modeltranslation.translator import translator, TranslationOptions
from .models import Country


class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Country, CountryTranslationOptions)
