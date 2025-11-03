from django.urls import path
from .views import students, delete, student_detail, update_student, create_student, register, myOwnLogoutView, profile, detail_profile
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', students, name='main'),
    path('student/<int:pk>/', student_detail, name='detail'),
    path('update/<int:pk>/', update_student, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('create', create_student, name='create'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('detail_profile/', detail_profile, name='detail_profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', myOwnLogoutView, name='logout')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

