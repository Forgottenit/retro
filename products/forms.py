"""
Module for Products app forms:  Product and Load Albums
"""
from django import forms
from .widgets import CustomClearableFileInput
from .models import Album, Genre


class ProductForm(forms.ModelForm):
    """
    Form to edit Albums
    """

    class Meta:
        """
        Set fields for product Form
        """

        model = Album
        fields = [
            "album_name",
            "artists",
            "genres",
            "popularity",
            "price",
            "image",
        ]

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.SelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
        if "album_name" in self.fields:
            self.fields["album_name"].widget.attrs["readonly"] = False


class LoadAlbumsForm(forms.Form):
    """
    Form to select Albums to upload to Database
    """

    SEARCH_FIELDS = [("artist", "Artist"), ("album", "Album")]

    search_field = forms.ChoiceField(choices=SEARCH_FIELDS)
    query = forms.CharField(
        label="Query",
        widget=forms.TextInput(
            attrs={"placeholder": "Enter search term..."}
        ),
    )
