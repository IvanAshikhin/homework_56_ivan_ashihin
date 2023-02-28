from django import forms
from webapp.models import Product


class DecimalInput(forms.TextInput):
    input_type = 'number'
    is_hidden = False


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'description', 'image', 'category', 'remain', 'cost']
        labels = {
            'product_name': 'Наименование',
            'description': 'Описание',
            'image': 'Изображение',
            'category': 'Категория',
            'remain': 'Остаток',
            'cost': 'Стоимость'
        }
        widgets = {
            'remain': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'cost': DecimalInput(attrs={'class': 'form-control'})
        }
