from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'status', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class SupplierProductForm(forms.ModelForm):
    STATUS_CHOICES = (
        ('WA', 'Waiting for receipt'),
        ('NA', 'Not available'),
    )

    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), disabled=True)
    status = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}, choices=STATUS_CHOICES))

    class Meta:
        model = Product
        fields = ['name', 'status', 'quantity']
        widgets = {
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class SellProductForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'datas'}))
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control datas'}), label='Quantity:')

    def clean(self):
        product_id = self.cleaned_data.get('product_id')
        if not product_id:
            raise forms.ValidationError("There is not product id data!")

        if not Product.objects.filter(id=product_id).exists():
            raise forms.ValidationError("Such product does not exist!")

        product = Product.objects.get(id=product_id)
        quantity = self.cleaned_data['quantity']

        if product.quantity < quantity:
            raise forms.ValidationError("You can't sell more goods than you have!")

        product.quantity -= quantity
        product.save()
        return self.cleaned_data


class DeleteProductForm(forms.Form):
    prod_id = forms.IntegerField(widget=forms.HiddenInput(attrs={'class': 'datas'}))

    def clean(self):
        prod_id = self.cleaned_data.get('prod_id')
        if not prod_id:
            raise forms.ValidationError("There is not product id data!")
        if not Product.objects.filter(id=prod_id).exists():
            raise forms.ValidationError("Such product does not exist!")
        return self.cleaned_data

