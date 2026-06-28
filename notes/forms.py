from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    """Form for creating and updating notes."""
    class Meta:
        """Bind the form to the Note model's title and content fields."""
        model = Note
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control",
                                             "rows": 5}),
        }
