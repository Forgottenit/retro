from django import forms
from .widgets import CustomClearableFileInput
from .models import Album, Genre


class ProductForm(forms.ModelForm):
    class Meta:
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
            self.fields["album_name"].widget.attrs["readonly"] = True
