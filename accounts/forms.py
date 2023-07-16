from django import forms
from .models import Customer, Review, AlbumRequest
from ckeditor.widgets import CKEditorWidget


from django import forms
from .models import Customer


from django import forms
from .models import Customer


class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ("user",)
        fields = (
            "default_first_name",
            "default_last_name",
            "default_phone_number",
            "default_postcode",
            "default_town_or_city",
            "default_street_address1",
            "default_street_address2",
            "default_county",
            "default_country",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "default_first_name": "First Name",
            "default_last_name": "Last Name",
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

            # Update first name and last name
            default_first_name = self.cleaned_data.get(
                "default_first_name", "Unknown"
            )
            default_last_name = self.cleaned_data.get(
                "default_last_name", "Unknown"
            )
            print(
                f"Updating user: {user.username} with first_name: {default_first_name} and last_name: {default_last_name}"
            )

            user.first_name = default_first_name
            user.last_name = default_last_name

            # Update address fields
            customer.default_phone_number = self.cleaned_data[
                "default_phone_number"
            ]
            customer.default_postcode = self.cleaned_data["default_postcode"]
            customer.default_town_or_city = self.cleaned_data[
                "default_town_or_city"
            ]
            customer.default_street_address1 = self.cleaned_data[
                "default_street_address1"
            ]
            customer.default_street_address2 = self.cleaned_data[
                "default_street_address2"
            ]
            customer.default_county = self.cleaned_data["default_county"]
            customer.default_country = self.cleaned_data["default_country"]

            user.save()
            customer.save()

        return customer


class ReviewForm(forms.ModelForm):
    review_text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Review
        fields = ["review_text"]


class AlbumRequestForm(forms.ModelForm):
    request_title = forms.CharField(required=True)
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 4, "cols": 15}), required=False
    )

    artist_name = forms.CharField(required=False)
    album_title = forms.CharField(required=False)

    class Meta:
        model = AlbumRequest
        fields = ["request_title", "artist_name", "album_title", "message"]
