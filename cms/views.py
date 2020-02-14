from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from datetime import datetime, timedelta, time
# Create your views here.

from cms.models import Live,Channel
from cms.forms import ChannelForm
from . import getlive

def live_list(request):
    """Liveの一覧"""
    #return HttpResponse('ライブの一覧')
    limit = datetime.now() - timedelta(hours=1)
    limit = limit.time()
    lives = Live.objects.filter(starttime__gte=limit).order_by('starttime')
    return render(request,'cms/live_list.html', {'lives': lives})


def channel_list(request):
    """Channelの一覧"""
    #return HttpResponse('ライブの一覧')
    ch = Channel.objects.all().order_by('id')
    return render(request,'cms/channel_list.html', {'channels': ch})


def channel_edit(request, id=None):
    """Channelの編集"""
    #return HttpResponse('ライブの編集')
    if id:   # id が指定されている (修正時)
        channelInstance = get_object_or_404(Channel, pk=id)
    else:    # id が指定されていない (追加時)
        channelInstance = Channel()

    if request.method == 'POST':
        form = ChannelForm(request.POST, instance=channelInstance)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            channelInstance.save()
            return redirect('cms:channel_list')
    else:    # GET の時
        form = ChannelForm(instance=channelInstance)  # channel インスタンスからフォームを作成

    return render(request, 'cms/channel_edit.html', dict(form=form, id=id))


def channel_del(request, id):
    """ライブの削除"""
    #return HttpResponse("ライブの削除")
    liveInstance = get_object_or_404(Channel, pk=id)
    liveInstance.delete()
    return redirect('cms:channel_list')


def getLive(request):
    """ライブ情報の取得"""
    channels = Channel.objects.all()

    for channel in channels:
        
        liveInfo = getlive.getLive(channel.channelid)

        if liveInfo['boolean']:
            info, created = Live.objects.update_or_create(
                thumbnail = liveInfo['thumbnail'],
                channelid = liveInfo['channelid'],
                videoid = liveInfo['videoid'],
                videotitle = liveInfo['videotitle'],
                channeltitle = liveInfo['channeltitle'],
                starttime = liveInfo['starttime'],
                status = liveInfo['status'],
                liveurl = liveInfo['liveurl'],
                channelurl = liveInfo['channelurl']
            )

    return redirect('cms:live_list')
    