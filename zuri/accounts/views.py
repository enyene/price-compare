from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render
from .models import Product , Platform
from .decorators import unauthenticated_user
from .products import jumia_get_product
from .forms import CommentForm
from django.contrib.auth.decorators import login_required



# Create your views here.

# landing page
def home(request):
    return render(request, 'accounts/home.html')

#login page
@unauthenticated_user
def user_login(request):
    user = request.user
    context = {'user': user}
    return render(request, 'accounts/login.html', context)


# register page
@unauthenticated_user
def register(request):
    return render(request, 'accounts/register.html')

# logout page
def logout(request):
    return render(request, 'accounts/logout.html')


 # profile page
@login_required(login_url='/')
def profile(request):
    return render(request, 'accounts/profile.html')


def product_detail(request,id,product):
    product = get_object_or_404(
        Product,
        slug=product,
        id = id,
    )

    comments = product.comments.filter(active=True)
    new_comment = None
    platforms = []
    prd = {
        'name':product.name,
        'brand':product.brand
    }
    print(prd)
    platforms.append(jumia_get_product(prd))

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.product = product
            new_comment.save()
    else:
            comment_form = CommentForm()

    return render(request,'price_compare/product/detail.html',
                    {
                        'product':product,
                        'comments':comments,
                        'platforms':platforms,
                        'new_comment':new_comment,
                        'comment_form':comment_form
                    },            
    )


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'price_compare/product/list.html'
    