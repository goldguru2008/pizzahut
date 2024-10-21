from django import forms
from .models import Pizza


class pizzaform(forms.ModelForm):
     class Meta:
         model = Pizza
         fields = ['topping1', 'topping2', 'size']
         labels = {'topping1':'Topping1','topping2':'Topping2','size':'Size'}

class multiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=10)
