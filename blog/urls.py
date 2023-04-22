from django.urls import path
from . import starting_page_view 

urlpatterns = [
    path("", starting_page_view.StartingPageView.as_view(), name="starting-page"),
    path("posts", starting_page_view.AllPostsView.as_view(), name="posts-page"),
    path("posts/<slug:slug>", starting_page_view.SinglePostView.as_view(), name="post-detail-page"),
    path ("read-later", starting_page_view.ReadLaterView.as_view(), name="read-later")
]
