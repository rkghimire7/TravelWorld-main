from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from accounts.forms import GuideForm
from travello.models import Guide , Destination, Contact


# Create your views here.


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid credentials...")
            return redirect("login")
    else:
        return render(request, "login.html")


def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken...")
                test = User.objects.all()
                print(test)
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken...")
                return redirect("register")
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password1,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                )
                user.save()
                messages.info(request, "user created...")
                return redirect("login")
        else:
            messages.info(request, "password not matched...")
            return redirect("register")
        return redirect("/")
    else:
        return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect("/")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the contact message to the database
        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        # Display a success message
        messages.success(request, 'Your message has been sent successfully!')

        # Redirect to the same page to clear the form
        return redirect('contact')  # Replace 'contact' with your URL name for this view

    return render(request, 'contact.html')  # Update with the correct template path

# def contact(request):
#     if request.method == 'POST':
#         print(request.POST)  # Debugging
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         subject = request.POST.get('subject')
#         message = request.POST.get('message')

#         Contact.objects.create(
#             name=name,
#             email=email,
#             subject=subject,
#             message=message,
#         )
#         messages.success(request, 'Your message has been sent successfully!')
#         return redirect('contact')
#     return render(request, 'contact.html')


def index(request):
    return render(request, 'accounts/index.html') 

def about(request):
    return render(request, "about.html")


def guides(request):
    guides = Guide.objects.all()
    return render(request, "guides.html", {"guides":guides})


def destinations(request):
    destinations = Destination.objects.all()
    return render(request, 'destinations.html', {'destinations': destinations})


# def guide(request):
#     return render(request, 'guideregistration.html')
# # guide.html thyo paila ya


def guide(request):
    if request.method == "POST":
        form = GuideForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")  # Redirect to a success page
    else:
        form = GuideForm()
    return render(request, "guideregistration.html", {"form": form})
