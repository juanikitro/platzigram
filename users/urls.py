"""Posts URLs"""

# Django
from django.urls import path

# Views
from users import views

urlpatterns = [

    # Management
        path(
            route = 'users/login/', 
            view = views.login_view, 
            name='login'
        ),
        path(
            route = 'users/logout/', 
            view = views.logout_view, 
            name='logout'
        ),
        path(
            route = 'users/signup/', 
            view = views.signup_view, 
            name='signup'
        ),
        path(
            route = 'users/me/profile/', 
            view = views.update_profile, 
            name='update_profile'
        ),

    # Posts
    path(
        route = 'profile/<str:username>',
        view = views.UserdetailView.as_view(),
        name = 'detail',
    ),
    
]