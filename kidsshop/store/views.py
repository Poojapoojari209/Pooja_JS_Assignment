from django.shortcuts import render

def home(request):
    return render(request, 'store/home.html')

def products(request):
    product_list = [
        {'name': 'Kids T-Shirt', 'price': 499},
        {'name': 'Toy Car', 'price': 299},
        {'name': 'School Bag', 'price': 899},
    ]
    return render(request, 'store/products.html', {'products': product_list})

def cart(request):
    return render(request, 'store/cart.html')
