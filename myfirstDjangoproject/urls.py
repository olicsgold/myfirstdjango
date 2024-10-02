from django.contrib import admin 
from django.urls import path, re_path  # Ensure re_path is imported
from webchat import views
from accounts import views as accounts_views

urlpatterns = [
    # Admin site URL
    path('admin/', admin.site.urls),

    # Home page URL
    path('', views.home, name='home'),  # Home page
    path('home/', views.home, name='home'),
    re_path(r'^signup/$', accounts_views.signup, name='signup'),  # Fixed the typo here

    # URL patterns for chat boards and topics
    path('board/<int:board_pk>/topics/', views.chat_board_topics, name='chat_board_topics'),  # List topics in a board
    path('board/<int:board_pk>/topic/new/', views.new_board_topic, name='new_board_topic'),  # Create new topic
    path('board/<int:board_pk>/topic/<int:topic_pk>/', views.board_topic, name='board_topic'),  # View specific topic

    # Uncomment and correct the following lines as needed
    # path('about/', views.about, name='about'),
    # path('about/company/', views.about_company, name='about_company'),
    # path('about/privacy/', views.about_privacy, name='about_privacy'),
]
