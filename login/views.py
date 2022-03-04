from django.shortcuts import render
from django.conf import settings
from django.http import FileResponse, HttpRequest, HttpResponse
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_GET
from logging import exception
from multiprocessing import AuthenticationError
from django import forms
from django.contrib import auth
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from .models import Order
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.views.generic import CreateView
from .forms import RegistrationForm, AdminStudentRegistrationForm
from .forms import OrderForm
from .forms import CommentForm
from bootstrap_datepicker_plus.widgets import DatePickerInput
from .models import Order
from .models import Comment




def home(request):
    return render(request, "index.html")


class RegistrationView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'signup.html'


    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # return redirect('learner')
        return redirect('/signin')

class AdminStudentRegisterView(CreateView):
    model = User
    form_class = AdminStudentRegistrationForm
    template_name = 'signup2.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        # return redirect('learner')
        return redirect('/signin')

class OrderView(CreateView):
    
    model = Order
    form_class = OrderForm
    template_name = 'order.html'

    
    def form_valid(self, form):
        order = form.save()
        # return redirect('learner')
        messages.success(self.request, 'Please Wait, your order will be arrived soon!%s  '%order.Name)
        Name=order.Name
        Contact_number=order.Contact_number
        Japanese_food=order.Japanese_food
        Japanese_food_quantity=order.Japanese_food_quantity
        Rice_Dishes=order.Rice_Dishes
        Rice_Dishes_quantity=order.Rice_Dishes_quantity
        Beverage=order.Beverage
        Beverage_quantity=order.Beverage_quantity
        Vegetarian=order.Vegetarian
        Vegetarian_quantity=order.Vegetarian_quantity
        order_date=order.order_date
        order_time=order.order_time
        Taking_method=order.Taking_method
        payment_method=order.payment_method
        
        return render(self.request, "showorder.html",{'Name':Name, "Contact_number":Contact_number, "Japanese_food":Japanese_food, "Japanese_food_quantity":Japanese_food_quantity, "Rice_Dishes":Rice_Dishes, "Rice_Dishes_quantity":Rice_Dishes_quantity, "Beverage": Beverage, "Beverage_quantity":Beverage_quantity, "Vegetarian":Vegetarian, "Vegetarian_quantity":Vegetarian_quantity, "order_date":order_date, "order_time":order_time, "Taking_method":Taking_method, "payment_method":payment_method})


def showresult(request):
    context={}
    context["dataset"] = Order.objects.all()
    return render(request, "showresult.html", context)

def comment_result(request):
    context={}
    context["dataset"] = Comment.objects.all()
    return render(request, "comment_result.html", context)



class CommentView(CreateView):
    
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html'

    
    def form_valid(self, form):
        comment = form.save()
        # return redirect('learner')
        Nickname=comment.Nickname
        Comment=comment.Comment
        messages.success(self.request, '%s, your comment is posted  '%comment.Nickname)
        return render(self.request, "showcomment.html",{'Nickname':Nickname, "Comment":Comment})




def signin(request):
    if request.method=="POST":
        username=request.POST["username"]
        pass1=request.POST["pass1"]
        user=authenticate(username=username, password=pass1)
        if user is not None:
            auth.login(request, user)
            if user.is_admin or user.is_superuser:
                return redirect('/main_menu2')
            else:
                return redirect('/main_menu')
        else:
            messages.error(request,"Wrong Username or password")
            return render(request, "signin.html")
    else:
        return render(request, "signin.html")


def signout(request):
    return render(request, "index.html")

def menu2(request):
    return render(request,'main_menu2.html')

def menu(request):
    return render(request, 'main_menu.html')

def Japanese_food(request):
   
    return render(request, 'Japanese_food.html')

def Rice(request):
   
    return render(request, 'Rice.html')
def Beverage(request):
   
    return render(request, 'Beverage.html')

def Vegetarian(request):
    return render (request, 'Vegetarian.html')

def rating(request):
    return render(request,'comment.html')

def recipe(request):
    return render(request,'recipe.html')

def recipe2(request):
    return render(request,'recipe2.html')

def share(request):
    return render(request, "share.html")






