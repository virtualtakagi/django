from django.urls import path
from cms import views

app_name = 'cms'
urlpatterns = [
    # channel
    path('channel/', views.channel_list, name='channel_list'),   # チャンネル一覧
    path('channel/add/', views.channel_edit, name='channel_add'),  # チャンネル登録
    path('channel/mod/<int:channel_id>/', views.channel_edit, name='channel_mod'),  # チャンネル修正
    path('channel/del/<int:channel_id>/', views.channel_del, name='channel_del'),   # チャンネル削除

    # live
    path('live/', views.live_list, name='live_list'), # ライブ一覧

    # GetLiveInformation
    path('live/update', views.getLive, name="get_live")
]