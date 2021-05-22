from django.shortcuts import render, redirect
from .models import Cart
from .forms import OrderCreateForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


@login_required
def cart_lister(request):

    cart_lister = Cart.objects.filter(user=request.user)

    return render(request, "cart_lister.html", {'cart_lister': cart_lister})


class PerformCommand(LoginRequiredMixin, generic.TemplateView):

    template = 'command_form.html'

    def get(self, request):
        form = OrderCreateForm()
        post = form.save(commit=False)

        args = {
            'form': form,
        }

        return render(request, self.template, args)

    def post(self, request):

        form = OrderCreateForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.user = request.user

            for query in Cart.objects.filter(user=request.user):

                post.products_list = post.products_list + str(query.product) + " " + str(query.quantity) + " " + str(query.price) + "\n"

                query.delete()

            post.save()

            return redirect('/')

        return redirect('/')
