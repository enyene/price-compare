from django.shortcuts import redirect
from django.contrib import messages

# decorator for  unauthenticated users
def unauthenticated_user(view_func):
     def wrapper_func(request, *args, **kwargs):

        # If user is logged in, redirect to homepage
        if request.user.is_authenticated:
            return redirect('/')

        # If user is not logged in, show the page they tried to access
        else:
            return view_func(request, *args, **kwargs)
     return wrapper_func

# decorator for users 
def allowed_users(allowed_roles=None):
    if allowed_roles is None:
        allowed_roles = []

    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            # Check if user is apart of any Groups
            groups = None
            if request.user.groups.exists():
                # group = request.user.groups.all()[0].name
                groups = request.user.groups.all()

            # If User group is allowed, show the page
            for group in groups:
                if group.name in allowed_roles:
                    return view_func(request, *args, **kwargs)

            # If User group is not allowed, show unauthorized message
            else:
                messages.error(request, f"You are not authorized to view this page")
                return redirect("/")
        return wrapper_func
    return decorator

# decorator for superuser
def superuser_only(view_func):
    def wrapper_func(request, *args, **kwargs):

        # If user is logged in, redirect to homepage
        if not request.user.is_superuser:
            messages.error(request, f"You are not authorized to view this page")
            return redirect('/')

        # If user is not logged in, show the page they tried to access
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func