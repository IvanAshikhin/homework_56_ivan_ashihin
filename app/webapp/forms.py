from django import forms
from webapp.models import Product


class DecimalInput(forms.TextInput):
    input_type = 'number'
    is_hidden = False


class ProductForm(forms.ModelForm):
    CHOICES = [
        ('laptops', 'Laptops'),
        ('headphones', 'Headphones'),
        ('mouses', 'Mouses'),
        ('keyboards', 'Keyboards'),
        ('other', 'Other')
    ]
    category = forms.ChoiceField(choices=CHOICES, initial='other', label="Category")

    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image', 'category', 'remain', 'cost']
        labels = {
            'product_name': 'Product',
            'description': 'Description',
            'image': 'Image',
            'remain': 'Remain',
            'cost': 'Cost'
        }
        widgets = {
            'remain': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'cost': DecimalInput(attrs={'class': 'form-control'})
        }
