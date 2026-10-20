from django import forms
from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["title", "content", "author"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Give your note a title"}),
            "content": forms.Textarea(attrs={"rows": 6, "placeholder": "Write your note here..."}),
            "author": forms.TextInput(attrs={"placeholder": "Your name"}),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()
        if not title:
            raise forms.ValidationError("Please enter a title.")
        return title

    def clean_content(self):
        content = self.cleaned_data["content"].strip()
        if not content:
            raise forms.ValidationError("Please enter some note content.")
        return content
