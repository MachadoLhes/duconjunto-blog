from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def home(request):
    context = {
        'user': request.user,
    }

    return render(request, 'home.html', context)