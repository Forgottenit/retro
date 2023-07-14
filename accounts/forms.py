from django import forms
from .models import Customer, Review
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

        # user = self.instance.user
        # if user:
        #     self.fields["default_full_name"].initial = user.default_full_name

        placeholders = {
            "default_full_name": "Full Name",
            # "default_last_name": "Last Name",
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
            # user.last_name = customer.default_last_name
            user.save()
            customer.save()
        return customer


class ReviewForm(forms.ModelForm):
    review_text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Review
        fields = ["review_text"]
