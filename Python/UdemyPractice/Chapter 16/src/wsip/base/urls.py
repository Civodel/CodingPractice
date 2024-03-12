from django.urls import path
from .views import GamesList, GameDetail, GameCreateView, GameEditView, GameDeleteView, Login, LoginCreateView
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', GamesList.as_view(), name='games'),
    path('login/', Login.as_view(), name='login2'),
    path('sign/', LoginCreateView.as_view(), name='sign'),
    path('logout/', LogoutView.as_view(next_page='login2'), name='logout'),
    path('game/<int:pk>', GameDetail.as_view(), name='game'),
    path('game-create/', GameCreateView.as_view(), name='game-create'),
    path('game-edit/<int:pk>', GameEditView.as_view(), name='game-edit'),
    path('game-delete/<int:pk>', GameDeleteView.as_view(), name='game-delete')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

