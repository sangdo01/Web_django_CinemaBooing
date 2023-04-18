from django.forms import ModelForm
from .models import ReviewRating


class ReviewRatingForm(ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['review', 'rate']

