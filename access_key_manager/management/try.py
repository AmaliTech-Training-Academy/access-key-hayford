from django.contrib.auth.models import User

def create_user(request):
    user= User.objects.get(id)
    print (user.email)