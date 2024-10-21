from django.shortcuts import render
from .forms import pizzaform,multiplePizzaForm

# Create your views here.
def homepage(request):
    return render(request, 'pizza/home.html')
def order(request):
    multiple_Pizza_form = multiplePizzaForm()
    if request.method == 'POST':
        filled_form = pizzaform(request.POST)
        if filled_form.is_valid():
            note = 'Thanks your ordering %s, %s, %s size pizza'%(filled_form. cleaned_data['topping1'],
                                                                 filled_form. cleaned_data['topping2'],
                                                                 filled_form. cleaned_data['size'])
            filled_form.save()
        else:
            note = 'Sorry please tryagain...'
        new_form = pizzaform()
        return render(request, 'pizza/order.html', {'PizzaForm':filled_form,'note':note,'multiple_pizza_form': multiplePizzaForm})
    else:
        form = pizzaform()
        print(form)
        print('hello')
        return render(request, 'pizza/order.html', {'PizzaForm': form,'multiple_pizza_form':multiplePizzaForm})

def pizzas(request):
    no_of_pizzas = 2
    if request.method =='GET':
        filled_multiple_pizza_form = multiplePizzaForm(request.GET)
        if filled_multiple_pizza_form.is_valid():
           no_of_pizzas =  filled_multiple_pizza_form.cleaned_data['number']
        print(no_of_pizzas)
    return render(request,'pizza/pizzas.html')

