from django import forms

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        # fields = ['name', 'price', '']
        # exclude = ['user']

    def clean_product_name(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['product_name']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В названии товара не допустимо использования слова: {}'.format(word))
        return cleaned_data

    def clean_product_description(self):
        forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа',
                           'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        cleaned_data = self.cleaned_data['product_description']
        for word in forbidden_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('В описании товара не допустимо использования слова: {}'.format(word))
        return cleaned_data


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
