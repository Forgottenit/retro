from django import forms
from .models import Customer, Review, AlbumRequest
from ckeditor.widgets import CKEditorWidget


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ("user",)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)

        placeholders = {
            "default_full_name": "Full Name",
            "default_phone_number": "Phone Number",
            "default_postcode": "Postal Code",
            "default_town_or_city": "Town or City",
            "default_street_address1": "Street Address 1",
            "default_street_address2": "Street Address 2",
            "default_county": "County, State or Locality",
            "default_country": "Country",
        }

        self.fields["default_phone_number"].widget.attrs["autofocus"] = True
        for field in self.fields:
            if field != "default_country":
                if self.fields[field].required:
                    placeholder = f"{placeholders[field]} *"
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs[
                "class"
            ] = "border-black rounded-0 profile-form-input"
            self.fields[field].label = False

    def save(self, commit=True):
        customer = super().save(commit=False)
        if commit:
            user = customer.user
            user.full_name = customer.default_full_name
            user.save()
            customer.save()
        return customer


class ReviewForm(forms.ModelForm):
    review_text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Review
        fields = ["review_text"]


class AlbumRequestForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "cols": 15}), required=False
    )
    artist_name = forms.CharField(required=False)
    album_title = forms.CharField(required=False)

    class Meta:
        model = AlbumRequest
        fields = ["artist_name", "album_title", "message"]

    def __init__(self, *args, **kwargs):
        super(AlbumRequestForm, self).__init__(*args, **kwargs)
        customer = kwargs.get("instance")
        if customer:
            self.fields["artist_name"].initial = customer.default_full_name
            self.fields[
                "album_title"
            ].initial = customer.default_phone_number
