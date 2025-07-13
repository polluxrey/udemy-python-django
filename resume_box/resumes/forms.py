from django import forms
from django.utils import timezone, dateformat
from .models import ResumeModel
from dateutil.relativedelta import relativedelta

ALLOWED_DOMAINS = ["gmail.com"]
ALLOWED_PREFIX = [
    {
        "country": "PH",
        "prefix": "+63",
        "nsn": 10
    }
]
ALLOWED_AGE = 18
ALLOWED_FILES = [".pdf"]
ALLOWED_FILESIZE = 5 * 1024 * 1024


class ResumeForm(forms.ModelForm):
    class Meta:
        model = ResumeModel
        fields = [
            "first_name", "last_name", "email", "phone_number", "date_of_birth", "cover_letter", "resume"
        ]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "Juan"}),
            "last_name": forms.TextInput(
                attrs={"placeholder": "Dela Cruz"}),
            "email": forms.EmailInput(
                attrs={"placeholder": "juandelacruz@gmail.com"}),
            "phone_number": forms.TextInput(
                attrs={"value": "+639",
                       "placeholder": "+639XXXXXXXXX"}),
            "date_of_birth": forms.DateInput(
                attrs={"type": "date",
                       "max": dateformat.format(
                           value=timezone.now() - relativedelta(years=ALLOWED_AGE),
                           format_string="Y-m-d")}
            ),
            "cover_letter": forms.FileInput(
                attrs={"accept": ".pdf"}
            ),
            "resume": forms.FileInput(
                attrs={"accept": ".pdf"}
            )
        }

    def clean_first_name(self):
        first_name = self.cleaned_data.get("first_name")

        if first_name:
            return first_name.strip().upper()
        else:
            raise forms.ValidationError("First name required.")

    def clean_last_name(self):
        last_name = self.cleaned_data.get("last_name")

        if last_name:
            return last_name.strip().upper()
        else:
            raise forms.ValidationError("Last name required.")

    def clean_email(self):
        email = self.cleaned_data.get("email")

        if email:
            email = email.strip().lower()
            domain = email.split("@")[-1]

            if domain not in ALLOWED_DOMAINS:
                raise forms.ValidationError("Email address not valid.")
        else:
            raise forms.ValidationError("Email address required.")

        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get("phone_number")

        if phone_number:
            phone_number = phone_number.strip()

            matched_prefix = next(
                (item for item in ALLOWED_PREFIX if phone_number.startswith(item["prefix"])), None)

            if matched_prefix:
                if len(phone_number) != len(matched_prefix["prefix"]) + matched_prefix["nsn"]:
                    raise forms.ValidationError("Phone number incomplete.")
            else:
                raise forms.ValidationError("Phone number not valid.")
        else:
            raise forms.ValidationError("Phone number required.")

        return phone_number

    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data.get("date_of_birth")

        if date_of_birth:
            if date_of_birth > timezone.now().date() - relativedelta(years=ALLOWED_AGE):
                raise forms.ValidationError("You must be in legal age.")
        else:
            raise forms.ValidationError("Date of birth required.")

        return date_of_birth

    def _validate_uploaded_file(self, file, field_label="File"):
        if file:
            if not file.name.endswith(tuple(ALLOWED_FILES)):
                raise forms.ValidationError(f"{field_label} must be in PDF.")
            if file.size > ALLOWED_FILESIZE:
                raise forms.ValidationError(
                    f"{field_label} must be under 5MB.")

        return file

    def clean_cover_letter(self):
        cover_letter = self.cleaned_data.get("cover_letter")
        return self._validate_uploaded_file(cover_letter, "Cover Letter")

    def clean_resume(self):
        resume = self.cleaned_data.get("resume")
        return self._validate_uploaded_file(resume, "Resume")
