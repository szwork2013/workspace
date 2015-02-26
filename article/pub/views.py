from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, Http404
from pub.models import Poll, Article
from django.template import Context, loader

# Create your views here.


def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    latest_article_list = Article.objects.all()
    #t = loader.get_template('pub/index.html')
    # c = Context({'latest_poll_list': latest_poll_list,
    #             })
    return render_to_response('pub/index.html', {'latest_article_list': latest_article_list})
#    return HttpResponse(t.render(c))


def detail(request, poll_id):
    # try:
    #    p=Poll.objects.get(pk=poll_id)
    # except Poll.DoesNotExist:
    #    raise Http404
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('pub/detail.html', {'poll': p})


def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %w." % poll_id)


def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)
