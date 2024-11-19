from django import forms
from books.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text']
        labels = {
            'review_text': 'Review'
        }
        widgets = {
            'review_text': forms.Textarea(attrs={'rows': 4}),
        }