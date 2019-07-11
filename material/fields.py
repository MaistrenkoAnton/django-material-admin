from django.forms import Field

from material.widgets import MaterialAutocompleteInput


class AutocompleteField(Field):
    widget = MaterialAutocompleteInput

    def __init__(self, *, strip=True, empty_value='', choices=None, **kwargs):
        self.strip = strip
        self.empty_value = empty_value
        super().__init__(**kwargs)
        self.widget.choices = choices
        print(self.widget.choices)
