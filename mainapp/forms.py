import json

from django import forms

from mainapp.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm, StyleFormMixin):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ('product_name', 'description', 'product_price', 'product_image',)
        # exclude = ('is_active', )


    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Вы используете запрещённое слово {word}')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError(f'Вы используете запрещённое слово {word}')

        return cleaned_data


class VersionForm(forms.ModelForm, StyleFormMixin):
    class Meta:
        model = Version
        fields = '__all__'



