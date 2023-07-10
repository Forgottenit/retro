from django import forms
from .widgets import CustomClearableFileInput
from .models import Album, Artist, Genre


class ProductForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = "__all__"

    image = forms.ImageField(
        label="Image", required=False, widget=CustomClearableFileInput
    )

    artists = forms.ModelMultipleChoiceField(
        queryset=Artist.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "border-black rounded-0"
