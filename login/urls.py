from django.urls import path, include
from . import views
from django.conf import settings
from django.views.generic.base import RedirectView
from .views import RegistrationView, OrderView, CommentView, AdminStudentRegisterView
from .forms import OrderForm

app_name = 'login' # So we can use it like: {% url 'mymodule:user_register' %} on our template.
urlpatterns = [
    path('', views.home, name="home"),
    path('signup2', AdminStudentRegisterView.as_view(), name="signup"),
    path('signin', views.signin, name="signin"),
    path('signup', RegistrationView.as_view(), name="signup"),
    path('index/', views.signout, name="signout"),
    path('Rice/', views.Rice, name='rice') ,
    path('Beverage/', views.Beverage, name='Beverage') ,
    path('Japanese_food/', views.Japanese_food, name='Japanese food') ,
    path('Vegetarian/', views.Vegetarian, name='Vegetarian') ,
    path('order', OrderView.as_view(), name="order"),
    path('Japanese_food/order', OrderView.as_view(), name="order"),
    path('Rice/order', OrderView.as_view(), name="order"),
    path('Beverage/order', OrderView.as_view(), name="order"),
    path('Vegetarian/order', OrderView.as_view(), name="order"),
    path('main_menu', views.menu, name="main_menu"),
    path('Japanese_food/comment', CommentView.as_view(), name="comment"),
    path('Rice/comment', CommentView.as_view(), name="comment"),
    path('Beverage/comment', CommentView.as_view(), name="comment"),
    path('Vegetarian/comment', CommentView.as_view(), name="comment"),
    path('comment', CommentView.as_view(), name="order"),
    path('recipe', views.recipe, name="recipe"),
    path('recipe2', views.recipe2, name="recipe2"),
    path('share', views.share, name="share"),
    path('main_menu2', views.menu2, name="main_menu2"),
    path('showresult', views.showresult, name="showresult"),
    path('comment_result', views.comment_result, name="showresult"),
    
    
    
   
   
   
  
  
    
]
  
