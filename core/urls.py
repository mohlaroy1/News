from django.contrib import admin
from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from main.views import HomeView, NewsletterCreateView, ArticleDetailsView, CommentCreateView, ContactView,SearchArticlesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('articles/<slug:slug>/', ArticleDetailsView.as_view(), name='article-details' ),
    path('newsletter/create/', NewsletterCreateView.as_view(), name='newsletter-create'),
    path('<slug:slug>/add-comment/', CommentCreateView.as_view(), name='comment-create'),
    path('contact-us/', ContactView.as_view(), name='contact-us'),
    path('search/',SearchArticlesView, name='search-articles'),


]


urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

