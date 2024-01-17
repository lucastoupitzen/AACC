from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("encaminhamentos/", views.encaminhamentos, name="encaminhamentos"),
    path("login/", views.login, name='login'),
    path("naoencaminhadas/", views.aacc_aguardando_encaminhamento, name="naoencaminhadas"),
    path('documentos/<str:nome_arquivo>', views.visualizar_documento, name='visualizar_documento'),
    path('encaminhar/', views.encaminhar, name="encaminhar"),
    path('cadastro/', views.cadastro, name="cadastro"),
    path('home/', views.home_page, name="home"),
    path("logout/", views.logout, name="logout"),
    path("avaliar_page/", views.avaliar_page, name="avaliar_page"),
    path("nao_avaliadas/<str:nrousp>", views.aacc_aguardando_avaliacao, name="aacc_nao_avaliadas"),
    path("avaliar/", views.avaliar, name="avaliar"),
    path("confirmar_page/", views.confirmar_page, name="confirmar_page"),
    path("confirmar_page/nao_confirmadas", views.aacc_aguardando_confirmacao, name="naoconfirmadas"),
    path("confirmar_page/confirmar", views.confirmar, name="confirmar")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)