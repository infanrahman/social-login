from django.shortcuts import render

from allauth.socialaccount.models import SocialAccount

def profile_view(request):
    social_account = SocialAccount.objects.filter(user=request.user, provider='google').first()
    if social_account:
        # User is logged in with Google, get their email and profile picture
        email = social_account.extra_data['email']
        profile_picture_url = social_account.extra_data['picture']
    else:
        # User is not logged in with Google
        email = None
        profile_picture_url = None

    # Render the template with the user's email and profile picture
    return render(request, 'profile.html', {
        'email': email,
        'profile_picture_url': profile_picture_url,
    })

def home(request):
    return render(request, 'index.html')