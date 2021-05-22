from django.shortcuts import render, redirect
from django.views import generic
from .models import Product
from Cart.forms import CartForm
from Cart.models import Cart
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


class ProductsLister(generic.TemplateView):

    template = 'products_lister.html'

    def get(self, request):
        form = CartForm()
        post = form.save(commit=False)

        products_query = Product.objects.all()

        args = {
            'form': form,
            'products_query': products_query,
        }

        return render(request, self.template, args)

    def post(self, request):

        form = CartForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user

            price = Product.objects.get(name=post.product).price
            post.price = price * post.quantity

            if not Cart.objects.filter(product=post.product).exists():
                post.save()

            return redirect('/shopping-cart/cart')

        return redirect('/')

class ProductDetails(generic.DetailView):

    model = Product

    template_name = 'product_details.html'

    slug_field = 'slug'
    slug_url_kwarg = 'slug'


def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
        
    return render(request, 'registration/signup.html', {'form': form})
