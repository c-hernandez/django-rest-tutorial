from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets.views import SnippetViewSet, UserViewSet, api_root

snippet_list = SnippetViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

snippet_detail = SnippetViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

snippet_highlight = SnippetViewSet({
    'get': 'highlight'
})

user_list = UserViewSet({
    'get': 'list'
})

user_detail = UserViewSet({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    path('', views.api_root),
    path('snippets/', snippet_list, name='snippet_list'),
    path('snippets/<int:pk>', snippet_detail, name='snippet_detail'),
    path(
        'snippets/<int:pk>/highlight', snippet_highlight, name='snippet_highlight'
    ),
    path('users/', user_list, name='user_list'),
    path('users/<int:pk>', user_detail, name='user_detail'),
])
