"""Platzigram middleware catalog """

#Django
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Proile completion middleware.
    Ensure every user that is interacting with de plataform have their profile picture and biography
    """

    def __init__(self, get_response):
        """Middleware initialization"""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called"""
        if not request.user.is_anonymous:
            
            #valida que el usuario sea administrador y permite que la solicitud continue
            if request.user.is_superuser:
                return self.get_response(request)
            
            #verifica el perfil del usuario 
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                    return redirect('users:update_profile')

        response = self.get_response(request)
        return response 