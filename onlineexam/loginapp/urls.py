from django.urls import path

from . import views


urlpatterns = [

    
    path('saveUser/',views.saveUser),   
    path('login/',views.login),
    path('addition/<no1>/<no2>',views.addition),

    path('giveMePage1/',views.giveMePage1),

    path('sum/',views.sum)



]