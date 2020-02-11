from django.shortcuts import render, redirect
from apps.online_shop_dashboard.models import Product, Category
from apps.online_shop_index.models import User

def dashboard(request):
        if("user_id" not in request.session):
            return redirect('/login')
        context = {
            "request": request,
            "category": Category.objects.all(),
            "user_cart": User.objects.get(id = request.session["user_id"]).shopping_cart.all()
        }
        return render(request, "online_shop_dashboard/dashboard.html", context)

def show_product(request, product_id):
    context = {
        "request": request,
        "category": Category.objects.all(),
        "user_cart": User.objects.get(id = request.session["user_id"]).shopping_cart.all(),
        "p": Product.objects.get(id = product_id),
    }
    return render(request, "online_shop_dashboard/show_product.html", context)

def create_product(request):
    context = {
        "request": request,
        "category": Category.objects.all(),
        "user_cart": User.objects.get(id = request.session["user_id"]).shopping_cart.all()
    }
    if request.method == "POST":
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_image = request.POST['product_image']
        product_details = request.POST['product_details']
        product_category = request.POST['product_category']
        if len(Category.objects.filter(name = product_category)) == 0:
            Category.objecsts.create(name = product_category)
        curr_product = Product.objects.create(name = product_name,  price = product_price, image = product_image, details = product_details)
        return redirect ('products/show/' + str(curr_product.id))
    return render(request, "online_shop_dashboard/create_product.html", context)

def add_to_cart(request, product_id):
    target_Product = Product.objects.get(id = product_id)
    target_user = User.objects.get(id = request.session["user_id"])
    target_user.shopping_cart.add(target_Product)
    return redirect('/')

def remove_from_cart(request, product_id):
    target_Product = Product.objects.get(id = product_id)
    target_user = User.objects.get(id = request.session["user_id"])
    target_user.shopping_cart.remove(target_Product)
    return redirect('/products/shopping_cart')

def show_shopping_cart(request):
    context = {
        "request": request,
        "category": Category.objects.all(),
        "user_cart": User.objects.get(id = request.session["user_id"]).shopping_cart.all()
    }
    return render(request, "online_shop_dashboard/shopping_cart.html", context)


        

        

