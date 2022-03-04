from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.db import transaction
from .models import (User,Customer, Order, Comment)


class RegistrationForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
    

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_Customer= True
        user.save()
        Customer.objects.create(user=user)
        return user

class AdminStudentRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    contact = forms.CharField(max_length=11)

    class Meta:
        model = User
        fields = ['username', 'email', 'contact', 'password1', 'password2']

    

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.save()
        Customer.objects.create(user=user)
        return user



class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=["Name","Contact_number", "Japanese_food","Japanese_food_quantity","Beverage","Beverage_quantity","Rice_Dishes","Rice_Dishes_quantity", "Vegetarian", "Vegetarian_quantity" ,"order_date","order_time","payment_method","Taking_method"]
    

    @transaction.atomic
    def save(self):
        order = super().save(commit=False)
        order.save()
        Order.objects.create()
        return order

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=["Nickname","Comment"]
    

    @transaction.atomic
    def save(self):
        comment = super().save(commit=False)
        comment.save()
        Comment.objects.create()
        return comment

   