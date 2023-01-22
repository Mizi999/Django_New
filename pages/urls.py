from django.urls import path
from .views import HomePageView,AboutPage,Sign
urlpatterns = [
path('sign_in/', Sign.as_view(),name = 'sign_in'),
path('about/', AboutPage.as_view(), name = 'about'),
path('', HomePageView.as_view(), name = 'home'),

]
