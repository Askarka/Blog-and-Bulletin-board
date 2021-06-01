from django.conf.urls.static import static
from django.urls import path

# from .views import index, by_rubric, BbCreateView


from src.blog.views import CreatePostView, HomePageView, flow
from true_life import settings

urlpatterns = [
    # path('add/', BbCreateView.as_view(), name='add'),
    # path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    # path('', index, name='index'),
    path('flow/', flow, name='flow'),
    path('', HomePageView.as_view(), name='home'),
    path('post/', CreatePostView.as_view(), name='add_post'), # new
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


