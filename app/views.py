from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .models import Subscriber, User


# Create your views here.

def home(request):
    return HttpResponse("Hello, world. You're at the Home.")

def subscriber(request):
    data = Subscriber.objects.all().values()
    print(list(data))
    return JsonResponse({"data": list(data)})
    # return JsonResponse({"data":data})


# if Hahsim exist then update the name to Talha Khan
# if not then create a new user with name Talha KHan and email: h@gmail.com
# obj, created = User.objects.update_or_create(
#     name="Hashim",
#     email="h@gmail.com",
#     defaults={"name": "Talha Khan"},
#     # create_defaults={"name": "Khan123"},
# )


# print(obj, created)