from django.urls import path
from .views import KakaoLogin
import accounts.views

app_name='accounts'

urlpatterns = [
    path('',accounts.views.index, name="index"),
    path('oauth/',accounts.views.oauth, name='oauth'),
    path('kakao_login/',accounts.views.kakao_login, name='kakao_login'),
    path('kakao_logout/',accounts.views.kakao_logout, name='kakao_logout'),

	path('rest-auth/kakao/', KakaoLogin.as_view(), name='kakao_login2'),
]