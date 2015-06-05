import os

from StringIO import StringIO

from django.conf import settings
from django.core.files.images import ImageFile
from django.shortcuts import render, redirect
from django.utils import simplejson
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt

from .models import ProfilePhoto


def profile(request):
    if request.user.is_authenticated():
        return render(
            request, 'profile.html',
            {'profile': request.user.get_profile()})
    return redirect('admin:index')


@csrf_exempt
def upload_image(request):
    user = request.user
    if (request.method != 'POST' or not request.is_ajax() or
        not user.is_authenticated()):
        raise Http404
    fname = request.GET.get('qqfile', '')
    try:
        fname = '.'.join(fname.split('.')[-2:])
    except IndexError:
        return HttpResponse(
            simplejson.dumps({'success': False}),
            mimetype='application/json')
    f = StringIO()
    while True:
        buf = request.read(512 * 1024)
        if buf:
            f.write(buf)
        else:
            break
    profile = user.get_profile()
    pf = ProfilePhoto(
            profile=profile,
            title=fname.split('.')[0],
            image=ImageFile(f, name=fname))
    pf.save()
    return HttpResponse(
        simplejson.dumps({'success': True, 'url': pf.image.url}),
        mimetype='application/json')
