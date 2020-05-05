from django.urls import path

from knowledgepro import views

app_name = 'knowledgepro'
urlpatterns=[

        path('register',views.register,name='register'),
        path('user_login/',views.user_login,name='user_login')
]
