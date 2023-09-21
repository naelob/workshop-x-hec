from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
# Create your views here.

def health_view(request):
    if request.method == 'GET':
        return HttpResponse('healthy 200')