from django import forms

from account.models import Articles


# class ItemCreation(forms.ModelForm):
#     class Meta:
#         model = Articles
#         fields = ['heading', 'body', 'author']
#         widgets = {
#             'heading': forms.TextInput(attrs={'class': 'form-control'}),
#             'body': forms.TextInput(attrs={'class': 'form-control'}),
#             'author': forms.NumberInput(attrs={'class': 'form-control'}),
#         }


class ItemCreation(forms.ModelForm):
    class Meta:
        model = Articles
        fields = ['heading', 'body', 'category', 'content_type', 'source_link', 'image_link', 'tags', 'published_date',
                  'published_time', 'author']
        widgets = {
            'heading': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'cols': "40", 'rows': "5"}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'content_type': forms.TextInput(attrs={'class': 'form-control'}),
            'source_link': forms.TextInput(attrs={'class': 'form-control'}),
            'image_link': forms.TextInput(attrs={'class': 'form-control'}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'published_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM/DD/YYYY'}),
            'published_time': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'HH:MM'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),

        }
