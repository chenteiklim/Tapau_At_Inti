from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.contrib.auth import get_user_model
import datetime  

item_choices1=[
    ('Sushi', 'Sushi'),
    ('Okonomiyaki',"Okonomiyaki"),
    ('Gyoza',"Gyoza"),
    ('Mochi',"Mochi"),
    ('Kushiyaki','Kushiyaki'),
    ('None','None')
]


item_choices2=[
    ('Milo ice', 'Milo ice'),
    ('Chrysanthemum Tea',"Chrysanthemum Tea"),
    ('Watermelon juice ',"Watermelon juice "),
    ('Orange Juice',"Orange Juice"),
    ('Lemon tea','Lemon tea'),
    ('None',"None")
]


item_choices3=[
    ('Hainan Chicken Rice', 'Hainan Chicken Rice'),
    ('Nasi Lemak',"Nasi Lemak"),
    ('Fried rice ',"Fried rice "),
    ('indian Style rice',"Indian Style rice"),
    ('Economy rice','Economy rice'),
    ('None',"None")
]

item_choices4=[
    ('Walnut and Lentil Bolognese ', 'Walnut and Lentil Bolognese '),
    ('Vegan Roasted Sweet Potato Salad',"Vegan Roasted Sweet Potato Salad"),
    ('Shaved Brussels Sprout Salad  ',"Shaved Brussels Sprout Salad  "),
    ('Vegetarian Burrito Bowl with Avocado Crema',"Vegetarian Burrito Bowl with Avocado Crema"),
    ('Green Curry Buddha Bowl','Green Curry Buddha Bowl'),
    ('None',"None")
]
item_choices5=[
    ('Dine in','Dine in'),
    ('Take away','Take away')
]

payment_choices=[
    ('Credit Card','Credit Card'),
    ('Cash','Cash')
]

class User(AbstractUser):
    is_Customer=models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
class Order(models.Model):  
    Name=models.CharField(max_length=50)
    Contact_number=models.CharField(max_length=50)
    Japanese_food= models.CharField(max_length=50, default="None", choices=item_choices1)
    Japanese_food_quantity=models.IntegerField( default=0)
    Beverage=models.CharField(max_length=50, default="None", choices=item_choices2)
    Beverage_quantity=models.IntegerField( default=0)
    Rice_Dishes=models.CharField(max_length=50, default="None", choices=item_choices3)
    Rice_Dishes_quantity=models.IntegerField( default=0)
    Vegetarian=models.CharField(max_length=50, default="None", choices=item_choices4)
    Vegetarian_quantity=models.IntegerField( default=0)
    order_date=models.CharField(max_length=50, blank=True, null=True)
    order_time=models.CharField( max_length=50, default=0)
    payment_method=models.CharField(max_length=50, default="credit card", choices=payment_choices)
    Taking_method=models.CharField(max_length=50, default="None", choices=item_choices5)

class Comment(models.Model): 
    Nickname=models.CharField(max_length=50)
    Comment=models.CharField(max_length=150)




    